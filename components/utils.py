"""
Utility functions untuk styling dan helpers
"""
import streamlit as st
from datetime import datetime
import json
import os

def get_theme_colors(theme_name, custom_theme=None):
    """Get theme colors"""
    from config.wedding_config import THEMES
    
    if theme_name and theme_name in THEMES:
        return THEMES[theme_name]
    elif custom_theme:
        return custom_theme
    else:
        return THEMES["gold"]

def apply_custom_css(theme):
    """Apply custom CSS with theme colors"""
    css = f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&family=Poppins:wght@300;400;600&display=swap');
    
    /* Global Styles */
    .main {{
        background: linear-gradient(180deg, {theme['background']} 0%, {theme['background_alt']} 100%);
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Typography */
    .title-cursive {{
        font-family: 'Great Vibes', cursive;
        color: {theme['primary']};
        font-size: 4rem;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}
    
    .title-elegant {{
        font-family: 'Playfair Display', serif;
        color: {theme['text']};
        font-size: 2.5rem;
        text-align: center;
        margin: 1.5rem 0;
        font-weight: 700;
    }}
    
    .subtitle {{
        font-family: 'Poppins', sans-serif;
        color: {theme['text_light']};
        font-size: 1rem;
        text-align: center;
        margin: 0.5rem 0;
        font-weight: 300;
        letter-spacing: 2px;
    }}
    
    .body-text {{
        font-family: 'Poppins', sans-serif;
        color: {theme['text']};
        line-height: 1.8;
        text-align: center;
    }}
    
    /* Bismillah */
    .bismillah {{
        font-family: 'Traditional Arabic', serif;
        font-size: 2.5rem;
        text-align: center;
        color: {theme['primary']};
        margin: 2rem 0;
        direction: rtl;
    }}
    
    /* Arabic Quote */
    .arabic-text {{
        font-family: 'Traditional Arabic', serif;
        font-size: 1.8rem;
        text-align: center;
        color: {theme['primary_dark']};
        margin: 2rem 0;
        direction: rtl;
        line-height: 2;
    }}
    
    /* Card Styles */
    .custom-card {{
        background: {theme['background']};
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1.5rem 0;
        border: 1px solid {theme['primary_light']};
    }}
    
    .couple-card {{
        background: linear-gradient(135deg, {theme['background']} 0%, {theme['background_alt']} 100%);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 2px solid {theme['primary_light']};
        transition: transform 0.3s ease;
    }}
    
    .couple-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }}
    
    /* Profile Image */
    .profile-image {{
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid {theme['primary']};
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 1rem auto;
        display: block;
    }}
    
    /* Countdown */
    .countdown-box {{
        background: linear-gradient(135deg, {theme['primary']} 0%, {theme['primary_dark']} 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin: 0.5rem;
    }}
    
    .countdown-number {{
        font-size: 3rem;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
    }}
    
    .countdown-label {{
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.5rem;
    }}
    
    /* Buttons */
    .stButton > button {{
        background: linear-gradient(135deg, {theme['primary']} 0%, {theme['primary_dark']} 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.8rem 2.5rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }}
    
    /* Event Cards */
    .event-card {{
        background: {theme['background']};
        border-left: 4px solid {theme['primary']};
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }}
    
    .event-icon {{
        font-size: 3rem;
        color: {theme['primary']};
        margin-bottom: 1rem;
    }}
    
    /* Gift Card */
    .gift-card {{
        background: linear-gradient(135deg, {theme['background']} 0%, {theme['background_alt']} 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px solid {theme['primary_light']};
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}
    
    .account-number {{
        background: {theme['primary_light']};
        color: {theme['primary_dark']};
        padding: 1rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 1.3rem;
        font-weight: 700;
        text-align: center;
        margin: 1rem 0;
        letter-spacing: 2px;
    }}
    
    /* Gallery */
    .gallery-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }}
    
    .gallery-item {{
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }}
    
    .gallery-item:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }}
    
    .gallery-item img {{
        width: 100%;
        height: 300px;
        object-fit: cover;
    }}
    
    /* Divider */
    .divider {{
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, transparent, {theme['primary']}, transparent);
        margin: 2rem auto;
    }}
    
    .ornament {{
        text-align: center;
        color: {theme['primary']};
        font-size: 2rem;
        margin: 1.5rem 0;
    }}
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {{
        border: 2px solid {theme['primary_light']};
        border-radius: 10px;
        padding: 0.8rem;
        font-family: 'Poppins', sans-serif;
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {{
        border-color: {theme['primary']};
        box-shadow: 0 0 0 3px {theme['primary_light']};
    }}
    
    /* Messages */
    .message-card {{
        background: {theme['background_alt']};
        border-left: 4px solid {theme['primary']};
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }}
    
    .message-name {{
        font-weight: 600;
        color: {theme['primary_dark']};
        margin-bottom: 0.5rem;
    }}
    
    .message-text {{
        color: {theme['text']};
        line-height: 1.6;
    }}
    
    .message-date {{
        font-size: 0.8rem;
        color: {theme['text_light']};
        margin-top: 0.5rem;
    }}
    
    /* Social Icons */
    .social-icon {{
        display: inline-block;
        width: 40px;
        height: 40px;
        line-height: 40px;
        text-align: center;
        background: {theme['primary']};
        color: white;
        border-radius: 50%;
        margin: 0.5rem;
        transition: transform 0.3s ease;
    }}
    
    .social-icon:hover {{
        transform: translateY(-5px);
        background: {theme['primary_dark']};
    }}
    
    /* Footer */
    .footer {{
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        color: {theme['text_light']};
        font-family: 'Poppins', sans-serif;
    }}
    
    .hashtag {{
        font-size: 1.5rem;
        color: {theme['primary']};
        font-weight: 600;
        margin: 1rem 0;
    }}
    
    /* Animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .fade-in-up {{
        animation: fadeInUp 0.8s ease-out;
    }}
    
    /* Responsive */
    @media (max-width: 768px) {{
        .title-cursive {{
            font-size: 2.5rem;
        }}
        
        .title-elegant {{
            font-size: 1.8rem;
        }}
        
        .countdown-number {{
            font-size: 2rem;
        }}
        
        .profile-image {{
            width: 150px;
            height: 150px;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def calculate_countdown(target_date):
    """Calculate countdown to wedding date"""
    try:
        target = datetime.strptime(target_date, "%Y-%m-%d")
        now = datetime.now()
        diff = target - now
        
        if diff.total_seconds() <= 0:
            return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0, "passed": True}
        
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60
        
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "passed": False
        }
    except:
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0, "passed": False}

def save_rsvp(data):
    """Save RSVP data to JSON file"""
    rsvp_file = "data/rsvp.json"
    
    # Create data directory if not exists
    os.makedirs("data", exist_ok=True)
    
    # Load existing data
    if os.path.exists(rsvp_file):
        try:
            with open(rsvp_file, "r", encoding="utf-8") as f:
                rsvp_data = json.load(f)
        except:
            rsvp_data = []
    else:
        rsvp_data = []
    
    # Add timestamp
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append new data
    rsvp_data.append(data)
    
    # Save
    with open(rsvp_file, "w", encoding="utf-8") as f:
        json.dump(rsvp_data, f, indent=2, ensure_ascii=False)
    
    return True

def load_rsvp():
    """Load all RSVP data"""
    rsvp_file = "data/rsvp.json"
    
    if os.path.exists(rsvp_file):
        try:
            with open(rsvp_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def format_date_indonesian(date_string):
    """Format date to Indonesian format"""
    months = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    
    days = {
        0: "Senin", 1: "Selasa", 2: "Rabu", 3: "Kamis",
        4: "Jumat", 5: "Sabtu", 6: "Minggu"
    }
    
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
        day_name = days[date.weekday()]
        return f"{day_name}, {date.day} {months[date.month]} {date.year}"
    except:
        return date_string

def format_time(time_string):
    """Format time from HH:MM to readable format"""
    try:
        time = datetime.strptime(time_string, "%H:%M")
        return time.strftime("%H:%M WIB")
    except:
        return time_string

def create_ornament():
    """Create decorative ornament"""
    return """
    <div class="ornament">
        ❦ ◈ ❦
    </div>
    """

def create_divider():
    """Create decorative divider"""
    return '<div class="divider"></div>'
