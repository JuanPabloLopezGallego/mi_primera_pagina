import streamlit as st
from PIL import Image
st.title ("hola!!, mi nombre es juan pablo")

image= Image.open("digimon.jpg")
st.image (image,caption = "digimon")

st.header("pagina Digimon")
st.write ("me gusta digimon")

texto= st.text_input("escribe tu digimon favorito","este es mi texto")
st.write("tu digimon favorito es", texto)

st.subheader("ahora usemos 2 columnas")

col1,col2= st.columns(2)
with col1:
  st.subheader("esta es la primera columna")
  st.write("las interfaces multimodales mejoran la experiencia de usuario")
  resp=st.checkbox("estoy de acuerdo")
  if resp:
    st.write("correcto")

with col2:
  st.subheader("esta es la segunda columna")
  modo=st.radio ("que modalidad es la principal en tu interfaz", ("visual", "auditiva", "tactil"))
  if modo == "visual":
    st.write("la vista es fundamental para tu interfaz")

  if modo == "auditiva":
    st.write("la audicion es fundamental para tu interfaz")

  if modo == "tactil":
    st.write("el tactil es fundamenta para tu interfaz")
