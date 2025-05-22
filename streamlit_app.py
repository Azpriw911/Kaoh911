import streamlit as st

st.title("Kaoh911")
st.write(
    "🤘😝🤘"
)

st.image("view/Screenshot_20250207-160804.jpg")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka) adalah Bilangan Genap") I
else:
  st.write(f"{angka) adalah Bilangan Ganjil")
