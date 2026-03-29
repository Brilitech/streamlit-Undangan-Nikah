# 💌 Undangan Nikah Digital - Streamlit Version

Template undangan pernikahan digital yang elegan, customizable, dan modern untuk deployment di Streamlit Cloud.

**Original Template:** [gorillaworkout/undangan-nikah](https://github.com/gorillaworkout/undangan-nikah) (Next.js)  
**Ported to:** Streamlit + Python

---

## ✨ Fitur

- 🎭 **Cover dengan nama tamu** — Personalisasi via URL `?to=Nama`
- 🕌 **Nuansa Islami** — Bismillah, ayat Al-Quran, salam
- 👫 **Profil mempelai** — Foto, nama orang tua, Instagram
- 📅 **Akad & Resepsi** — Tanggal, waktu, lokasi + Google Maps
- ⏰ **Countdown live** — Hitung mundur ke hari H
- 🖼️ **Gallery** — Grid foto prewedding
- 💳 **Amplop digital** — Rekening bank + alamat kirim hadiah
- 📝 **RSVP** — Form konfirmasi kehadiran + ucapan doa
- 🎵 **Background music** — Audio player di sidebar
- 🎨 **5 Theme presets** — Gold, Rose, Navy, Forest, Lavender
- ⚡ **Feature toggles** — On/off setiap section
- 📱 **100% Responsive** — Mobile-first design

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/your-username/undangan-streamlit.git
cd undangan-streamlit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Customize Data

Edit **`config/wedding_config.py`** — semua customization ada di sini!

### 4. Tambahkan Foto

Taruh foto di folder:
- `assets/images/groom.jpg` — Foto mempelai pria
- `assets/images/bride.jpg` — Foto mempelai wanita
- `assets/gallery/1.jpg, 2.jpg, ...` — Foto prewedding
- `assets/music/background.mp3` — Background music

### 5. Run Locally

```bash
streamlit run app.py
```

Buka: `http://localhost:8501?to=Nama%20Tamu`

---

## 📝 Cara Customize

### 1. Pilih Theme Warna

Edit `config/wedding_config.py`:

```python
THEME = "gold"  # Pilihan: "gold", "rose", "navy", "forest", "lavender"
```

#### 🎨 Theme Presets:

| Preset | Warna | Vibe |
|--------|-------|------|
| `gold` | ✨ Gold + Sage | Mewah, elegan, timeless |
| `rose` | 🌹 Rose Pink | Romantis, soft, feminine |
| `navy` | 🌊 Navy + Gold | Maskulin, bold, modern |
| `forest` | 🌿 Green + Brown | Natural, earthy, rustic |
| `lavender` | 💜 Purple | Dreamy, soft, whimsical |

#### Custom Theme:

```python
THEME = None  # Set None untuk pakai custom
CUSTOM_THEME = {
    "primary": "#E91E63",
    "primary_light": "#F48FB1",
    "primary_dark": "#AD1457",
    # ... dst
}
```

### 2. Data Mempelai

```python
GROOM = {
    "name": "Ahmad Wahyu",
    "full_name": "Ahmad Wahyu Pratama, S.Kom",
    "father": "Bapak Surya Pratama",
    "mother": "Ibu Dewi Lestari",
    "child_order": "Putra pertama",
    "photo": "assets/images/groom.jpg",
    "instagram": "@wahyupratama",
}
```

### 3. Tanggal & Tempat

```python
AKAD = {
    "date": "2026-06-15",  # Format: YYYY-MM-DD
    "time": "08:00",
    "end_time": "09:30",
    "venue": "Masjid Agung Al-Azhar",
    "address": "Jl. Sisingamangaraja...",
    "maps_url": "https://maps.google.com/?q=...",
}
```

### 4. Gallery

```python
GALLERY = [
    {"src": "assets/gallery/1.jpg", "alt": "Prewedding 1"},
    {"src": "assets/gallery/2.jpg", "alt": "Prewedding 2"},
    # Tambah/kurangi sesuka hati
]
```

### 5. Amplop Digital

```python
GIFTS = [
    {
        "type": "bank",
        "bank_name": "Bank Central Asia (BCA)",
        "account_number": "1234567890",
        "account_holder": "Ahmad Wahyu Pratama",
    },
    {
        "type": "address",
        "label": "Kirim Hadiah",
        "address": "Jl. Mawar No. 10...",
        "phone": "0812-3456-7890",
    },
]
```

### 6. Toggle Fitur

```python
FEATURES = {
    "music": True,           # Background music
    "countdown": True,       # Countdown timer
    "rsvp": True,           # RSVP form
    "gifts": True,          # Amplop digital
    "gallery": True,        # Photo gallery
    "guest_messages": True, # Ucapan tamu
    "social_share": True,   # Share button
}
```

---

## 🚀 Deploy ke Streamlit Cloud

### Step 1: Push ke GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/undangan-streamlit.git
git push -u origin main
```

### Step 2: Deploy di Streamlit Cloud

1. Buka [share.streamlit.io](https://share.streamlit.io)
2. Login dengan GitHub
3. Klik **"New app"**
4. Pilih repository: `your-username/undangan-streamlit`
5. Main file: `app.py`
6. Klik **"Deploy"**

### Step 3: Custom Domain (Optional)

Di Streamlit Cloud settings, tambahkan custom domain Anda.

---

## 🗄️ Database RSVP

RSVP otomatis tersimpan di `data/rsvp.json` (file-based).

### Lihat Data RSVP:

```bash
cat data/rsvp.json
```

### Format Data:

```json
[
  {
    "name": "John Doe",
    "attendance": "hadir",
    "guests": 2,
    "message": "Selamat menikah!",
    "timestamp": "2026-05-20 14:30:00"
  }
]
```

### Upgrade ke Database (Optional)

Untuk undangan besar (>500 tamu), gunakan:
- **Supabase** (gratis, cloud)
- **PostgreSQL** (self-hosted)
- **Google Sheets API** (simple)

Edit `components/rsvp.py` untuk integrasi database.

---

## 🔗 Cara Kirim Undangan

Tambahkan `?to=` di URL untuk personalisasi:

```
https://your-app.streamlit.app/?to=Bapak%20Hasan
https://your-app.streamlit.app/?to=Keluarga%20Pratama
https://your-app.streamlit.app/?to=Teman%20Kantor
```

**Cara encode nama:**
- Spasi → `%20`
- Use online URL encoder: [urlencoder.org](https://www.urlencoder.org/)

---

## 📂 Struktur Project

```
undangan-streamlit/
├── app.py                      # Main application
├── requirements.txt            # Dependencies
├── .streamlit/
│   └── config.toml            # Streamlit config
├── config/
│   └── wedding_config.py      # ⭐ ALL CUSTOMIZATION HERE
├── components/
│   ├── utils.py               # Helper functions
│   ├── cover.py               # Cover section
│   ├── hero.py                # Hero section
│   ├── quote.py               # Quote section
│   ├── couple.py              # Couple profile
│   ├── event.py               # Event details
│   ├── countdown.py           # Countdown timer
│   ├── gallery.py             # Photo gallery
│   ├── gift.py                # Digital envelope
│   ├── rsvp.py                # RSVP form
│   └── footer.py              # Footer
├── assets/
│   ├── images/
│   │   ├── groom.jpg
│   │   └── bride.jpg
│   ├── gallery/
│   │   └── 1.jpg, 2.jpg, ...
│   └── music/
│       └── background.mp3
├── data/
│   └── rsvp.json              # RSVP data (auto-created)
└── README.md
```

---

## 🎨 Customization Tips

### Ganti Font

Edit `components/utils.py`:

```css
@import url('https://fonts.googleapis.com/css2?family=Your+Font&display=swap');

.title-cursive {
    font-family: 'Your Font', cursive;
}
```

### Tambah Section Baru

1. Buat file di `components/your_section.py`
2. Import di `app.py`
3. Render dengan `render_your_section()`

### Ganti Icon/Emoji

Cari emoji di: [emojipedia.org](https://emojipedia.org/)

---

## 🆚 Perbedaan dengan Next.js Version

| Fitur | Next.js | Streamlit |
|-------|---------|-----------|
| 3D Elements | ✅ Three.js | ❌ (Streamlit limitasi) |
| Particles | ✅ Framer Motion | ⚠️ CSS only (simplified) |
| Music Auto-play | ✅ | ⚠️ Sidebar only (browser policy) |
| RSVP API | ✅ Route API | ✅ File-based / extendable |
| Deploy | Vercel/VPS | Streamlit Cloud (gratis) |
| Setup | npm, build | pip, run (lebih simple) |

---

## ⚡ Performance Tips

### 1. Optimize Images

```bash
# Install imagemagick
brew install imagemagick  # macOS
apt install imagemagick   # Linux

# Resize images
mogrify -resize 1200x1200 -quality 85 assets/gallery/*.jpg
```

### 2. Lazy Loading

Streamlit auto lazy-load images. Tidak perlu config.

### 3. Caching

Tambah `@st.cache_data` di functions yang sering dipanggil.

---

## 🐛 Troubleshooting

### Problem: Foto tidak muncul

**Solusi:**
- Pastikan path benar: `assets/images/groom.jpg`
- Cek file exists: `ls assets/images/`
- Gunakan format: `.jpg`, `.jpeg`, atau `.png`

### Problem: Music tidak auto-play

**Solusi:**
- Browser policy: auto-play audio blocked by default
- Music akan muncul di sidebar
- User harus klik play manual

### Problem: RSVP tidak tersimpan

**Solusi:**
- Folder `data/` harus writable
- Check: `chmod 777 data/`
- Di Streamlit Cloud, data tidak persisten (gunakan database)

### Problem: Deployment gagal

**Solusi:**
- Check `requirements.txt` valid
- Pastikan semua files pushed ke GitHub
- Lihat logs di Streamlit Cloud dashboard

---

## 📱 Testing

### Test Responsive

```bash
# Desktop
streamlit run app.py

# Mobile simulation (Chrome DevTools)
# F12 → Toggle device toolbar → Pilih device
```

### Test Personalisasi

```bash
# Test dengan nama berbeda
http://localhost:8501?to=Test%20User
http://localhost:8501?to=Bapak%20Ahmad
```

---

## 🔄 Update dari Next.js Original

Untuk sync dengan template asli:

```bash
# Add upstream remote
git remote add upstream https://github.com/gorillaworkout/undangan-nikah.git

# Fetch updates
git fetch upstream

# Manual merge (karena beda stack)
# Review changes dan adapt ke Streamlit version
```

---

## 🤝 Contributing

Pull requests welcome! Untuk perubahan besar:
1. Fork repository
2. Buat branch: `git checkout -b feature/amazing-feature`
3. Commit: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open Pull Request

---

## 📄 License

MIT License — free untuk dipakai, dimodifikasi, dan didistribusikan.

---

## 🙏 Credits

- **Original Template:** [gorillaworkout/undangan-nikah](https://github.com/gorillaworkout/undangan-nikah)
- **Ported to Streamlit by:** [Your Name]
- **Fonts:** Google Fonts (Great Vibes, Playfair Display, Poppins)
- **Icons:** Emoji Unicode

---

## 💡 FAQ

**Q: Apakah gratis?**  
A: Ya! Template gratis, Streamlit Cloud gratis (tier public), hosting gratis.

**Q: Bisa pakai custom domain?**  
A: Ya, Streamlit Cloud support custom domain (CNAME).

**Q: Data RSVP aman?**  
A: File-based RSVP di Streamlit Cloud tidak persisten. Untuk production, gunakan database eksternal (Supabase/PostgreSQL).

**Q: Bisa tambah fitur X?**  
A: Ya! Buat component baru di `components/`, lalu render di `app.py`.

**Q: Support multi-language?**  
A: Belum built-in. Tambahkan di `config/wedding_config.py` untuk i18n support.

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/your-username/undangan-streamlit/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-username/undangan-streamlit/discussions)
- **Email:** your-email@example.com

---

Made with ❤️ for your special day 💒
