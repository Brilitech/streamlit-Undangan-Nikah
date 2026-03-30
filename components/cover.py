"""
Cover Section - Landing page dengan nama tamu
"""
import streamlit as st
from components.utils import create_ornament

def render_cover(guest_name="Bapak/Ibu/Saudara/i"):
    """Render cover section"""
    
    st.markdown(f"""
    <div class="custom-card fade-in-up" style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(95, 113, 97, 0.1) 100%);">
        <div class="bismillah">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        
        <p class="subtitle" style="margin-top: 2rem;">UNDANGAN PERNIKAHAN</p>
        
        {create_ornament()}
        
        <p class="body-text" style="font-size: 1.1rem; margin: 2rem 0;">
            Kepada Yth.<br>
            <strong style="font-size: 1.3rem; color: var(--primary);">{guest_name}</strong>
        </p>
        
        <p class="body-text" style="margin-top: 1.5rem; font-size: 0.95rem; color: #7F8C8D;">
            Tanpa mengurangi rasa hormat, kami mengundang Bapak/Ibu/Saudara/i<br>
            untuk hadir di acara pernikahan kami.
        </p>
        
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
