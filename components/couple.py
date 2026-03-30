"""
Couple Section - Profil mempelai
"""
import streamlit as st
import os
from components.utils import create_ornament

def render_couple_section(groom, bride):
    """Render couple profile section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Mempelai</h2>
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for groom and bride
    col1, col2 = st.columns(2)
    
    with col1:
        render_person_card(groom, "Mempelai Pria")
    
    with col2:
        render_person_card(bride, "Mempelai Wanita")

def render_person_card(person, label):
    """Render individual person card"""
    
    # Check if photo exists
    photo_path = person['photo']
    if os.path.exists(photo_path):
        with open(photo_path, "rb") as f:
            import base64
            photo_base64 = base64.b64encode(f.read()).decode()
            photo_html = f'<img src="data:image/jpeg;base64,{photo_base64}" class="profile-image">'
    else:
        # Placeholder if no photo
        photo_html = f'''
        <div style="width: 200px; height: 200px; margin: 1rem auto; border-radius: 50%; 
                    background: linear-gradient(135deg, #D4AF37 0%, #8B7355 100%);
                    display: flex; align-items: center; justify-content: center;
                    font-size: 4rem; color: white; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
            {person['name'][0]}
        </div>
        '''
    
    instagram_html = ""
    if person.get('instagram'):
        instagram_html = f'''
        <p style="margin-top: 1rem;">
            <a href="https://instagram.com/{person['instagram'].replace('@', '')}" 
               target="_blank"
               style="color: #D4AF37; text-decoration: none; font-weight: 500;">
                <span style="font-size: 1.2rem;">📷</span> {person['instagram']}
            </a>
        </p>
        '''
    
    st.markdown(f"""
    <div class="couple-card fade-in-up">
        <p class="subtitle" style="margin-bottom: 1rem;">{label}</p>
        
        {photo_html}
        
        <h3 class="title-cursive" style="font-size: 2rem; margin: 1rem 0;">
            {person['name']}
        </h3>
        
        <p class="body-text" style="font-size: 0.95rem; font-weight: 600; margin: 0.5rem 0;">
            {person['full_name']}
        </p>
        
        <div style="margin: 1.5rem 0; padding: 1rem; background: rgba(212, 175, 55, 0.1); border-radius: 10px;">
            <p class="body-text" style="font-size: 0.9rem; margin: 0.3rem 0;">
                {person['child_order']} dari
            </p>
            <p class="body-text" style="font-size: 0.9rem; margin: 0.3rem 0;">
                <strong>{person['father']}</strong>
            </p>
            <p class="body-text" style="font-size: 0.9rem; margin: 0.3rem 0;">
                & <strong>{person['mother']}</strong>
            </p>
        </div>
        
        {instagram_html}
    </div>
    """, unsafe_allow_html=True)
