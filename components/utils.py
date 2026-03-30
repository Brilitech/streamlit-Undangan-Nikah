"""
Utility functions untuk styling dan helpers
"""
import json
import os
from datetime import datetime

# CATATAN: 
# Fungsi get_theme_colors dan apply_custom_css sengaja dihapus
# karena seluruh pengaturan tema Putih-Emas yang baru 
# sudah kita tanamkan secara permanen di dalam file app.py.

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
    # BUG FIX: Ditulis rata kiri menjadi 1 baris saja tanpa indentasi
    # Menggunakan var(--primary) agar warnanya otomatis menjadi emas
    return '<div style="text-align: center; color: var(--primary); font-size: 2.2rem; margin: 1.5rem 0; text-shadow: 1px 1px 2px rgba(212,175,55,0.2);">❦ ◈ ❦</div>'

def create_divider():
    """Create decorative divider"""
    # BUG FIX: Sama seperti ornament, dijadikan 1 baris rata kiri.
    # Diberi efek gradasi elegan (transparan ke emas ke transparan)
    return '<div style="width: 150px; height: 2px; background: linear-gradient(90deg, transparent, var(--primary), transparent); margin: 2rem auto;"></div>'
