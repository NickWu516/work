import streamlit as st
st.title('幣值轉換')
o=st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])
d=st.number_input('金額')
op=st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])
  
if o==美金 and o2==英鎊:
  uu=d*0.74
  st.wirte(uu,'英鎊')
