import streamlit as st
    
st.set_page_config(page_title='Wellcome to my first Web Application',page_icon='💩')
colum1,colum2 = st.columns(2)
kg = st.number_input('นํ้าหนัก (Kg):')
cm = st.number_input('ส่วนสูง (Cm):')

import io
if st.button('คำนวณ'):
    if cm and kg > 0:
        
        bmi=kg/(cm/100)**2
        st.write(f'ค่า BMI ของคุณคือ: **{bmi:.2f}**')
        
        if bmi <= 18.5 :
            st.info('ผอม')
            st.image('A.png')
        elif bmi < 22.9 :
            st.success('ปกติ')
            st.image('aa.jpg')
        elif bmi < 24.9 :
            st.warning('อ้วน1')
            st.image('C.jpg')
        else :
            st.error('อ้วนมาก')
            st.image('B.png')
    
            text = st.text_input('ข้อความ','คอคอ')
            mp3_fp = io.BytesIO()
            
    
with colum1:
    if st.button('เพลง'):
        st.video('https://youtu.be/XpQLEl38p3c?si=LYKVw_wp2aMmVdP5')
with colum2:
    if st.button('เรื่องเล่า'):
        st.video('https://youtu.be/I4wKuwisRfQ?si=Xshn-lCbzL1vKbd4')
import streamlit as st
import requests
from pathlib import Path

st.title("Botnoi Voice API Demo")

API_URL = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
API_TOKEN = "M3h3RncxMGUzd2gzb3haN1g5YkJheElOQ0pXMjU2MTg5NA=="

text_input = st.text_input("ข้อความที่ต้องการแปลงเป็นเสียง", "สวัสดีครับ")
speaker_id = st.text_input("Speaker ID", "1")
generate_btn = st.button("Generate Voice")

if generate_btn:
    payload = {
        "text": text_input,
        "speaker": speaker_id,
        "volume": 1,
        "speed": 1,
        "type_media": "mp3",
        "save_file": "true",
        "language": "th",
        "page": "user"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "botnoi-token": API_TOKEN
    }

    try:
        res = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        res.raise_for_status()
        data = res.json()
        st.write("API Response:", data)

        # ดึง URL ไฟล์เสียง
        audio_url = (
            data.get("url")
            or data.get("audio_url")
            or (data.get("data") or {}).get("url")
        )

        if audio_url:
            audio_bytes = requests.get(audio_url, timeout=30).content
            out_path = Path("botnoi_voice.mp3")
            out_path.write_bytes(audio_bytes)
            st.success(f"✅ บันทึกเสียงเรียบร้อย → {out_path.resolve()}")
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("ไม่พบลิงก์ไฟล์เสียงใน response")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
