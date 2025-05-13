import joblib
import numpy as np

modelo_url = joblib.load("modelo_urls.pkl")

def detectar_url_maliciosa(url: str):
    features = np.random.rand(1, 87)  # Simulación. Reemplaza por tus features reales
    resultado = modelo_url.predict(features)[0]
    return "Maliciosa" if resultado == 1 else "Segura"
