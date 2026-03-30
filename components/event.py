"""
Event Section - Akad & Resepsi
"""
import streamlit as st
from components.utils import create_ornament, format_date_indonesian, format_time

def render_event_section(akad, resepsi):
    """Render event details section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk menghindari bug Code Block Streamlit
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Waktu & Tempat</h2>
<div style="margin: 1rem 0;">{ornament}</div>
</div>
""", unsafe_allow_html=True)
    
    # Create two columns for akad and resepsi
    col1, col2 = st.columns(2)
    
    with col1:
        render_event_card(akad, "Akad Nikah", "🕌")
    
    with col2:
        render_event_card(resepsi, "Resepsi", "🎉")

def render_event_card(event, title, icon):
    """Render individual event card"""
    
    date_formatted = format_date_indonesian(event['date'])
    time_formatted = format_time(event['time'])
    end_time_formatted = format_time(event['end_time'])
    
    # Rata kiri untuk menghindari bug Code Block Streamlit
    # Menyesuaikan warna dengan tema CSS Putih & Emas
    st.markdown(f"""
<div class="event-card fade-in-up" style="background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); height: 100%;">
<div class="event-icon" style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
<h3 class="title-elegant" style="font-size: 1.8rem; margin: 1rem 0; color: var(--primary);">
{title}
</h3>
<div style="margin: 1.5rem 0;">
<p class="body-text" style="font-size: 1rem; margin: 0.5rem 0; color: var(--text-color);">
<strong>📅 {date_formatted}</strong>
</p>
<p class="body-text" style="font-size: 1rem; margin: 0.5rem 0; color: var(--text-color);">
<strong>🕐 {time_formatted} - {end_time_formatted}</strong>
</p>
</div>
<div style="margin: 1.5rem 0; padding: 1rem; background: rgba(212, 175, 55, 0.08); border-radius: 10px; border: 1px dashed var(--primary);">
<p class="body-text" style="font-weight: 600; margin: 0.5rem 0; color: var(--primary-dark);">
📍 {event['venue']}
</p>
<p class="body-text" style="font-size: 0.9rem; margin: 0.5rem 0; color: var(--text-light);">
{event['address']}
</p>
</div>
</div>
""", unsafe_allow_html=True)
    
    # Add Google Maps button (Juga diratakan kiri)
    if event.get('maps_url'):
        st.markdown(f"""
<div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
<a href="{event['maps_url']}" target="_blank" style="display: inline-block; background-color: var(--primary); color: white; padding: 0.8rem 2rem; border-radius: 30px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.3); transition: transform 0.2s ease;">
🗺️ Buka Google Maps
</a>
</div>
""", unsafe_allow_html=True)
