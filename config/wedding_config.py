"""
🎉 KONFIGURASI UNDANGAN PERNIKAHAN
Pusat Data: Ubah semua informasi mempelai, acara, dan aset di file ini!
Catatan: Tema visual (Emas & Putih) sudah diatur secara permanen di app.py
"""

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
    "date": "2026-06-15",  # Format Wajib: YYYY-MM-DD
    "time": "08:00",
    "end_time": "09:30",
    "venue": "Masjid Agung Al-Azhar",
    "address": "Jl. Sisingamangaraja No. Kav. 2-4, Jakarta Selatan, DKI Jakarta 12110",
    "maps_url": "https://maps.google.com/?q=Masjid+Agung+Al-Azhar+Jakarta", # Ganti dengan Link Maps Asli
}

RESEPSI = {
    "date": "2026-06-15",
    "time": "11:00",
    "end_time": "14:00",
    "venue": "Grand Ballroom Hotel Mulia",
    "address": "Jl. Asia Afrika Senayan, Jakarta Pusat, DKI Jakarta 10270",
    "maps_url": "https://maps.google.com/?q=Hotel+Mulia+Senayan", # Ganti dengan Link Maps Asli
}

# ========== GALLERY ==========
# Taruh foto di folder assets/gallery/ (Bisa tambah atau kurangi baris sesuai jumlah foto)
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
        "label": "Kirim Kado / Hadiah Fisik",
        "address": "Jl. Mawar No. 10, Perumahan Griya Asri, Jakarta Selatan 12345",
        "phone": "0812-3456-7890",
    },
]

# ========== MUSIC ==========
# Pastikan file audio (flac/mp3/wav) ada di folder assets/music/
MUSIC = {
    "src": "assets/music/bg.flac", # Telah disesuaikan ke format .flac
    "title": "When I Need You - Celine Dion",
}

# ========== QUOTES ==========
QURAN_QUOTE = {
    "arabic": "وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً",
    "translation": "Dan di antara tanda-tanda (kebesaran)-Nya ialah Dia menciptakan pasangan-pasangan untukmu dari jenismu sendiri, agar kamu cenderung dan merasa tenteram kepadanya, dan Dia menjadikan di antaramu rasa kasih dan sayang.",
    "source": "QS. Ar-Rum: 21",
}

# ========== HASHTAG ==========
HASHTAG = "#WahyuHaliza2026"

# ========== FEATURE TOGGLES (PENGATURAN FITUR) ==========
# Ubah True menjadi False jika ada fitur/section yang ingin disembunyikan
FEATURES = {
    "music": True,          # Background music di sidebar
    "countdown": True,      # Countdown timer (Menghitung Hari)
    "rsvp": True,           # Form konfirmasi kehadiran (RSVP)
    "gifts": True,          # Amplop digital (Rekening/Alamat)
    "gallery": True,        # Galeri foto prewedding
    "guest_messages": True, # Buku tamu / Ucapan doa
    "social_share": True,   # Tombol bagikan ke WA/Sosmed
}

# ========== SEO & META ==========
# Muncul saat link undangan dibagikan ke WhatsApp atau Sosmed
META = {
    "title": f"Undangan Pernikahan {GROOM['name']} & {BRIDE['name']}",
    "description": f"Merupakan suatu kehormatan bagi kami mengundang Bapak/Ibu untuk hadir di hari bahagia {GROOM['name']} dan {BRIDE['name']}.",
    "image": "assets/images/cover.jpg",
}
