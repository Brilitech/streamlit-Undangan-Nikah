"""
Countdown Section - Hitung mundur ke hari pernikahan
"""
import streamlit as st
from components.utils import create_ornament, calculate_countdown
import time

def render_countdown_section(wedding_date):
    """Render countdown timer section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Menghitung Hari</h2>
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
    
    # Create placeholder for countdown
    countdown_placeholder = st.empty()
    
    # Calculate countdown
    countdown = calculate_countdown(wedding_date)
    
    if countdown['passed']:
        countdown_placeholder.markdown("""
        <div class="custom-card" style="text-align: center; padding: 3rem;">
            <h3 class="title-elegant" style="color: #D4AF37;">
                🎉 Acara Telah Berlangsung 🎉
            </h3>
            <p class="body-text" style="margin-top: 1rem;">
                Terima kasih atas doa dan kehadiran Anda
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Display countdown
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="countdown-box fade-in-up">
                <div class="countdown-number">{countdown['days']}</div>
                <div class="countdown-label">Hari</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="countdown-box fade-in-up">
                <div class="countdown-number">{countdown['hours']}</div>
                <div class="countdown-label">Jam</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="countdown-box fade-in-up">
                <div class="countdown-number">{countdown['minutes']}</div>
                <div class="countdown-label">Menit</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="countdown-box fade-in-up">
                <div class="countdown-number">{countdown['seconds']}</div>
                <div class="countdown-label">Detik</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Add auto-refresh note
        st.markdown("""
        <p style="text-align: center; color: #7F8C8D; font-size: 0.85rem; margin-top: 1rem;">
            ⏰ Reload halaman untuk update waktu
        </p>
        """, unsafe_allow_html=True)
