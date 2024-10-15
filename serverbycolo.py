import streamlit as st

# Define las URLs para los tests
test_par_url = "https://tally.so/r/m6Op2Y"  # Cambia este link por la URL de tu test para números pares
test_impar_url = "https://tally.so/r/wQJOxp"  # Cambia este link por la URL de tu test para números impares

# Leer el valor actual del contador desde un archivo de texto
def leer_contador():
    try:
        with open("contador.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Escribir el valor actualizado del contador en el archivo de texto
def escribir_contador(valor):
    with open("contador.txt", "w") as file:
        file.write(str(valor))

# Incrementar el contador y devolver el nuevo valor
def incrementar_contador():
    contador = leer_contador()
    contador += 1
    escribir_contador(contador)
    return contador

# Interfaz de Streamlit
st.title("Bienvenido al Test")
st.write("Haz clic en el botón para empezar el test.")

# Botón para iniciar el test
if st.button("Empezar Test"):
    contador = incrementar_contador()
    
    # Determina el test correspondiente y muestra el enlace
    if contador % 2 == 0:
        st.success(f"Redirigiendo al test par (Visitas: {contador})...")
        st.write(f"[Ir al test par]({test_par_url})", unsafe_allow_html=True)
    else:
        st.success(f"Redirigiendo al test impar (Visitas: {contador})...")
        st.write(f"[Ir al test impar]({test_impar_url})", unsafe_allow_html=True)
