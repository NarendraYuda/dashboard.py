import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='whitegrid')
import numpy as np


day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')


st.title("Bike Sharing Dashboard")


if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(day_df)

st.subheader('Statistics')
st.write(day_df.describe())


st.subheader('Temperature vs Count')
st.line_chart(day_df[['temp', 'cnt']])

season = st.selectbox('Select Season:', day_df['season'].unique())
filtered_data = day_df[day_df['season'] == season]

st.subheader(f'Data for Season {season}')
st.write(filtered_data)


monthly_counts = day_df.groupby('mnth')['cnt'].sum()
st.subheader('Monthly Bike Rentals')
st.bar_chart(monthly_counts)

avg_rentals_by_season = day_df.groupby('season')['cnt'].mean()


data = {
    'Spring': 2604,
    'Summer': 4992,
    'Fall': 5644,
    'Winter': 4728
}
avg_rentals_by_season = pd.Series(data)


st.subheader('Data Rata-rata Penyewaan Sepeda per Musim')
st.write(avg_rentals_by_season)


plt.figure(figsize=(8, 6))
sns.barplot(x=avg_rentals_by_season.index, y=avg_rentals_by_season.values)
plt.title('Rata-rata Penyewaan Sepeda per Musim')
plt.xlabel('Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)')
plt.ylabel('Rata-rata Jumlah Penyewaan')


st.pyplot(plt)




jam = np.arange(23)
hari_kerja = [36, 19, 12, 5, 9, 25, 99, 471, 244, 138, 159, 202, 204, 192, 200, 280, 525, 486, 330, 235, 166, 118, 88]
akhir_pekan = [98, 72, 55, 25, 8, 18, 40, 111, 253, 321, 371, 377, 370, 360, 350, 340, 300, 250, 180, 140, 110, 90, 85]


st.title("Dashboard Perbandingan Jumlah Penyewaan Sepeda")
st.write("""
Grafik ini membandingkan jumlah penyewaan sepeda per jam pada hari kerja dan akhir pekan.
""")


fig, ax = plt.subplots()
ax.plot(jam, hari_kerja, label='Hari Kerja')
ax.plot(jam, akhir_pekan, label='Akhir Pekan')
ax.set_title('Perbandingan Jumlah Penyewaan Sepeda per Jam (Hari Kerja vs Akhir Pekan)')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
ax.legend(title='Jenis Hari')

st.pyplot(fig)

segmen_rfm = ['444', '111', '222', '344', '233', '433', '322', '133', '122', '211', '333', '311', '411', '422', '244']
jumlah_pengguna = [110, 105, 90, 80, 70, 65, 60, 50, 50, 50, 50, 40, 30, 20, 5]

st.title("Dashboard Distribusi Segmen RFM")
st.write("""
Grafik ini menunjukkan distribusi pengguna berdasarkan segmen RFM.
""")


fig, ax = plt.subplots()
ax.bar(segmen_rfm, jumlah_pengguna)
ax.set_title('Distribusi Segmen RFM')
ax.set_xlabel('Segmen RFM')
ax.set_ylabel('Jumlah Pengguna')

st.pyplot(fig)