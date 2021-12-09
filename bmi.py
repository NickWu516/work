import streamlit as st

w = st.numberinput('請輸入體重(KG)？'))
h = st.numberinput('請輸入身高(M)？'))
bmi =w/h*h
st.write('BMI為', bmi)
if (bmi < 18):
    st.write('體重過輕')
elif (bmi < 24):
    st.write('體重正常')
elif (bmi < 27):
    st.write('體重過重')
else:
    st.write('體重肥胖')
