"""
💌 UNDANGAN PERNIKAHAN DIGITAL
Template undangan pernikahan modern dengan Streamlit

Author: Your Name
Deploy: Streamlit Cloud
"""

import streamlit as st
from config.wedding_config import *
from components.utils import get_theme_colors, apply_custom_css
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

# ========== THEME SETUP ==========
theme = get_theme_colors(THEME, CUSTOM_THEME)
apply_custom_css(theme)

# ========== QUERY PARAMS (Guest Name) ==========
# URL: ?to=Nama%20Tamu
query_params = st.query_params
guest_name = query_params.get("to", "Bapak/Ibu/Saudara/i")

# ========== MAIN CONTAINER ==========
# Remove default padding
st.markdown("""
<style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 1200px;
    }
</style>
""", unsafe_allow_html=True)

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
if FEATURES['countdown']:
    render_countdown_section(AKAD['date'])
    st.markdown("<br><br>", unsafe_allow_html=True)

# 7. GALLERY SECTION
if FEATURES['gallery']:
    render_gallery_section(GALLERY)
    st.markdown("<br><br>", unsafe_allow_html=True)

# 8. GIFT SECTION (Amplop Digital)
if FEATURES['gifts']:
    render_gift_section(GIFTS)
    st.markdown("<br><br>", unsafe_allow_html=True)

# 9. RSVP SECTION
if FEATURES['rsvp']:
    render_rsvp_section()
    st.markdown("<br><br>", unsafe_allow_html=True)

# 10. GUEST MESSAGES
if FEATURES['guest_messages']:
    render_guest_messages()
    st.markdown("<br><br>", unsafe_allow_html=True)

# 11. SOCIAL SHARE
if FEATURES['social_share']:
    render_social_share(GROOM['name'], BRIDE['name'], HASHTAG)
    st.markdown("<br>", unsafe_allow_html=True)

# 12. FOOTER
render_footer(HASHTAG, GROOM['name'], BRIDE['name'])

# ========== MUSIC PLAYER (Optional) ==========
if FEATURES['music']:
    import os
    if os.path.exists(MUSIC['src']):
        st.sidebar.header("🎵 Background Music")
        st.sidebar.info(f"Now Playing: {MUSIC['title']}")
        
        with open(MUSIC['src'], "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.sidebar.audio(audio_bytes, format="audio/mp3")
    else:
        st.sidebar.warning("⚠️ Music file not found. Add music to assets/music/")

# ========== SIDEBAR INFO ==========
with st.sidebar:
    st.header("ℹ️ Info Undangan")
    st.markdown(f"""
    **Mempelai:**  
    {GROOM['name']} & {BRIDE['name']}
    
    **Tanggal Akad:**  
    {AKAD['date']}
    
    **Lokasi:**  
    {AKAD['venue']}
    
    ---
    
    💡 **Tips:**
    - Scroll ke bawah untuk melihat semua section
    - Isi form RSVP untuk konfirmasi kehadiran
    - Bagikan undangan ke teman dan keluarga
    
    ---
    
    Made with ❤️ using Streamlit
    """)
