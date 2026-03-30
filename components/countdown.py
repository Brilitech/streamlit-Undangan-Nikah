"""
Countdown Section - Hitung mundur ke hari pernikahan
"""
import streamlit as st
from components.utils import create_ornament, calculate_countdown

def render_countdown_section(wedding_date):
    """Render countdown timer section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk menghindari bug markdown Code Block
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Menghitung Hari</h2>
<div style="margin: 1rem 0;">{ornament}</div>
</div>
""", unsafe_allow_html=True)
    
    # Create placeholder for countdown
    countdown_placeholder = st.empty()
    
    # Calculate countdown
    countdown = calculate_countdown(wedding_date)
    
    if countdown['passed']:
        countdown_placeholder.markdown("""
<div class="custom-card fade-in-up" style="text-align: center; padding: 3rem; background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
<h3 class="title-elegant" style="color: var(--primary); font-size: 2rem; margin-bottom: 1rem;">
🎉 Acara Telah Berlangsung 🎉
</h3>
<p class="body-text" style="margin-top: 1rem; color: var(--text-color); font-size: 1.1rem;">
Terima kasih atas doa dan kehadiran Anda
</p>
</div>
""", unsafe_allow_html=True)
    else:
        # Mengubah menjadi 3 kolom agar proporsional (Hari, Jam, Menit)
        col1, col2, col3 = st.columns(3)
        
        # Gaya seragam untuk setiap kotak countdown
        box_style = "background-color: var(--card-bg); border: 1px solid var(--primary); border-radius: 10px; padding: 1.5rem 1rem; text-align: center; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.1);"
        number_style = "font-size: 2.5rem; font-weight: bold; color: var(--primary); margin-bottom: 0.5rem;"
        label_style = "font-size: 1rem; color: var(--text-color); text-transform: uppercase; letter-spacing: 1px;"

        with col1:
            st.markdown(f"""
<div class="countdown-box fade-in-up" style="{box_style}">
<div class="countdown-number" style="{number_style}">{countdown['days']}</div>
<div class="countdown-label" style="{label_style}">Hari</div>
</div>
""", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
<div class="countdown-box fade-in-up" style="{box_style}">
<div class="countdown-number" style="{number_style}">{countdown['hours']}</div>
<div class="countdown-label" style="{label_style}">Jam</div>
</div>
""", unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
<div class="countdown-box fade-in-up" style="{box_style}">
<div class="countdown-number" style="{number_style}">{countdown['minutes']}</div>
<div class="countdown-label" style="{label_style}">Menit</div>
</div>
""", unsafe_allow_html=True)
        
        # Pesan keterangan yang lebih masuk akal karena detiknya hilang
        st.markdown("""
<p style="text-align: center; color: var(--text-light); font-size: 0.85rem; margin-top: 2rem; font-style: italic;">
* Waktu akan diperbarui setiap kali Anda memuat ulang halaman
</p>
""", unsafe_allow_html=True)
