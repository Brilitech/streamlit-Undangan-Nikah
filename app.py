"""
💌 UNDANGAN PERNIKAHAN DIGITAL
Template undangan pernikahan modern dengan Streamlit
"""

import streamlit as st

# Impor semua konfigurasi
from config.wedding_config import *

# Hapus impor 'get_theme_colors' dan 'apply_custom_css' karena kita menggunakan tema permanen
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
    page_icon="💒",
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

    /* Reset & Container Utama */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 2rem;
        max-width: 1000px;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stApp {
        background-color: var(--background-color);
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
    if os.path.exists(MUSIC['src']):
        st.sidebar.header("🎵 Background Music")
        st.sidebar.info(f"Now Playing: {MUSIC['title']}")
        
        try:
            with open(MUSIC['src'], "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.sidebar.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.sidebar.error("Gagal memuat musik.")
    else:
        st.sidebar.warning("⚠️ File musik tidak ditemukan. Pastikan path di config benar.")

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
