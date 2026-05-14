from typing import Callable
import sqlite3

DB_PATH = "banco.db"


# ── Inicialización de la BD ────────────────────────────────────────────────────

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS cuentas (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                titular TEXT    NOT NULL UNIQUE,
                saldo   REAL    NOT NULL DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS historial (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                cuenta_id  INTEGER NOT NULL,
                tipo       TEXT    NOT NULL,
                monto      REAL    NOT NULL,
                saldo_post REAL    NOT NULL,
                fecha      TEXT    DEFAULT (datetime('now','localtime')),
                FOREIGN KEY (cuenta_id) REFERENCES cuentas(id)
            );
        """)


# ── Repositorio (acceso a datos) ──────────────────────────────────────────────

class CuentaRepo:
    """Toda la lógica SQL vive aquí, separada del dominio."""

    @staticmethod
    def _conectar():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row   # acceso por nombre de columna
        return conn

    # ── cuentas ──

    @staticmethod
    def crear(titular: str, saldo: float) -> int:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.execute(
                    "INSERT INTO cuentas (titular, saldo) VALUES (?, ?)",
                    (titular.strip().title(), saldo)
                )
                return cur.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Ya existe una cuenta para '{titular}'.")

    @staticmethod
    def obtener_todos() -> list[sqlite3.Row]:
        with CuentaRepo._conectar() as conn:
            return conn.execute("SELECT * FROM cuentas ORDER BY titular").fetchall()

    @staticmethod
    def obtener_por_id(cuenta_id: int) -> sqlite3.Row | None:
        with CuentaRepo._conectar() as conn:
            return conn.execute(
                "SELECT * FROM cuentas WHERE id = ?", (cuenta_id,)
            ).fetchone()

    @staticmethod
    def actualizar_saldo(cuenta_id: int, nuevo_saldo: float):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "UPDATE cuentas SET saldo = ? WHERE id = ?",
                (nuevo_saldo, cuenta_id)
            )

    # ── historial ──

    @staticmethod
    def registrar_movimiento(cuenta_id: int, tipo: str, monto: float, saldo_post: float):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO historial (cuenta_id, tipo, monto, saldo_post) VALUES (?, ?, ?, ?)",
                (cuenta_id, tipo, monto, saldo_post)
            )

    @staticmethod
    def historial_por_cuenta(cuenta_id: int) -> list[sqlite3.Row]:
        with CuentaRepo._conectar() as conn:
            return conn.execute(
                "SELECT * FROM historial WHERE cuenta_id = ? ORDER BY fecha",
                (cuenta_id,)
            ).fetchall()


# ── Dominio ───────────────────────────────────────────────────────────────────

class CuentaBancaria:
    def __init__(self, id: int, titular: str, saldo: float, on_transaccion: Callable = None):
        self.__id = id
        self.__titular = titular
        self.__saldo = 0.0
        self.__on_transaccion = on_transaccion

        try:
            self.saldo = saldo
        except ValueError as e:
            print(f"⚠️  {e}")

    # ── Getters / Setters ──

    @property
    def id(self) -> int:
        return self.__id

    @property
    def titular(self) -> str:
        return self.__titular

    @titular.setter
    def titular(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El titular no puede estar vacío.")
        self.__titular = nombre.strip().title()

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, monto: float):
        if monto < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self.__saldo = monto

    @property
    def saldo_fmt(self) -> str:
        return f"$ {self.__saldo:,.0f}"

    # ── Lógica ──

    def __registrar(self, tipo: str, monto: float):
        CuentaRepo.registrar_movimiento(self.__id, tipo, monto, self.__saldo)
        CuentaRepo.actualizar_saldo(self.__id, self.__saldo)
        if self.__on_transaccion:
            self.__on_transaccion(self.__titular, {"tipo": tipo, "monto": monto, "saldo": self.__saldo})

    def depositar(self, monto: float):
        try:
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            self.__saldo += monto
            self.__registrar("Depósito", monto)
            print(f"✅ Depósito exitoso. Nuevo saldo: {self.saldo_fmt}")
        except ValueError as e:
            print(f"⚠️  {e}")

    def girar(self, monto: float):
        try:
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            if monto > self.__saldo:
                raise ValueError("Fondos insuficientes.")
            self.__saldo -= monto
            self.__registrar("Giro", monto)
            print(f"✅ Giro exitoso. Nuevo saldo: {self.saldo_fmt}")
        except ValueError as e:
            print(f"⚠️  {e}")

    def ver_historial(self):
        movimientos = CuentaRepo.historial_por_cuenta(self.__id)
        if not movimientos:
            print("📭 Sin movimientos registrados.")
            return
        # lista de comprensión para formatear cada fila
        lineas = [
            f"  {i+1}. {m['fecha']} | {m['tipo']:<10} | "
            f"Monto: $ {m['monto']:>12,.0f} | Saldo: $ {m['saldo_post']:>12,.0f}"
            for i, m in enumerate(movimientos)
        ]
        print(f"\n📋 Historial de {self.__titular}:")
        print("\n".join(lineas))

    def __str__(self):
        return f"[{self.__id}] 👤 {self.__titular:<15} | Saldo: {self.saldo_fmt}"


# ── Callback ──────────────────────────────────────────────────────────────────

def notificar_transaccion(titular: str, tx: dict):
    print(f"🔔 [{titular}] {tx['tipo']} de $ {tx['monto']:,.0f} → Saldo: $ {tx['saldo']:,.0f}")


# ── Banco ─────────────────────────────────────────────────────────────────────

class Banco:
    def __init__(self):
        init_db()

    def _cargar_cuenta(self, row: sqlite3.Row) -> CuentaBancaria:
        return CuentaBancaria(row["id"], row["titular"], row["saldo"], notificar_transaccion)

    def crear_cuenta(self):
        try:
            nombre = input("Nombre del titular: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            saldo = float(input("Saldo inicial: $ "))
            cuenta_id = CuentaRepo.crear(nombre, saldo)
            # registrar depósito inicial si aplica
            if saldo > 0:
                CuentaRepo.registrar_movimiento(cuenta_id, "Apertura", saldo, saldo)
            print(f"✅ Cuenta creada con ID {cuenta_id}.")
        except ValueError as e:
            print(f"⚠️  {e}")

    def listar_cuentas(self) -> list[CuentaBancaria]:
        rows = CuentaRepo.obtener_todos()
        cuentas = [self._cargar_cuenta(r) for r in rows]   # lista de comprensión
        activas = [c for c in cuentas if c.saldo > 0]

        print(f"\n📊 Total: {len(cuentas)} cuenta(s) | Con saldo: {len(activas)}")
        [print(f"  {c}") for c in cuentas]
        return cuentas

    def seleccionar_cuenta(self) -> CuentaBancaria | None:
        cuentas = self.listar_cuentas()
        if not cuentas:
            print("⚠️  No hay cuentas registradas.")
            return None
        try:
            idx = int(input("Selecciona el número de cuenta: ")) - 1
            if idx < 0:
                raise IndexError
            return cuentas[idx]
        except (ValueError, IndexError):
            print("⚠️  Selección inválida.")
            return None

    def resumen_total(self):
        rows = CuentaRepo.obtener_todos()
        if not rows:
            print("⚠️  No hay cuentas.")
            return
        total = sum(r["saldo"] for r in rows)              # suma pythónica
        titulares = ", ".join(r["titular"] for r in rows)  # join pythónico
        print(f"\n💰 Saldo total: $ {total:,.0f}")
        print(f"👥 Titulares : {titulares}")


# ── Menú ──────────────────────────────────────────────────────────────────────

OPCIONES = {
    "1": "Crear cuenta",
    "2": "Depositar",
    "3": "Girar",
    "4": "Ver historial",
    "5": "Listar cuentas",
    "6": "Resumen total",
    "0": "Salir",
}

def mostrar_menu():
    print("\n" + "═" * 42)
    print("        🏦  BANCO PYTHÓNICO  💾 SQLite")
    print("═" * 42)
    print("\n".join(f"  [{k}] {v}" for k, v in OPCIONES.items()))
    print("═" * 42)


def main():
    banco = Banco()

    acciones: dict[str, Callable] = {
        "1": banco.crear_cuenta,
        "2": lambda: (c := banco.seleccionar_cuenta()) and c.depositar(float(input("Monto: $ "))),
        "3": lambda: (c := banco.seleccionar_cuenta()) and c.girar(float(input("Monto: $ "))),
        "4": lambda: (c := banco.seleccionar_cuenta()) and c.ver_historial(),
        "5": banco.listar_cuentas,
        "6": banco.resumen_total,
    }

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        accion = acciones.get(opcion)
        if accion:
            accion()
        else:
            print("⚠️  Opción no válida.")


if __name__ == "__main__":
    main()