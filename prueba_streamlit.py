import streamlit as st

st.title("Sistema de Ventas Académico")

# Datos iniciales
ventas = [1200, 3500, 800, 2200, 1500, 700, 4000, 950]

# --- ESTRUCTURA DE CONTROL: SIDEBAR (Para simular el menú) ---
st.sidebar.header("Menú del Sistema")
opcion = st.sidebar.selectbox("Selecciona una opción:", 
    ["-", "1", "2", "3", "4", "5", "6", "7", "8", "0"])

# --- ESTRUCTURA DE CONTROL: MATCH ---
match opcion:
    case "1":
        st.subheader("Todas las ventas")
        # --- ESTRUCTURA DE CONTROL: WHILE ---
        # Usamos un while con un contador para recorrer la lista
        i = 0
        while i < len(ventas):
            st.write(f"Venta {i+1}: ${ventas[i]}")
            i += 1

    case "2":
        st.subheader("Ventas mayores a $1000")
        # --- ESTRUCTURA DE CONTROL: FOR e IF ---
        resultados = []
        for v in ventas:
            if v > 1000:
                resultados.append(v)
        st.write(resultados)

    case "3":
        st.subheader("Ventas menores o iguales a $1000")
        # --- ESTRUCTURA DE CONTROL: FOR e IF ---
        resultados = [v for v in ventas if v <= 1000]
        st.write(resultados)

    case "4":
        total = sum(ventas)
        st.metric("Total de Ventas", f"${total}")

    case "5":
        promedio = sum(ventas) / len(ventas)
        st.metric("Promedio", f"${promedio:.2f}")

    case "6":
        st.subheader("Ventas en rango personalizado")
        l_inf = st.number_input("Límite inferior", value=0)
        l_sup = st.number_input("Límite superior", value=2000)
        
        # --- ESTRUCTURA DE CONTROL: FOR e IF ---
        filtradas = []
        for v in ventas:
            if l_inf <= v <= l_sup:
                filtradas.append(v)
        st.write(filtradas)

    case "7":
        promedio = sum(ventas) / len(ventas)
        # --- ESTRUCTURA DE CONTROL: FOR e IF ---
        mayores = [v for v in ventas if v > promedio]
        st.write(f"Promedio: ${promedio:.2f}")
        st.write(f"Ventas mayores al promedio: {mayores}")

    case "8":
        st.subheader("Buscador de montos")
        buscar = st.number_input("Monto a buscar", step=1)
        if st.button("Ejecutar búsqueda"):
            # --- ESTRUCTURA DE CONTROL: IF (in) ---
            if buscar in ventas:
                st.success("Venta encontrada")
            else:
                st.error("No encontrada")

    case "0":
        st.warning("Has seleccionado Salir. Reinicia la aplicación para volver a usarla.")
        st.stop() # Detiene la ejecución de la app de Streamlit

    case _:
        st.info("Selecciona una opción del menú lateral para ejecutar la lógica.")