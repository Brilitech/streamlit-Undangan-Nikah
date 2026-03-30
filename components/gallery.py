"""
Gallery Section - Foto prewedding
"""
import streamlit as st
import os
import base64
from components.utils import create_ornament

def render_gallery_section(gallery):
    """Render photo gallery section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk judul section agar terhindar dari bug markdown
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Galeri Foto</h2>
<div style="margin: 1rem 0;">{ornament}</div>
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
            
        # Rata kiri untuk HTML dan penambahan efek bayangan emas
        st.markdown(f"""
<div class="gallery-item fade-in-up" style="margin-bottom: 1.5rem;">
<img src="data:image/jpeg;base64,{photo_base64}" alt="{photo.get('alt', 'Foto Galeri')}" style="width: 100%; height: 300px; object-fit: cover; border-radius: 15px; border: 1px solid var(--border-color); box-shadow: 0 8px 15px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.4s ease;" onmouseover="this.style.transform='scale(1.03)'; this.style.boxShadow='0 12px 25px rgba(212, 175, 55, 0.3)'; this.style.borderColor='var(--primary)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 8px 15px rgba(0,0,0,0.05)'; this.style.borderColor='var(--border-color)';">
</div>
""", unsafe_allow_html=True)
        
        # CATATAN: st.image() dinonaktifkan agar foto tidak tercetak dua kali (ganda) 
        # karena kita sudah merendernya dengan cantik menggunakan HTML di atas.
        # st.image(photo['src'], use_container_width=True)
        
    except Exception as e:
        st.warning(f"⚠️ Tidak dapat memuat foto: {photo['src']}")
