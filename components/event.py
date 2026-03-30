"""
Event Section - Akad & Resepsi
"""
import streamlit as st
from components.utils import create_ornament, format_date_indonesian, format_time

def render_event_section(akad, resepsi):
    """Render event details section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Waktu & Tempat</h2>
        {create_ornament()}
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
    
    st.markdown(f"""
    <div class="event-card fade-in-up">
        <div class="event-icon">{icon}</div>
        
        <h3 class="title-elegant" style="font-size: 1.8rem; margin: 1rem 0;">
            {title}
        </h3>
        
        <div style="margin: 1.5rem 0;">
            <p class="body-text" style="font-size: 1rem; margin: 0.5rem 0;">
                <strong>📅 {date_formatted}</strong>
            </p>
            
            <p class="body-text" style="font-size: 1rem; margin: 0.5rem 0;">
                <strong>🕐 {time_formatted} - {end_time_formatted}</strong>
            </p>
        </div>
        
        <div style="margin: 1.5rem 0; padding: 1rem; background: rgba(212, 175, 55, 0.1); border-radius: 10px;">
            <p class="body-text" style="font-weight: 600; margin: 0.5rem 0;">
                📍 {event['venue']}
            </p>
            <p class="body-text" style="font-size: 0.9rem; margin: 0.5rem 0; color: #7F8C8D;">
                {event['address']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add Google Maps button
    if event.get('maps_url'):
        st.markdown(f"""
        <div style="text-align: center; margin-top: 1rem;">
            <a href="{event['maps_url']}" target="_blank" 
               style="display: inline-block; background: linear-gradient(135deg, #D4AF37 0%, #8B7355 100%);
                      color: white; padding: 0.8rem 2rem; border-radius: 30px; text-decoration: none;
                      font-weight: 600; box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                      transition: transform 0.3s ease;">
                🗺️ Buka Google Maps
            </a>
        </div>
        """, unsafe_allow_html=True)
