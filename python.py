import streamlit as st
    
st.set_page_config(page_title='Wellcome to my first Web Application',page_icon='💩')
colum1,colum2 = st.columns(2)
kg = st.number_input('นํ้าหนัก (Kg):')
cm = st.number_input('ส่วนสูง (Cm):')

import io
if st.button('คำนวณ'):
    bmi=kg/(cm/100)**2
    st.write(f'ค่า BMI ของคุณคือ: **{bmi:.2f}**')
    if bmi <= 18.5 :
        st.info('ผอม')
        st.image('A.png')
    elif bmi < 22.9 :
        st.success('ปกติ')
        st.image('https://cf.shopee.co.th/file/905f5cc2292c5e4fbe0dc0c1b24b4efb')
    elif bmi < 24.9 :
        st.warning('อ้วน1')
        st.image('C.jpg')
    else :
        st.error('อ้วนมาก')
        st.image('B.png')

        text = st.text_input('ข้อความ','คอวออายอ')
        tts = gTTS(text=word, lang='th')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        st.audio(mp3_fp, format='audio/mp3')
    
with colum1:
    if st.button('เพลง'):
        st.video('https://youtu.be/XpQLEl38p3c?si=LYKVw_wp2aMmVdP5')
with colum2:
    if st.button('เรื่องเล่า'):
        st.video('https://youtu.be/I4wKuwisRfQ?si=Xshn-lCbzL1vKbd4')







