"""
Hero Section - Nama mempelai utama
"""
import streamlit as st
from components.utils import create_ornament, create_divider

def render_hero(groom, bride):
    """Render hero section with bride and groom names"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk mencegah bug Code Block Markdown Streamlit
    st.markdown(f"""
<div class="fade-in-up" style="text-align: center; padding: 4rem 1rem;">
<div style="margin-bottom: 2rem;">{ornament}</div>
<p class="subtitle" style="margin-bottom: 1rem; color: var(--text-light); letter-spacing: 4px; font-size: 1.2rem; text-transform: uppercase;">THE WEDDING OF</p>
<h1 style="font-size: 4.5rem; color: var(--primary); font-family: 'Great Vibes', 'Brush Script MT', cursive, serif; margin: 0; line-height: 1.2; text-shadow: 2px 2px 4px rgba(212, 175, 55, 0.2);">
{groom['name']}
</h1>
<div style="font-size: 3.5rem; color: var(--primary-dark); font-family: 'Georgia', serif; font-style: italic; margin: 0.5rem 0;">
&
</div>
<h1 style="font-size: 4.5rem; color: var(--primary); font-family: 'Great Vibes', 'Brush Script MT', cursive, serif; margin: 0; line-height: 1.2; text-shadow: 2px 2px 4px rgba(212, 175, 55, 0.2);">
{bride['name']}
</h1>
<div style="margin-top: 2.5rem;">{ornament}</div>
</div>
""", unsafe_allow_html=True)
