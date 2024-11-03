import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración básica del título centrado con emoticono
st.markdown("<h1 style='text-align: center;'>🌤️ Dashboard Clima Boadilla 🌤️</h1>", unsafe_allow_html=True)

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/FSot0/PKDL-Climate-Project/refs/heads/main/data/data.CSV'

# Carga de datos desde GitHub
@st.cache
def load_data(url):
    data = pd.read_csv(url, delimiter=';', encoding='ISO-8859-1')
    data.columns = ['Date_Time', 'Temperature_C', 'Humidity_percent']
    data['Date_Time'] = pd.to_datetime(data['Date_Time'], errors='coerce')
    data.set_index('Date_Time', inplace=True)
    return data

data = load_data(csv_url)

# Mostrar las últimas temperaturas registradas a horas específicas
st.subheader("Temperaturas Registradas a Horas Fijas")
for hour in ['09:00', '15:00', '21:00', '03:00']:
    last_record = data[data.index.time == pd.to_datetime(hour).time()]
    last_temp = last_record.iloc[-1]['Temperature_C'] if not last_record.empty else 'No disponible'
    st.write(f"Temperatura a las {hour}: {last_temp} °C")

# Mostrar el día con la temperatura más baja y más alta
st.subheader("Día con Temperatura Más Baja y Más Alta")
min_temp_day = data['Temperature_C'].idxmin()
max_temp_day = data['Temperature_C'].idxmax()
min_temp = data['Temperature_C'].min()
max_temp = data['Temperature_C'].max()

st.write(f"Temperatura más baja registrada: {min_temp} °C el día {min_temp_day.strftime('%Y-%m-%d')}")
st.write(f"Temperatura más alta registrada: {max_temp} °C el día {max_temp_day.strftime('%Y-%m-%d')}")

# Gráfico de la evolución de la temperatura del último día registrado
st.subheader("Evolución de la Temperatura del Último Día Registrado")
last_day = data.loc[data.index.date == data.index.date.max()]
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(last_day.index, last_day['Temperature_C'], marker='o')
plt.title("Evolución de la Temperatura en el Último Día")
plt.xlabel("Hora")
plt.ylabel("Temperatura (°C)")
st.pyplot(fig)

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
