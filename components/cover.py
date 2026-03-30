"""
Cover Section - Landing page dengan nama tamu
"""
import streamlit as st
from components.utils import create_ornament

def render_cover(guest_name="Bapak/Ibu/Saudara/i"):
    """Render cover section"""
    
    # Perhatikan: Saya merapatkan baris HTML agar parser Streamlit tidak bocor
    # Saya juga menyesuaikan background gradient sedikit agar lebih pas dengan tema Putih-Emas
    st.markdown(f"""
    <div class="custom-card fade-in-up" style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(212, 175, 55, 0.08) 0%, rgba(255, 255, 255, 0.1) 100%); border-radius: 15px;">
        <div style="font-size: 2.8rem; color: var(--primary); font-family: 'Amiri', 'Traditional Arabic', serif; margin-bottom: 1rem; line-height: 1.5;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <p class="subtitle" style="margin-top: 1rem; font-size: 1.5rem; letter-spacing: 2px; color: var(--primary);">UNDANGAN PERNIKAHAN</p>
        <div style="margin: 1.5rem 0;">
            {create_ornament()}
        </div>
        <p class="body-text" style="font-size: 1.1rem; margin: 2rem 0;">Kepada Yth.<br><strong style="font-size: 1.5rem; color: var(--primary); display: inline-block; margin-top: 10px;">{guest_name}</strong></p>
        <p class="body-text" style="margin-top: 1.5rem; font-size: 1rem; color: var(--text-light);">Tanpa mengurangi rasa hormat, kami mengundang Bapak/Ibu/Saudara/i<br>untuk hadir di acara pernikahan kami.</p>
        <div style="margin: 1.5rem 0;">
            {create_ornament()}
        </div>
    </div>
    """, unsafe_allow_html=True)
