"""
💌 UNDANGAN PERNIKAHAN DIGITAL
Template undangan pernikahan modern dengan Streamlit
"""

import streamlit as st
import base64
import os

# Impor semua konfigurasi
from config.wedding_config import *

# Impor komponen
from components.cover import render_cover
from components.hero import render_hero
from components.quote import render_quote
from components.couple import render_couple_section
from components.event import render_event_section
from components.countdown import render_countdown_section
from components.gallery import render_gallery_section
from components.gift import render_gift_section
from components.rsvp import render_rsvp_section, render_guest_messages
from components.footer import render_footer, render_social_share

# ========== SESSION STATE SETUP ==========
# Melacak apakah tamu sudah mengklik tombol "Buka Undangan"
if 'opened' not in st.session_state:
    st.session_state.opened = False

def open_invitation():
    st.session_state.opened = True

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title=META['title'],
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== PERMANENT THEME & BUTTON CSS ==========
custom_css = """
<style>
    :root {
        --primary: #D4AF37;
        --primary-dark: #B5952F;
        --text-color: #333333;
    }

    h1, h2, h3, .title, .subtitle {
        color: var(--primary) !important;
        text-align: center;
        font-family: 'Georgia', serif;
    }

    /* Styling Tombol Standar */
    .stButton>button {
        background-color: var(--primary);
        color: white;
        border: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }

    /* Styling Khusus Tombol Buka Undangan (Primary) */
    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg, #D4AF37 0%, #B5952F 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2.5rem !important;
        font-size: 1.2rem !important;
        border-radius: 50px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
        font-weight: bold !important;
        display: block;
        margin: 0 auto;
    }
    
    .stButton>button[kind="primary"]:hover {
        transform: scale(1.05) translateY(-2px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6) !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ========== FIXED BACKGROUND FUNCTION ==========
def set_fixed_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            
        bg_css = f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_string}");
                background-size: cover;
                background-position: center center;
                background-attachment: fixed !important;
            }}
            .block-container {{
                background-color: rgba(255, 255, 255, 0.9) !important;
                backdrop-filter: blur(8px);
                border-radius: 20px;
                max-width: 1000px;
                padding: 2rem !important;
                margin-top: 2rem !important;
                margin-bottom: 2rem !important;
            }}
            .stAppHeader {{ display: none; }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)

set_fixed_background("assets/images/bg_freepik.jpg")

# ========== QUERY PARAMS ==========
query_params = st.query_params
guest_name = query_params.get("to", "Bapak/Ibu/Saudara/i")

# ==========================================================
# 1. LOGIKA HALAMAN DEPAN (COVER & TOMBOL BUKA)
# ==========================================================
if not st.session_state.opened:
    # Hanya tampilkan cover
    render_cover(guest_name)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Kolom untuk menengahkan tombol
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        # Tombol Buka Undangan dengan ikon amplop
        st.button("📩 Buka Undangan", on_click=open_invitation, type="primary", use_container_width=True)
    
    # Berhenti di sini agar bagian bawah tidak terlihat
    st.stop()


# ==========================================================
# 2. ISI UNDANGAN (MUNCUL SETELAH TOMBOL DIKLIK)
# ==========================================================

# 2. HERO SECTION
render_hero(GROOM, BRIDE)
st.markdown("<br>", unsafe_allow_html=True)

# 3. QUOTE SECTION
render_quote(QURAN_QUOTE)
st.markdown("<br><br>", unsafe_allow_html=True)

# 4. COUPLE SECTION
render_couple_section(GROOM, BRIDE)
st.markdown("<br><br>", unsafe_allow_html=True)

# 5. EVENT SECTION
render_event_section(AKAD, RESEPSI)
st.markdown("<br><br>", unsafe_allow_html=True)

# 6. COUNTDOWN SECTION
if FEATURES.get('countdown', False):
    render_countdown_section(AKAD['date'])
    st.markdown("<br><br>", unsafe_allow_html=True)

# 7. GALLERY SECTION
if FEATURES.get('gallery', False):
    render_gallery_section(GALLERY)
    st.markdown("<br><br>", unsafe_allow_html=True)

# 8. GIFT SECTION
if FEATURES.get('gifts', False):
    render_gift_section(GIFTS)
    st.markdown("<br><br>", unsafe_allow_html=True)

# 9. RSVP SECTION
if FEATURES.get('rsvp', False):
    render_rsvp_section()
    st.markdown("<br><br>", unsafe_allow_html=True)

# 10. GUEST MESSAGES
if FEATURES.get('guest_messages', False):
    render_guest_messages()
    st.markdown("<br><br>", unsafe_allow_html=True)

# 11. SOCIAL SHARE
if FEATURES.get('social_share', False):
    render_social_share(GROOM['name'], BRIDE['name'], HASHTAG)
    st.markdown("<br>", unsafe_allow_html=True)

# 12. FOOTER
render_footer(HASHTAG, GROOM['name'], BRIDE['name'])

# ========== MUSIC PLAYER (Dipicu Setelah Klik Buka) ==========
if FEATURES.get('music', False):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    music_path = os.path.join(base_dir, MUSIC['src'])
    
    if os.path.exists(music_path):
        st.sidebar.header("🎵 Background Music")
        st.sidebar.info(f"Now Playing: {MUSIC['title']}")
        
        file_ext = os.path.splitext(music_path)[1].lower()
        audio_format = 'audio/mpeg' if file_ext == '.mp3' else f'audio/{file_ext[1:]}'
            
        try:
            with open(music_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                # Karena user sudah berinteraksi (klik tombol), autoplay akan bekerja
                st.sidebar.audio(audio_bytes, format=audio_format, autoplay=True)
        except Exception:
            st.sidebar.error("❌ Gagal memuat musik.")

# ========== SIDEBAR INFO ==========
with st.sidebar:
    st.header("ℹ️ Info Undangan")
    st.markdown(f"""
    **Mempelai:** {GROOM['name']} & {BRIDE['name']}
    **Tanggal:** {AKAD['date']}
    **Lokasi:** {AKAD['venue']}
    """)
