"""
Hero Section - Nama mempelai utama
"""
import streamlit as st
from components.utils import create_ornament, create_divider

def render_hero(groom, bride):
    """Render hero section with bride and groom names"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 3rem 1rem;">
        {create_ornament()}
        
        <p class="subtitle" style="margin-top: 2rem;">THE WEDDING OF</p>
        
        <h1 class="title-cursive">{groom['name']}</h1>
        
        <div style="font-size: 3rem; color: #D4AF37; margin: 1rem 0;">
            &
        </div>
        
        <h1 class="title-cursive">{bride['name']}</h1>
        
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
