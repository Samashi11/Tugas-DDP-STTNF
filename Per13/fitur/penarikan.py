import streamlit as st

st.title("Halaman Penarikan")

# Form Menabung
with st.form("Penarikan"):
  nama = st.text_input("Nama Anda")
  jumlah = st.number_input("Jumlah Penarikan", min_value=0)
  tanggal = st.date_input("Tanggal Penarikan")
  waktu = st.time_input("Waktu Penarikan")
  tombol = st.form_submit_button("Simpan")
  if tombol and jumlah >= 50000:
    st.session_state['total_semua'].append({
    'Tipe': 'Penarikan',
    'Jumlah': jumlah
    })
    st.success(f"Anda Berhasil Penarikan sebesar {jumlah}")
  else:
    st.error("Minimal Penarikan 50000")