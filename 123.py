import streamlit as st
st.title('幣值轉換')
o=st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])
d=st.number_input('金額')
op=st.selectbox(
  '換算幣值',
  ['美金','英鎊','歐元'])
