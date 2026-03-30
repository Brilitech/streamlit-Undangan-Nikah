"""
🎉 KONFIGURASI UNDANGAN PERNIKAHAN
Customize semua data di file ini saja!
"""

# ========== THEME & COLORS ==========
# Pilihan: "gold", "rose", "navy", "forest", "lavender", "monochrome", "rustic", "blush"
THEME = "gold"

# Custom theme (jika THEME = None)
CUSTOM_THEME = {
    "primary": "#D4AF37",
    "primary_light": "#F4E4C1",
    "primary_dark": "#8B7355",
    "secondary": "#5F7161",
    "background": "#FFFFFF",
    "background_alt": "#F8F6F0",
    "text": "#2C3E50",
    "text_light": "#7F8C8D",
}

# Theme Presets
THEMES = {
    "gold": {
        "primary": "#D4AF37",
        "primary_light": "#F4E4C1",
        "primary_dark": "#8B7355",
        "secondary": "#5F7161",
        "background": "#FFFFFF",
        "background_alt": "#F8F6F0",
        "text": "#2C3E50",
        "text_light": "#7F8C8D",
    },
    "rose": {
        "primary": "#E8B4B8",
        "primary_light": "#F5D6D8",
        "primary_dark": "#C97C81",
        "secondary": "#A8DADC",
        "background": "#FFFFFF",
        "background_alt": "#FFF5F7",
        "text": "#2C3E50",
        "text_light": "#7F8C8D",
    },
    "navy": {
        "primary": "#2C3E50",
        "primary_light": "#5D6D7E",
        "primary_dark": "#1C2833",
        "secondary": "#D4AF37",
        "background": "#FFFFFF",
        "background_alt": "#F4F6F7",
        "text": "#2C3E50",
        "text_light": "#7F8C8D",
    },
    "forest": {
        "primary": "#4A7C59",
        "primary_light": "#86A789",
        "primary_dark": "#2F5233",
        "secondary": "#8B7355",
        "background": "#FFFFFF",
        "background_alt": "#F4F1E8",
        "text": "#2C3E50",
        "text_light": "#7F8C8D",
    },
    "lavender": {
        "primary": "#B4A7D6",
        "primary_light": "#D4C5F9",
        "primary_dark": "#8B7BB8",
        "secondary": "#F4D9D0",
        "background": "#FFFFFF",
        "background_alt": "#F9F7FF",
        "text": "#2C3E50",
        "text_light": "#7F8C8D",
    },
}

# ========== DATA MEMPELAI ==========
GROOM = {
    "name": "Ahmad Wahyu",
    "full_name": "Ahmad Wahyu Pratama, S.Kom",
    "father": "Bapak Surya Pratama",
    "mother": "Ibu Dewi Lestari",
    "child_order": "Putra pertama",
    "photo": "assets/images/groom.jpg",
    "instagram": "@wahyupratama",
}

BRIDE = {
    "name": "Siti Nurhaliza",
    "full_name": "Siti Nurhaliza Rahmawati, S.Pd",
    "father": "Bapak Budi Rahmawan",
    "mother": "Ibu Asri Wulandari",
    "child_order": "Putri kedua",
    "photo": "assets/images/bride.jpg",
    "instagram": "@sitihaliza",
}

# ========== EVENT DETAILS ==========
AKAD = {
    "date": "2026-06-15",  # Format: YYYY-MM-DD
    "time": "08:00",
    "end_time": "09:30",
    "venue": "Masjid Agung Al-Azhar",
    "address": "Jl. Sisingamangaraja No. Kav. 2-4, Jakarta Selatan, DKI Jakarta 12110",
    "maps_url": "https://maps.google.com/?q=Masjid+Agung+Al-Azhar+Jakarta",
}

RESEPSI = {
    "date": "2026-06-15",
    "time": "11:00",
    "end_time": "14:00",
    "venue": "Grand Ballroom Hotel Mulia",
    "address": "Jl. Asia Afrika Senayan, Jakarta Pusat, DKI Jakarta 10270",
    "maps_url": "https://maps.google.com/?q=Hotel+Mulia+Jakarta",
}

# ========== GALLERY ==========
# Taruh foto di folder assets/gallery/
GALLERY = [
    {"src": "assets/gallery/1.jpg", "alt": "Prewedding 1"},
    {"src": "assets/gallery/2.jpg", "alt": "Prewedding 2"},
    {"src": "assets/gallery/3.jpg", "alt": "Prewedding 3"},
    {"src": "assets/gallery/4.jpg", "alt": "Prewedding 4"},
    {"src": "assets/gallery/5.jpg", "alt": "Prewedding 5"},
    {"src": "assets/gallery/6.jpg", "alt": "Prewedding 6"},
]

# ========== GIFT / AMPLOP DIGITAL ==========
GIFTS = [
    {
        "type": "bank",
        "bank_name": "Bank Central Asia (BCA)",
        "account_number": "1234567890",
        "account_holder": "Ahmad Wahyu Pratama",
    },
    {
        "type": "bank",
        "bank_name": "Bank Mandiri",
        "account_number": "0987654321",
        "account_holder": "Siti Nurhaliza Rahmawati",
    },
    {
        "type": "address",
        "label": "Kirim Hadiah",
        "address": "Jl. Mawar No. 10, Perumahan Griya Asri, Jakarta Selatan 12345",
        "phone": "0812-3456-7890",
    },
]

# ========== MUSIC ==========
MUSIC = {
    "src": "assets/music/background.mp3",
    "title": "Beautiful In White - Shane Filan",
}

# ========== QUOTES ==========
QURAN_QUOTE = {
    "arabic": "وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً",
    "translation": "Dan di antara tanda-tanda (kebesaran)-Nya ialah Dia menciptakan pasangan-pasangan untukmu dari jenismu sendiri, agar kamu cenderung dan merasa tenteram kepadanya, dan Dia menjadikan di antaramu rasa kasih dan sayang.",
    "source": "QS. Ar-Rum: 21",
}

# ========== HASHTAG ==========
HASHTAG = "#WahyuHaliza2026"

# ========== FEATURE TOGGLES ==========
FEATURES = {
    "music": True,           # Background music
    "countdown": True,       # Countdown timer
    "rsvp": True,           # RSVP form
    "gifts": True,          # Amplop digital
    "gallery": True,        # Photo gallery
    "guest_messages": True, # Ucapan tamu
    "social_share": True,   # Share ke sosmed
}

# ========== SEO & META ==========
META = {
    "title": f"Undangan Pernikahan {GROOM['name']} & {BRIDE['name']}",
    "description": f"Undangan pernikahan {GROOM['full_name']} dan {BRIDE['full_name']}",
    "image": "assets/images/cover.jpg",
}
