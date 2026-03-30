"""
Quote Section - Ayat Al-Quran
"""
import streamlit as st
from components.utils import create_ornament

def render_quote(quote):
    """Render Quranic quote section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk mencegah bug Code Block Markdown Streamlit
    st.markdown(f"""
<div class="custom-card fade-in-up" style="background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 4rem 2rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); margin: 2rem auto; max-width: 800px;">
<div style="margin-bottom: 2rem;">{ornament}</div>
<div class="arabic-text" style="font-size: 2.2rem; color: var(--primary); font-family: 'Amiri', 'Traditional Arabic', serif; line-height: 2.2; margin: 2rem 0; direction: rtl;">
{quote['arabic']}
</div>
<p class="body-text" style="font-style: italic; margin: 2rem 0; line-height: 1.8; color: var(--text-color); font-size: 1.1rem; padding: 0 1rem;">
"{quote['translation']}"
</p>
<p class="subtitle" style="margin-top: 2rem; color: var(--primary-dark); font-weight: bold; letter-spacing: 2px; font-size: 1rem; text-transform: uppercase;">
- {quote['source']} -
</p>
<div style="margin-top: 2rem;">{ornament}</div>
</div>
""", unsafe_allow_html=True)
