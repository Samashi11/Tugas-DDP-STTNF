import streamlit as st

st.title("Halaman Menabung")

# Form Menabung
with st.form("Menabung"):
  nama = st.text_input("Nama Anda")
  jumlah = st.number_input("Jumlah Menabung", min_value=0)
  tanggal = st.date_input("Tanggal Menabung")
  waktu = st.time_input("Waktu Menabung")
  tombol = st.form_submit_button("Simpan")
  if tombol and jumlah >= 50000:
    st.session_state['total_semua'].append({
      "Tipe" : "Menabung",
      "Jumlah" : jumlah,
    })
    st.success(f"Anda Berhasil Menabung sebesar {jumlah}")
  else:
    st.error("Minimal Menabung 50000")