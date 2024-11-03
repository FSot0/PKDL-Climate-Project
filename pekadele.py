import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración básica
st.title("Dashboard de Datos Climáticos")
st.write("Visualización de temperatura y humedad con datos recogidos cada 5 minutos.")

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/FSot0/Clima_Dashboard/refs/heads/main/USB%20Data%20Logger_210101_2236%20-%20copia.CSV'

# Carga de datos desde GitHub
@st.cache
def load_data(url):
    data = pd.read_csv(url, delimiter=';', encoding='ISO-8859-1')
    data.columns = ['Date_Time', 'Temperature_C', 'Humidity_percent']
    data['Date_Time'] = pd.to_datetime(data['Date_Time'], errors='coerce')
    data.set_index('Date_Time', inplace=True)
    return data

data = load_data(csv_url)

# Estadísticas descriptivas
st.subheader("Estadísticas Descriptivas Diarias")
st.write(data.resample('D').mean().describe())

# Gráfico de tendencias diarias
st.subheader("Tendencias Diarias")
fig, ax = plt.subplots(figsize=(10, 5))
data.resample('D').mean().plot(ax=ax)
plt.title("Promedios diarios de Temperatura y Humedad")
st.pyplot(fig)

# Gráfico de tendencias mensuales
st.subheader("Tendencias Mensuales")
fig, ax = plt.subplots(figsize=(10, 5))
data.resample('M').mean().plot(ax=ax)
plt.title("Promedios mensuales de Temperatura y Humedad")
st.pyplot(fig)
