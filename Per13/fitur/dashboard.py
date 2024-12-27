import streamlit as st

st.title("Halaman Dashboard")

def total_n():
  total_nabung = sum(t['Jumlah']
              for t in st.session_state ['total_semua']
              if t ['Tipe'] == 'Menabung')
  return total_nabung

def total_t():
  total_tarik = sum(t['Jumlah']
              for t in st.session_state ['total_semua']
              if t ['Tipe'] == 'Penarikan')
  return total_tarik

def total_s():
  total_seluruh = total_n() - total_t()
  return total_seluruh


total_nabung = total_n()
total_tarik = total_t()
total_seluruh = total_s()

st.metric("Total Uang yang Masuk", f"Rp.{total_nabung:,}")
st.metric("Total Uang yang Keluar", f"Rp.{total_tarik:,}")
st.metric("Total Uang Keseluruhan", f"Rp.{total_seluruh:,}")
