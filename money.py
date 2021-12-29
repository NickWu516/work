import streamlit as st

st.title('匯率')
d=st.number_input('金額')
o=st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])

if o=='美金':
  u=d/27.265
  st.write(u,'元')
elif o=='英鎊':
  uk=d/35.92
  st.write(uk,'元')
elif o=='歐元':
  eu=d/30.42
  st.write(eu,'元')
