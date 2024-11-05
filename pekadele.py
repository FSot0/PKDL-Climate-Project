import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Configuración básica del título centrado con iconos de clima
st.markdown("<h1 style='text-align: center;'>🌤️ Dashboard Clima Boadilla 🌦️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>📅 Registro Mensual de Temperatura y Humedad 📊</h3>", unsafe_allow_html=True)

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/FSot0/PKDL-Climate-Project/refs/heads/main/data/raw_data.csv'

# Carga de datos desde GitHub
@st.cache
def load_data(url):
    data = pd.read_csv(url, delimiter=';', encoding='ISO-8859-1')
    data.columns = ['Date', 'Time', 'Temperature', 'Humidity']
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.date  # Convertimos Date a formato de fecha
    data['Time'] = pd.to_datetime(data['Time'], errors='coerce').dt.time  # Convertimos Time a formato de hora
    return data

data = load_data(csv_url)

# Función para encontrar la temperatura más cercana a una hora específica en cada día
def find_closest_temperature(data, target_time_str):
    target_time = datetime.strptime(target_time_str, '%H:%M').time()
    closest_record = data.iloc[0:0]  # Define un DataFrame vacío para almacenar el registro más cercano
    closest_time_diff = timedelta.max  # Inicializa el valor de diferencia de tiempo con el máximo posible
    
    # Recorrer cada registro para encontrar la hora más cercana
    for _, row in data.iterrows():
        time_diff = abs(datetime.combine(datetime.today(), row['Time']) - datetime.combine(datetime.today(), target_time))
        if time_diff < closest_time_diff:
            closest_record = row
            closest_time_diff = time_diff
    return closest_record['Temperature'] if not closest_record.empty else 'No disponible'

# Mostrar las temperaturas más cercanas a horas específicas
st.subheader("🌡️ Temperaturas Registradas a Horas Fijas")
for hour in ['09:00', '15:00', '21:00', '03:00']:
    closest_temp = find_closest_temperature(data, hour)
    st.write(f"🌞 Temperatura a las {hour}: {closest_temp} °C")

# Mostrar el día con la temperatura más baja y más alta
st.subheader("📉 Día con Temperatura Más Baja y 📈 Más Alta")
min_temp_day = data.loc[data['Temperature'].idxmin()]
max_temp_day = data.loc[data['Temperature'].idxmax()]
min_temp = data['Temperature'].min()
max_temp = data['Temperature'].max()

st.write(f"❄️ Temperatura más baja registrada: {min_temp} °C el día {min_temp_day['Date']}")
st.write(f"🔥 Temperatura más alta registrada: {max_temp} °C el día {max_temp_day['Date']}")

# Gráficas de la evolución de temperatura y humedad según los datos registrados
st.subheader("📊 Evolución de la Temperatura Registrada")
fig_temp, ax_temp = plt.subplots(figsize=(10, 5))

data['DateTime'] = pd.to_datetime(data['Date'].astype(str) + ' ' + data['Time'].astype(str))

ax_temp.plot(data['DateTime'], data['Temperature'], marker='o', color='tomato', label='Temperatura (°C)')
plt.title("Evolución de la Temperatura")
plt.xlabel("Fecha y Hora")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.xticks(rotation=45)
st.pyplot(fig_temp)

st.subheader("💧 Evolución de la Humedad Registrada")
fig_hum, ax_hum = plt.subplots(figsize=(10, 5))
ax_hum.plot(data['DateTime'], data['Humidity'], marker='o', color='skyblue', label='Humedad (%)')
plt.title("Evolución de la Humedad")
plt.xlabel("Fecha y Hora")
plt.ylabel("Humedad (%)")
plt.legend()
plt.xticks(rotation=45)
st.pyplot(fig_hum)

st.markdown("<h5 style='text-align: center;'>📈 Monitoriza la evolución de temperatura y humedad según los datos registrados 🕰️</h5>", unsafe_allow_html=True)



