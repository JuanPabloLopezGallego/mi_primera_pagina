import streamlit as st
from PIL import Image
st.title ("hola!!, mi nombre es Juan Pablo")

image= Image.open("digimon.jpg")
st.image (image,caption = "Digimon")

st.header("página Digimon")
st.write ("página sobre Digimon")

texto= st.text_input("Escribe tu Digimon favorito","este es mi texto")
st.write("Tu Digimon favorito es", texto)

st.subheader("Ahora usemos 2 columnas")

col1,col2= st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp=st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto")

with col2:
  st.subheader("Esta es la segunda columna")
  modo=st.radio ("¿Qué modalidad es la principal en tu interfaz?", ("Visual", "Auditiva", "Táctil"))
  if modo == "visual":
    st.write("La vista es fundamental para tu interfaz")

  if modo == "auditiva":
    st.write("La audición es fundamental para tu interfaz")

  if modo == "tactil":
    st.write("El táctil es fundamenta para tu interfaz")
