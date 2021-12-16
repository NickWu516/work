import streamlit as st
st.title('幣值轉換')
o=st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])
t=st.number_input('金額')
option = st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])

if option=='美金':
  us=t/27.81
  st.write(us,'美元')
elif option=='英鎊':
  uk=t/37.17
  st.write(uk,'英鎊')
elif option=='歐元':
  eu=t/31.54
  st.write(eu,'歐元')
