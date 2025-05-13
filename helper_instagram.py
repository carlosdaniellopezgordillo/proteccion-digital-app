import joblib
import numpy as np

modelo_ig = joblib.load("modelo_instagram.pkl")

def detectar_anomalia_instagram(post, likes, comentarios, historias, interacciones):
    features = np.array([[post, likes, comentarios, historias, interacciones]])
    resultado = modelo_ig.predict(features)[0]
    return "Perfil Anómalo" if resultado == 1 else "Perfil Normal"
