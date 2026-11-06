import streamlit as st
st.title ("Convertidor de Temperatura")
st.write ("Convierte grados celsius a Farenheit")

with st.form ("Formulario"):
    celsius = st.number_input (
        label="Introduce la tempertura en grados celsius: ",
        value= None,
        placeholder= "Escribe un número aquí, por ejemplo: 25.5")
    convertir = st.form_submit_button("Convertir")

if convertir:
    if celsius is None:
        st.warning ("Introduce un número válido")
    else:
        farenheit = (celsius * 9/5) + 32
        st.success (f"{celsius}°C son {farenheit:.1f}°F")
