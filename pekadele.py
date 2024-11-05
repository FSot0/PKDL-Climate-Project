import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración básica del título centrado con iconos de clima
st.markdown("<h1 style='text-align: center;'>🌤️ Dashboard Clima Boadilla 🌦️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>📅 Registro Mensual de Temperatura y Humedad 📊</h3>", unsafe_allow_html=True)

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/FSot0/PKDL-Climate-Project/refs/heads/main/data/data.CSV'

# Carga de datos desde GitHub
@st.cache
def load_data(url):
    data = pd.read_csv(url, delimiter=';', encoding='ISO-8859-1')
    data.columns = ['YY/MM/DD', 'Time', 'Temperature', 'Humidity']
    data['Date_Time'] = pd.to_datetime(data['YY/MM/DD'] + ' ' + data['Time'], errors='coerce')
    data.set_index('Date_Time', inplace=True)
    return data

data = load_data(csv_url)

# Mostrar las últimas temperaturas registradas a horas específicas
st.subheader("🌡️ Temperaturas Registradas a Horas Fijas")
for hour in ['09:00', '15:00', '21:00', '03:00']:
    last_record = data[data.index.time == pd.to_datetime(hour).time()]
    last_temp = last_record.iloc[-1]['Temperature'] if not last_record.empty else 'No disponible'
    st.write(f"🌞 Temperatura a las {hour}: {last_temp} °C")

# Mostrar el día con la temperatura más baja y más alta
st.subheader("📉 Día con Temperatura Más Baja y 📈 Más Alta")
min_temp_day = data['Temperature'].idxmin()
max_temp_day = data['Temperature'].idxmax()
min_temp = data['Temperature'].min()
max_temp = data['Temperature'].max()

st.write(f"❄️ Temperatura más baja registrada: {min_temp} °C el día {min_temp_day.strftime('%Y-%m-%d')}")
st.write(f"🔥 Temperatura más alta registrada: {max_temp} °C el día {max_temp_day.strftime('%Y-%m-%d')}")

# Gráficas de la evolución mensual de temperatura y humedad
st.subheader("📅 Evolución Mensual de Temperatura y Humedad")
monthly_data = data.resample('M').mean()

# Gráfico de la evolución mensual de la temperatura
fig_temp, ax_temp = plt.subplots(figsize=(10, 5))
ax_temp.plot(monthly_data.index, monthly_data['Temperature'], marker='o', color='tomato', label='Temperatura (°C)')
plt.title("Evolución Mensual de la Temperatura")
plt.xlabel("Mes")
plt.ylabel("Temperatura (°C)")
plt.legend()
st.pyplot(fig_temp)

# Gráfico de la evolución mensual de la humedad
fig_hum, ax_hum = plt.subplots(figsize=(10, 5))
ax_hum.plot(monthly_data.index, monthly_data['Humidity'], marker='o', color='skyblue', label='Humedad (%)')
plt.title("Evolución Mensual de la Humedad")
plt.xlabel("Mes")
plt.ylabel("Humedad (%)")
plt.legend()
st.pyplot(fig_hum)

st.markdown("<h5 style='text-align: center;'>📈 Monitoriza las tendencias mensuales para análisis climático 🕰️</h5>", unsafe_allow_html=True)

