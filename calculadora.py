import streamlit as st

# Funciones de lógica (se mantienen iguales)
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir por cero."

# Interfaz de Streamlit
st.title("🧮 CALCULADORA")

# Columnas para que los inputs se vean mejor (opcional)
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Ingrese el primer número:", value=0.0)
with col2:
    num2 = st.number_input("Ingrese el segundo número:", value=0.0)

st.write("### Seleccione la operación:")

# Usamos un selectbox en lugar de ingresar números del 1 al 4
opcion = st.selectbox(
    "Operaciones disponibles",
    ("Suma", "Resta", "Multiplicación", "División")
)

# Botón para ejecutar el cálculo
if st.button("Calcular"):
    if opcion == 'Suma':
        resultado = sumar(num1, num2)
        st.success(f"El resultado de la suma es: {resultado}")
        
    elif opcion == 'Resta':
        resultado = restar(num1, num2)
        st.success(f"El resultado de la resta es: {resultado}")
        
    elif opcion == 'Multiplicación':
        resultado = multiplicar(num1, num2)
        st.success(f"El resultado de la multiplicación es: {resultado}")
        
    elif opcion == 'División':
        resultado = dividir(num1, num2)
        if isinstance(resultado, str): # Si devuelve el mensaje de error
            st.error(resultado)
        else:
            st.success(f"El resultado de la división es: {resultado}")