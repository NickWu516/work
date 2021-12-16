import streamlit as st
st.title('台幣轉換')
t=st.number_input('金額')
option = st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])
confirm_input=st.button('確認')
