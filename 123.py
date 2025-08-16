import streamlit as st

st.set_page_config(page_title='Wellcome to my first Web Application',page_icon='💩')
kg = st.number_input('นํ้าหนัก (Kg):')
cm = st.number_input('ส่วนสูง (Cm):')
if st.button('คำนวณ'):
    bmi=kg/(cm/100)**2
    if bmi <= 18.5 :
        st.info('ผอม')
    elif bmi < 22.9 :
        st.success('ปกติ')
    elif bmi < 24.9 :
        st.warning('อ้วน1')
    else :
        st.error('อ้วนมาก')
