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

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title=META['title'],
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== PERMANENT THEME SETUP (WHITE & GOLD) ==========
# CSS Kustom untuk tampilan putih bersih dengan aksen emas
custom_css = """
<style>
    /* Variabel Warna */
    :root {
        --background-color: #FFFFFF; /* Putih bersih */
        --primary: #D4AF37;          /* Emas Klasik */
        --primary-dark: #B5952F;     /* Emas Gelap (Hover) */
        --text-color: #333333;       /* Abu-abu gelap untuk teks */
        --text-light: #666666;       /* Abu-abu terang untuk subteks */
        --card-bg: #FAFAFA;          /* Putih tulang untuk section card */
        --border-color: #EAEAEA;
    }

    /* Typography */
    h1, h2, h3, .title, .subtitle {
        color: var(--primary) !important;
        text-align: center;
        font-family: 'Georgia', serif; /* Font klasik untuk undangan */
    }

    p, .body-text {
        color: var(--text-color);
        line-height: 1.6;
    }

    /* Ornamen & Separator */
    .separator {
        color: var(--primary);
        font-size: 1.5rem;
        text-align: center;
        margin: 1.5rem 0;
    }

    /* Streamlit UI Overrides (Tombol & Input) */
    .stButton>button {
        background-color: var(--primary);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: var(--primary-dark);
        color: white;
        transform: translateY(-2px);
    }

    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: white;
        border: 1px solid var(--border-color);
        border-radius: 8px;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 1px var(--primary);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ========== FIXED BACKGROUND SETUP (SCROLLESS) ==========
def set_fixed_background(image_path):
    """Fungsi untuk memasang background gambar scrolless (fixed)"""
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            
        bg_css = f"""
        <style>
            /* Mengatur background gambar agar memenuhi layar dan scrolless (fixed) */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_string}");
                background-size: cover;
                background-position: center center;
                background-repeat: no-repeat;
                background-attachment: fixed !important;
            }}
            
            /* Mengubah container aplikasi menjadi transparan elegan (Glassmorphism) */
            .block-container {{
                background-color: rgba(255, 255, 255, 0.88) !important;
                backdrop-filter: blur(5px);
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.1);
                max-width: 1000px;
                padding-top: 2rem !important;
                padding-bottom: 3rem !important;
                margin-top: 2rem !important;
                margin-bottom: 2rem !important;
            }}
            
            /* Hide top padding Streamlit default */
            .stAppHeader {{
                display: none;
            }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)
    else:
        # Peringatan jika gambar tidak ada (hanya muncul di sidebar agar tidak merusak tampilan utama)
        st.sidebar.warning(f"⚠️ Background tidak ditemukan di: {image_path}")

# Panggil fungsi background dengan letak folder yang Anda sebutkan
set_fixed_background("assets/images/bg_freepik.jpg")


# ========== QUERY PARAMS (Guest Name) ==========
# Membaca nama tamu dari URL (contoh: ?to=Budi)
query_params = st.query_params
guest_name = query_params.get("to", "Bapak/Ibu/Saudara/i")

# ========== SECTIONS ==========

# 1. COVER SECTION
render_cover(guest_name)
st.markdown("<br><br>", unsafe_allow_html=True)

# 2. HERO SECTION (Nama Mempelai)
render_hero(GROOM, BRIDE)
st.markdown("<br>", unsafe_allow_html=True)

# 3. QUOTE SECTION (Ayat Al-Quran)
render_quote(QURAN_QUOTE)
st.markdown("<br><br>", unsafe_allow_html=True)

# 4. COUPLE SECTION (Profil Mempelai)
render_couple_section(GROOM, BRIDE)
st.markdown("<br><br>", unsafe_allow_html=True)

# 5. EVENT SECTION (Akad & Resepsi)
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

# 8. GIFT SECTION (Amplop Digital)
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

# ========== MUSIC PLAYER (Optional) ==========
if FEATURES.get('music', False):
    import os
    # Menggunakan absolute path agar file lebih mudah ditemukan
    base_dir = os.path.dirname(os.path.abspath(__file__))
    music_path = os.path.join(base_dir, MUSIC['src'])
    
    if os.path.exists(music_path):
        st.sidebar.header("🎵 Background Music")
        st.sidebar.info(f"Now Playing: {MUSIC['title']}")
        
        # Deteksi format audio secara otomatis
        file_ext = os.path.splitext(music_path)[1].lower()
        if file_ext == '.flac':
            audio_format = 'audio/flac'
        elif file_ext == '.wav':
            audio_format = 'audio/wav'
        elif file_ext == '.ogg':
            audio_format = 'audio/ogg'
        else:
            audio_format = 'audio/mpeg' # Default MP3
            
        try:
            with open(music_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                # TAMBAHKAN autoplay=True DI SINI
                st.sidebar.audio(audio_bytes, format=audio_format, autoplay=True)
        except Exception as e:
            st.sidebar.error("❌ Gagal memuat file musik.")
    else:
        st.sidebar.warning(f"⚠️ File musik tidak ditemukan di path: {music_path}")

# ========== SIDEBAR INFO ==========
with st.sidebar:
    st.header("ℹ️ Info Undangan")
    st.markdown(f"""
    **Mempelai:** {GROOM['name']} & {BRIDE['name']}
    
    **Tanggal Akad:** {AKAD['date']}
    
    **Lokasi:** {AKAD['venue']}
    
    ---
    
    💡 **Tips:**
    - Scroll ke bawah untuk melihat semua section
    - Isi form RSVP untuk konfirmasi kehadiran
    - Bagikan undangan ke teman dan keluarga
    """)
