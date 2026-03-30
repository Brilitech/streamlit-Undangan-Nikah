# Assets Folder

Taruh file-file media di sini:

## 📁 Struktur

```
assets/
├── images/
│   ├── groom.jpg       # Foto mempelai pria (recommended: 800x800px)
│   ├── bride.jpg       # Foto mempelai wanita (recommended: 800x800px)
│   └── cover.jpg       # Optional: Cover image
├── gallery/
│   ├── 1.jpg           # Foto prewedding 1
│   ├── 2.jpg           # Foto prewedding 2
│   ├── 3.jpg           # Foto prewedding 3
│   ├── 4.jpg           # ... dst
│   └── ...
└── music/
    └── background.mp3  # Background music (optional)
```

## 📸 Image Guidelines

### Profile Photos (groom.jpg, bride.jpg)
- **Ukuran:** 800x800px (square/portrait)
- **Format:** JPG atau PNG
- **Ukuran file:** < 500KB (optimize dulu)
- **Style:** Portrait, close-up, clear face

### Gallery Photos
- **Ukuran:** 1200x800px (landscape) atau 800x1200px (portrait)
- **Format:** JPG atau PNG
- **Ukuran file:** < 1MB per foto
- **Jumlah:** Recommended 6-12 foto

### Optimize Images

Gunakan tools online:
- [TinyPNG](https://tinypng.com/) — compress tanpa quality loss
- [Squoosh](https://squoosh.app/) — advanced image compression
- [Compressor.io](https://compressor.io/) — online image optimizer

Atau via command line:

```bash
# Install ImageMagick
brew install imagemagick  # macOS
apt install imagemagick   # Linux

# Optimize semua JPG di folder gallery
mogrify -resize 1200x1200 -quality 85 assets/gallery/*.jpg
```

## 🎵 Music Guidelines

### Background Music
- **Format:** MP3 (support terbaik di browser)
- **Bitrate:** 128kbps (balance quality vs size)
- **Ukuran file:** < 5MB
- **Durasi:** 2-4 menit (loop seamless lebih baik)
- **Volume:** Normalize audio, jangan terlalu loud

### Free Music Sources

- [YouTube Audio Library](https://studio.youtube.com/channel/UCcbh8w-r4Wc4QkP-vP-A8Mg/music)
- [Free Music Archive](https://freemusicarchive.org/)
- [Bensound](https://www.bensound.com/)
- [Incompetech](https://incompetech.com/music/royalty-free/)

⚠️ **Pastikan music punya license untuk commercial use!**

## 🖼️ Placeholder Images

Jika belum punya foto, gunakan placeholder:

- [Unsplash](https://unsplash.com/s/photos/wedding) — Free wedding photos
- [Pexels](https://www.pexels.com/search/wedding/) — Free stock photos
- [Lorem Picsum](https://picsum.photos/) — Random placeholder images

---

Happy wedding! 💒
