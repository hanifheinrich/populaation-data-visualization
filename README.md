# Dashboard Kependudukan Nagari Tanjung Balik

Dasbor Nagari Tanjung Balik dibangun untuk mendukung program digitalisasi desa dengan menyediakan platform yang menampilkan statistik kependudukan yang komprehensif. Situs web ini dibangun sebagai bagian dari proyek KKN dan memanfaatkan teknologi Streamlit untuk memastikan kemudahan penggunaan dan interaktivitas.

## Table of Contents:

- Dataset
- Data Visualization

  
## Dataset
- Dataset penduduk nagari tanjung balik diambil dari Kartu Keluarga penduduk yang merupakan bagain dari program kerja pendataan statistik nagari tanjung balik
- Dataset PHBS Pilot Project didapatkan dari youtube PKK Tanjung Balik: https://www.youtube.com/watch?v=CXfe1t_8EzY

## Data Visualization
```python
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#header website
col1,col2 = st.columns([2,8])
with col1:
  logo=Image.open('logo.png')
  st.image(logo, width=170)
with col2:
  st.title ("Dashboard Nagari Tanjung Balik")
  st.subheader ("Tanjuang Balik, Kecamatan X Koto Diatas, Kabupaten Solok, Sumatera Barat")
st.write("---")

#pilihtahun
st.write("Pilih Tahun")
domain = st.selectbox("Pilih Statistik Tahun",['2023','2024','2025'])
st.write("---")

#demografiwilayah
st.header ("Data Penduduk")
st.text ("Jelajahi statistik dan demografi penduduk desa kami melalui bagian informasi populasi yang interaktif dan informatif.")
datadw = pd.read_csv('data/nagari_penduduk.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datadw)
with col2:
  labels = 'Pasa Mudiak', 'Pasa Hilia', 'Kubang Tigo', 'Guak Nomeh', 'Batu Laweh'
  sizes = [629, 683, 628, 393, 74]
  explode = (0, 0.1,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  st.pyplot(fig1)
st.write("---")
```
![image](https://github.com/user-attachments/assets/6de36acb-f6fa-47ae-b3e9-dc028025ab9e)
