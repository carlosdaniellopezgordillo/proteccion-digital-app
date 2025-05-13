import streamlit as st
from helper_urls import detectar_url_maliciosa
from helper_instagram import detectar_anomalia_instagram

st.set_page_config(page_title="Protección Digital con IA", page_icon="🛡️", layout="centered")

st.title("🛡️ Protección Digital con Inteligencia Artificial")

opcion = st.sidebar.radio("Selecciona una funcionalidad:", ["🔗 Detección de URLs", "📱 Detección en Instagram"])

if opcion == "🔗 Detección de URLs":
    st.header("🔗 Verificador de URLs Maliciosas")
    url = st.text_input("Introduce una URL para analizar")
    if st.button("Analizar URL"):
        resultado = detectar_url_maliciosa(url)
        st.success(f"Resultado: {resultado}")

elif opcion == "📱 Detección en Instagram":
    st.header("📱 Analizador de Comportamiento en Instagram")
    post = st.number_input("Cantidad de posteos", min_value=0)
    likes = st.number_input("Promedio de likes", min_value=0)
    comentarios = st.number_input("Promedio de comentarios", min_value=0)
    historias = st.number_input("Historias publicadas por día", min_value=0)
    interacciones = st.number_input("Interacciones semanales", min_value=0)

    if st.button("Analizar Perfil"):
        resultado = detectar_anomalia_instagram(post, likes, comentarios, historias, interacciones)
        st.success(f"Resultado: {resultado}")
