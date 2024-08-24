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

#datapendidikan
st.header ("Data Pendidikan")
st.text ("Eksplorasi data pendidikan masyarakat Nagari dalam bagian pendidikan")
datapk = pd.read_csv('data/nagari_pendidikan.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datapk)
with col2:
  labels = 'Tidak/Belum Sekolah', 'PAUD/TK', 'Belum Tamat SD','Tamat SD', 'SMP', 'SMA', 'D1-D3', 'D4/S1','S2','S3'
  sizes = [580, 58, 505, 535, 295, 333, 36, 63, 2, 0]
  explode = (0, 0.1,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  st.pyplot(fig1)
st.write("---")

#datapekerjaan
st.header ("Data Pekerjaan")
st.text ("Telusuri gambaran pekerjaan masyarakat nagari melalui bagian informasi pekerjaan")
datapn = pd.read_csv('data/nagari_pekerjaan.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datapn)
with col2:
  labels = 'Tidak/Belum Bekerja', 'Pelajar/Mahasiswa', 'Petani', 'Ibu Rumah Tangga', 'Pedagang', 'TNI/Polisi', 'PNS', 'Perangkat Nagari', 'Honorer', 'Buruh Harian', 'Karyawan Swasta', 'Wiraswasta'
  sizes = [611,428,378,620,17,1,72,13,20,35,37,121]
  explode = (0, 0.1,0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  st.pyplot(fig1)
st.write("---")

#datajeniskelamin
st.subheader ("Data Jenis Kelamin")
st.text ("Temukan perbandingan jenis kelamin masyarakat nagari melalui bagian statistik Jenis Kelamin")
datajk = pd.read_csv('data/nagari_kelamin.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datajk)
with col2:
  labels = 'Laki-laki', 'Perempuan'
  sizes = [1217, 1190]
  explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  st.pyplot(fig1)
st.write("---")

st.subheader ("Data Usia Penduduk")
st.text ("Analisis usia penduduk terhadap distribusi demografi nagari tersedia dalam bagian informasi usia")
datau = pd.read_csv('data/usia.csv')
col1, col2 = st.columns([1,1])
with col1:
  st.dataframe(datau)
with col2:
  labels = 'Dibawah 1 Tahun', '2-4 Tahun', '5-9 Tahun', '10-14 Tahun', '15-19 Tahun', '20-24 Tahun', '30-34 Tahun', '35-39 Tahun', '40-44 Tahun'
  sizes = [5, 7,5,6,13,21,7,11,5]
  explode = (0, 0.1, 0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  st.pyplot(fig1)
st.write("---")