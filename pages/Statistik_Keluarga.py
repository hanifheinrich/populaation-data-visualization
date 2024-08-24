import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#header website
col1,col2 = st.columns([2,8])
with col1:
  logo=Image.open('logo.png')
  st.image(logo, width=170)
with col2:
  st.title ("Dashboard Nagari Tanjung Balik")
  st.subheader ("Tanjuang Balik, Kecamatan X Koto Diatas, Kabupaten Solok, Sumatera Barat")
st.write("---")

st.write("Pilih Tahun")
domain = st.selectbox("Pilih Statistik Tahun",['2022','2023','2024'])

st.subheader ("Data Klasifikasi Sosial")
st.text ("Menyajikan klasifikasi sosial masyarakat nagari melalui bagian informasi struktur sosial")
dataks = pd.read_csv('data/klasifikasi_sosial.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(dataks)
with col2:
  st.bar_chart(data=dataks, x="Jenis Kelompok", y="Jumlah")