class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = 0
        try:
            self.saldo = saldo_inicial  # ✅ Usa el setter correctamente
        except ValueError as e:
            print(f"Error: {e}")

    @property
    def saldo(self):
        return f"$ {self.__saldo:,.0f}"

    @saldo.setter
    def saldo(self, monto):
        if monto < 0:
            raise ValueError("No se permiten saldos negativos")
        self.__saldo = monto

    @property
    def titular(self):
        return self.__titular

    def girar(self, monto):
        match monto > self.__saldo:
            case True:
                print("Error: Fondos insuficientes para realizar el giro.")
            case False:
                self.__saldo -= monto
                print(f"Giro exitoso de {monto}. Nuevo saldo: {self.saldo}")  # ✅

    def __str__(self):
        return f"Cuenta de {self.__titular} - Saldo: {self.saldo}"  # ✅

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Nico", 1500000) 
    cuenta2 = CuentaBancaria("Tabita", 300000)
    print(cuenta1)
    print(cuenta2)  
    cuenta1.girar(2000000)  # Intento de giro que excede el saldo
    cuenta1.girar(500000)   # Giro exitoso
    print(cuenta1)  # Verificar el nuevo saldo después del giro
    print(cuenta2)  # Verificar que la cuenta de Tabita no se ha modificado
    