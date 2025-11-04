import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Judul dan Deskripsi Halaman
# -----------------------------
st.set_page_config(page_title="Visualisasi Data Mahasiswa", page_icon="🎓", layout="centered")

st.title("🎓 Visualisasi Data Mahasiswa")
st.markdown("""
Aplikasi ini menampilkan hasil visualisasi dari **data mahasiswa** berdasarkan 
beberapa faktor seperti prestasi, kepemilikan KIP, nilai ujian, dan penghasilan orang tua.  
Tujuannya untuk melihat **pola hubungan antara faktor sosial ekonomi dan prestasi siswa.**
""")

# -----------------------------
# Baca Dataset
# -----------------------------
df = pd.read_csv("student-data-train.csv")
# -----------------------------
# Interaktivitas: Filter Data
# -----------------------------
st.sidebar.header("🔍 Filter Data")
pilih_prestasi = st.sidebar.selectbox("Pilih Prestasi:", options=sorted(df["Prestasi"].unique()))
filtered_df = df[df["Prestasi"] == pilih_prestasi]

st.write(f"Menampilkan data untuk siswa dengan Prestasi = {pilih_prestasi}")

# -----------------------------
# Tampilkan Data
# -----------------------------
st.subheader("📋 Tabel Data Mahasiswa")
st.dataframe(df.head())

# -----------------------------
# Visualisasi 1: Pie Chart Prestasi
# -----------------------------
st.subheader("1️⃣ Distribusi Prestasi Siswa")
pie = px.pie(filtered_df,
    names='Prestasi',
    title='Perbandingan Jumlah Siswa Berprestasi vs Tidak Berprestasi',
    color='Prestasi',
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(pie, use_container_width=True)
st.caption("Grafik ini menunjukkan proporsi antara siswa yang **berprestasi (1)** dan **tidak berprestasi (0)**. "
           "Dari grafik, kita dapat melihat seberapa besar perbandingan antara keduanya.")

# -----------------------------
# Visualisasi 2: Bar Chart KIP vs Nilai
# -----------------------------
st.subheader("2️⃣ Rata-rata Nilai Berdasarkan Kepemilikan KIP")
kip_chart = filtered_df.groupby('PunyaSejenisKIP')['NilaiUjian'].mean().reset_index()
bar = px.bar(
    kip_chart,
    x='PunyaSejenisKIP',
    y='NilaiUjian',
    color='PunyaSejenisKIP',
    text_auto='.2f',
    color_discrete_sequence=px.colors.qualitative.Vivid,
    title='Rata-rata Nilai Ujian Siswa dengan dan tanpa KIP'
)
st.plotly_chart(bar, use_container_width=True)
st.caption("Grafik batang ini memperlihatkan perbandingan **rata-rata nilai ujian** antara siswa yang "
           "memiliki kartu bantuan pendidikan (KIP) dan yang tidak. Perbedaan nilai menunjukkan "
           "pengaruh dukungan finansial terhadap hasil belajar.")

# -----------------------------
# Visualisasi 3: Scatter Plot Penghasilan vs Nilai
# -----------------------------
st.subheader("3️⃣ Hubungan Penghasilan Orang Tua dan Nilai Ujian")
scatter = px.scatter(filtered_df,
    x='PenghasilanOrtu',
    y='NilaiUjian',
    color='Prestasi',
    title='Korelasi antara Penghasilan Orang Tua dan Nilai Ujian',
    color_discrete_sequence=px.colors.qualitative.Prism
)
st.plotly_chart(scatter, use_container_width=True)
st.caption("Diagram sebar ini menunjukkan hubungan antara **penghasilan orang tua** dan **nilai ujian siswa**. "
           "Dapat diamati apakah siswa dengan penghasilan orang tua lebih tinggi cenderung memiliki nilai ujian yang lebih baik.")

# -----------------------------
# Penutup
# -----------------------------
st.markdown("""
---
✨ **Kesimpulan Singkat:**  
Berdasarkan visualisasi di atas, faktor ekonomi dan kepemilikan bantuan pendidikan memiliki korelasi dengan prestasi akademik siswa.  
Visualisasi ini dapat digunakan oleh lembaga pendidikan untuk memahami kondisi sosial siswa dan memberikan dukungan yang tepat.
""")
