"""
Couple Section - Profil mempelai
"""
import streamlit as st
import os
from components.utils import create_ornament

def render_couple_section(groom, bride):
    """Render couple profile section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk judul section
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Mempelai</h2>
<div style="margin: 1rem 0;">{ornament}</div>
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
    photo_path = person.get('photo', '')
    if os.path.exists(photo_path):
        with open(photo_path, "rb") as f:
            import base64
            photo_base64 = base64.b64encode(f.read()).decode()
            # Memastikan foto berbentuk lingkaran sempurna dengan border emas
            photo_html = f'<img src="data:image/jpeg;base64,{photo_base64}" style="width: 200px; height: 200px; object-fit: cover; border-radius: 50%; border: 4px solid var(--primary); padding: 5px; margin: 1rem auto; display: block; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.2);">'
    else:
        # Placeholder if no photo - disesuaikan dengan warna emas
        photo_html = f'''
<div style="width: 200px; height: 200px; margin: 1rem auto; border-radius: 50%; background-color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 5rem; font-family: 'Georgia', serif; color: white; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.3); border: 4px solid white; outline: 2px solid var(--primary);">
{person['name'][0]}
</div>
'''
    
    instagram_html = ""
    if person.get('instagram'):
        instagram_html = f'''
<div style="margin-top: 1.5rem;">
<a href="https://instagram.com/{person['instagram'].replace('@', '')}" target="_blank" style="color: var(--primary-dark); text-decoration: none; font-weight: bold; background-color: white; padding: 0.5rem 1.2rem; border-radius: 20px; border: 1px solid var(--border-color); box-shadow: 0 2px 5px rgba(0,0,0,0.05); transition: all 0.3s ease;">
📷 {person['instagram']}
</a>
</div>
'''
    
    # Rata kiri untuk card utama dan menggunakan variabel CSS
    st.markdown(f"""
<div class="couple-card fade-in-up" style="background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 2.5rem 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); height: 100%;">
<p class="subtitle" style="margin-bottom: 1rem; color: var(--text-light); letter-spacing: 2px; text-transform: uppercase; font-size: 0.9rem;">{label}</p>
{photo_html}
<h3 class="title-cursive" style="font-size: 2.2rem; margin: 1.5rem 0 0.5rem 0; color: var(--primary); font-family: 'Georgia', serif;">
{person['name']}
</h3>
<p class="body-text" style="font-size: 1.1rem; font-weight: bold; margin: 0.5rem 0; color: var(--text-color);">
{person['full_name']}
</p>
<div style="margin: 1.5rem 0; padding: 1.2rem; background-color: rgba(212, 175, 55, 0.05); border: 1px dashed var(--primary); border-radius: 10px;">
<p class="body-text" style="font-size: 0.95rem; margin: 0.3rem 0; color: var(--text-light);">
{person['child_order']} dari
</p>
<p class="body-text" style="font-size: 1rem; margin: 0.3rem 0; color: var(--text-color);">
<strong>Bapak {person['father']}</strong>
</p>
<p class="body-text" style="font-size: 1rem; margin: 0.3rem 0; color: var(--text-color);">
& <strong>Ibu {person['mother']}</strong>
</p>
</div>
{instagram_html}
</div>
""", unsafe_allow_html=True)
