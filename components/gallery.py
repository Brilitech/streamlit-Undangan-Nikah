"""
Gallery Section - Foto prewedding
"""
import streamlit as st
import os
import base64
from components.utils import create_ornament

def render_gallery_section(gallery):
    """Render photo gallery section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Galeri Foto</h2>
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
    
    # Filter existing photos
    existing_photos = []
    for photo in gallery:
        if os.path.exists(photo['src']):
            existing_photos.append(photo)
    
    if not existing_photos:
        st.info("📸 Tambahkan foto prewedding di folder assets/gallery/")
        return
    
    # Display in grid - 3 columns
    cols_per_row = 3
    rows = [existing_photos[i:i + cols_per_row] for i in range(0, len(existing_photos), cols_per_row)]
    
    for row in rows:
        cols = st.columns(len(row))
        for idx, photo in enumerate(row):
            with cols[idx]:
                render_gallery_item(photo)

def render_gallery_item(photo):
    """Render individual gallery item"""
    
    try:
        with open(photo['src'], "rb") as f:
            photo_base64 = base64.b64encode(f.read()).decode()
            
        st.markdown(f"""
        <div class="gallery-item fade-in-up" style="margin-bottom: 1rem;">
            <img src="data:image/jpeg;base64,{photo_base64}" 
                 alt="{photo['alt']}"
                 style="width: 100%; height: 300px; object-fit: cover; border-radius: 15px; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); cursor: pointer;
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'">
        </div>
        """, unsafe_allow_html=True)
        
        # Also show with st.image for better viewing
        st.image(photo['src'], use_container_width=True)
        
    except Exception as e:
        st.warning(f"⚠️ Tidak dapat memuat foto: {photo['src']}")
