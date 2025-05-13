# 🛡️ Protección Digital con Inteligencia Artificial

Este proyecto es una aplicación web desarrollada con **Streamlit** que integra dos modelos de aprendizaje automático para ofrecer una herramienta de protección digital contra amenazas comunes en línea:

1. **Detección de URLs maliciosas**
2. **Detección de comportamientos anómalos en perfiles de Instagram**

---

## 📌 Objetivo del Proyecto

Crear una plataforma accesible y funcional que permita a los usuarios:
- Verificar si una URL puede representar una amenaza potencial (phishing, malware, etc.).
- Analizar perfiles de Instagram para detectar patrones de comportamiento sospechosos que podrían indicar suplantación de identidad o actividad automatizada.

---

## ⚙️ Tecnologías Utilizadas

- **Python 3.9+**
- **Streamlit** – Para la interfaz web.
- **Scikit-learn** – Para los modelos de Machine Learning.
- **NumPy / Pandas** – Para manejo de datos.
- **Joblib** – Para guardar y cargar modelos.

---

## 🧠 Modelos de IA Implementados

### 🔗 1. Detección de URLs Maliciosas
- **Entrada**: URL escrita por el usuario.
- **Proceso**:
  - Se extraen características de la URL (hasta 87 en el modelo original).
  - El modelo analiza patrones comunes en URLs maliciosas.
- **Salida**: Clasificación como `Segura` o `Maliciosa`.

### 📱 2. Detección de Anomalías en Perfiles de Instagram
- **Entrada**: Valores numéricos relacionados con la actividad del perfil (posts, likes, comentarios, historias, interacciones).
- **Proceso**:
  - Se normalizan los datos y se comparan con perfiles típicos.
  - Se evalúan desviaciones anómalas.
- **Salida**: Clasificación como `Perfil Normal` o `Perfil Anómalo`.

---

## 🖥️ Uso de la Aplicación

1. Ejecutar localmente con:
   ```bash
   streamlit run app.py
   ```

2. En la interfaz web:
   - Selecciona el módulo desde el menú lateral.
   - Introduce los datos requeridos.
   - Haz clic en el botón para obtener el resultado.

---

## 🌐 Despliegue en Render

La aplicación está diseñada para ejecutarse en la plataforma **Render.com**, permitiendo su disponibilidad en línea 24/7.

### Pasos para el despliegue:

1. Crear un repositorio en GitHub y subir el contenido del proyecto.
2. Conectar GitHub a Render.
3. Crear un nuevo servicio web con los siguientes parámetros:
   - **Start Command**:  
     ```
     streamlit run app.py
     ```
   - **Build**: Automática desde `requirements.txt`.

---

## 📂 Estructura del Proyecto

```
proteccion-digital-app/
├── app.py                  # Interfaz Streamlit
├── helper_urls.py         # Funciones de predicción para URLs
├── helper_instagram.py    # Funciones de predicción para Instagram
├── modelo_urls.pkl        # Modelo de detección de URLs maliciosas
├── modelo_instagram.pkl   # Modelo de detección de perfiles anómalos
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación del proyecto
```

---

## 📈 Ejemplo de Uso

### Detección de URL

- Entrada: `http://update-account-login.verifica-tu-cuenta.xyz`
- Resultado: `Maliciosa`

### Detección en Instagram

- Entrada: `Posteos: 3`, `Likes: 4000`, `Comentarios: 2`, `Historias: 0`, `Interacciones: 15`
- Resultado: `Perfil Anómalo`

---

## 👨‍💻 Autor

Este proyecto fue desarrollado por **Carlos Daniel Lopez Gordillo** como parte del prototipo universitario **"Protección Digital: Cómo la IA combate el robo de identidad"** en la Universidad Nacional Rosario Castellanos, Licenciatura en Ciencias de Datos para Negocios.

---

## ✅ Licencia

Este proyecto es de uso académico y educativo. No se autoriza su uso comercial sin consentimiento del autor.

**© 2025 Carlos Daniel Lopez Gordillo**
