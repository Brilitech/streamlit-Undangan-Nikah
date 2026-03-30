"""
Quote Section - Ayat Al-Quran
"""
import streamlit as st
from components.utils import create_ornament

def render_quote(quote):
    """Render Quranic quote section"""
    
    st.markdown(f"""
    <div class="custom-card fade-in-up" style="text-align: center; padding: 3rem 2rem;">
        {create_ornament()}
        
        <div class="arabic-text" style="margin: 2rem 0;">
            {quote['arabic']}
        </div>
        
        <p class="body-text" style="font-style: italic; margin: 1.5rem 0; line-height: 1.8;">
            "{quote['translation']}"
        </p>
        
        <p class="subtitle" style="margin-top: 1rem;">
            {quote['source']}
        </p>
        
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
