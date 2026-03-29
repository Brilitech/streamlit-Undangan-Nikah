# 🚀 Deployment Guide - Streamlit Cloud

Panduan lengkap deploy undangan pernikahan ke Streamlit Cloud.

---

## 📋 Prerequisites

1. ✅ Akun GitHub (gratis)
2. ✅ Akun Streamlit Cloud (gratis) - [share.streamlit.io](https://share.streamlit.io)
3. ✅ Repository sudah ready di GitHub

---

## 🎯 Step-by-Step Deployment

### Step 1: Persiapan Repository

#### 1.1. Clone & Customize

```bash
# Clone template
git clone https://github.com/your-username/undangan-streamlit.git
cd undangan-streamlit

# Edit config
nano config/wedding_config.py
# ... edit semua data mempelai
```

#### 1.2. Tambahkan Foto

```bash
# Copy foto ke folder assets
cp /path/to/your/photos/groom.jpg assets/images/
cp /path/to/your/photos/bride.jpg assets/images/
cp /path/to/your/photos/prewedding/* assets/gallery/

# Optional: music
cp /path/to/your/music.mp3 assets/music/background.mp3
```

#### 1.3. Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py

# Buka: http://localhost:8501?to=Test%20User
```

#### 1.4. Push ke GitHub

```bash
# Initialize git (jika belum)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Wedding invitation ready"

# Add remote
git remote add origin https://github.com/your-username/undangan-streamlit.git

# Push
git push -u origin main
```

---

### Step 2: Deploy ke Streamlit Cloud

#### 2.1. Login Streamlit Cloud

1. Buka [share.streamlit.io](https://share.streamlit.io)
2. Klik **"Sign up"** atau **"Sign in with GitHub"**
3. Authorize Streamlit Cloud access ke GitHub

#### 2.2. Create New App

1. Klik **"New app"** (tombol di kanan atas)
2. Pilih **"From existing repo"**

#### 2.3. Configuration

Fill in the form:

| Field | Value |
|-------|-------|
| **Repository** | `your-username/undangan-streamlit` |
| **Branch** | `main` |
| **Main file path** | `app.py` |
| **App URL** | `your-custom-name` (misal: `wahyu-haliza-wedding`) |

#### 2.4. Advanced Settings (Optional)

Klik **"Advanced settings"**:

- **Python version:** 3.11 (recommended)
- **Secrets:** (skip dulu, untuk database nanti)

#### 2.5. Deploy!

Klik **"Deploy!"**

Wait 2-5 menit. Streamlit akan:
1. Clone repository
2. Install dependencies dari `requirements.txt`
3. Run `app.py`
4. Deploy app

---

### Step 3: Testing

#### 3.1. Test Basic URL

```
https://your-custom-name.streamlit.app/
```

#### 3.2. Test Personalisasi

```
https://your-custom-name.streamlit.app/?to=Bapak%20Ahmad
https://your-custom-name.streamlit.app/?to=Keluarga%20Pratama
```

#### 3.3. Test RSVP

1. Scroll ke form RSVP
2. Isi data test
3. Submit
4. Refresh page
5. Scroll ke "Ucapan & Doa"
6. Pastikan ucapan muncul

#### 3.4. Test Mobile

- Buka di HP
- Test portrait & landscape
- Test semua fitur

---

## 🔧 Troubleshooting Deployment

### Problem: "No module named 'X'"

**Solusi:**

```bash
# Tambahkan ke requirements.txt
echo "module-name==version" >> requirements.txt

# Push
git add requirements.txt
git commit -m "Add missing dependency"
git push
```

Streamlit auto-redeploy dalam 1-2 menit.

---

### Problem: "File not found: assets/images/groom.jpg"

**Solusi:**

```bash
# Pastikan file ada dan ter-commit
git add assets/images/groom.jpg
git commit -m "Add groom photo"
git push
```

---

### Problem: RSVP tidak tersimpan

**Cause:** Streamlit Cloud filesystem tidak persisten.

**Solusi:** Upgrade ke database eksternal (lihat section Database Setup).

---

### Problem: App terlalu lambat

**Solusi:**

1. **Optimize images:**
   ```bash
   mogrify -resize 1200x1200 -quality 85 assets/gallery/*.jpg
   ```

2. **Reduce gallery size:**
   ```python
   # config/wedding_config.py
   GALLERY = GALLERY[:6]  # Only show 6 photos
   ```

3. **Add caching:**
   ```python
   # components/utils.py
   @st.cache_data
   def load_image(path):
       # ...
   ```

---

## 🌐 Custom Domain

### Step 1: Get Domain

Beli domain di:
- [Namecheap](https://www.namecheap.com/) — $10/year
- [Google Domains](https://domains.google/) — $12/year
- [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) — at cost

### Step 2: Configure DNS

Di domain provider, tambahkan CNAME record:

| Type | Name | Value |
|------|------|-------|
| CNAME | `www` | `your-app.streamlit.app` |
| CNAME | `@` or `root` | `your-app.streamlit.app` |

### Step 3: Streamlit Cloud Settings

1. Buka app di Streamlit Cloud dashboard
2. Klik **"Settings"** → **"General"**
3. Scroll ke **"Custom subdomain"**
4. Masukkan: `www.your-domain.com`
5. Klik **"Save"**

Wait 24-48 jam untuk DNS propagation.

---

## 📊 Analytics (Optional)

### Google Analytics

#### 1. Create GA Property

1. Buka [analytics.google.com](https://analytics.google.com/)
2. Create new property
3. Get tracking ID: `G-XXXXXXXXXX`

#### 2. Add to App

Edit `app.py`:

```python
# Add after st.set_page_config()
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
""", unsafe_allow_html=True)
```

#### 3. Deploy

```bash
git add app.py
git commit -m "Add Google Analytics"
git push
```

---

## 🗄️ Database Setup (Production)

Untuk RSVP yang persisten, gunakan database eksternal.

### Option 1: Supabase (Recommended)

#### 1. Create Supabase Project

1. Buka [supabase.com](https://supabase.com/)
2. Create new project (gratis)
3. Note down:
   - Project URL: `https://xxx.supabase.co`
   - API Key (anon): `eyJ...`

#### 2. Create Table

Di Supabase SQL Editor:

```sql
CREATE TABLE rsvp (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  attendance TEXT DEFAULT 'hadir',
  guests INTEGER DEFAULT 1,
  message TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable public access (for insert & read)
ALTER TABLE rsvp ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public insert" 
ON rsvp FOR INSERT 
TO anon 
WITH CHECK (true);

CREATE POLICY "Allow public read" 
ON rsvp FOR SELECT 
TO anon 
USING (true);
```

#### 3. Add Secrets

Di Streamlit Cloud:

1. App Settings → **Secrets**
2. Add:

```toml
[supabase]
url = "https://xxx.supabase.co"
key = "eyJ..."
```

#### 4. Update Code

Edit `components/rsvp.py`:

```python
import streamlit as st
from supabase import create_client

# Initialize Supabase
supabase = create_client(
    st.secrets["supabase"]["url"],
    st.secrets["supabase"]["key"]
)

def save_rsvp(data):
    try:
        supabase.table("rsvp").insert(data).execute()
        return True
    except:
        return False

def load_rsvp():
    try:
        result = supabase.table("rsvp").select("*").order("created_at", desc=True).execute()
        return result.data
    except:
        return []
```

#### 5. Add Dependency

```bash
# requirements.txt
supabase==2.3.0
```

#### 6. Deploy

```bash
git add .
git commit -m "Add Supabase integration"
git push
```

---

### Option 2: Google Sheets

Simple alternative untuk non-technical users.

#### 1. Create Google Sheet

1. Buat sheet baru
2. Header: `Name | Attendance | Guests | Message | Timestamp`
3. Share → Anyone with link can **edit**
4. Copy sheet ID dari URL

#### 2. Add Secrets

Streamlit Cloud Secrets:

```toml
[google_sheets]
sheet_id = "1abc..."
```

#### 3. Update Code

```python
# requirements.txt
gspread==5.12.0
google-auth==2.27.0

# components/rsvp.py
import gspread
from google.oauth2.service_account import Credentials

# Init gspread
gc = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
sh = gc.open_by_key(st.secrets["google_sheets"]["sheet_id"])
worksheet = sh.sheet1

def save_rsvp(data):
    worksheet.append_row([
        data['name'],
        data['attendance'],
        data['guests'],
        data['message'],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])
```

---

## 🔒 Security

### 1. Environment Variables

Jangan hardcode sensitive data. Gunakan Secrets.

**BAD:**
```python
SUPABASE_URL = "https://xxx.supabase.co"  # Hardcoded
```

**GOOD:**
```python
SUPABASE_URL = st.secrets["supabase"]["url"]  # From secrets
```

### 2. Rate Limiting

Prevent spam RSVP:

```python
import time
from datetime import datetime, timedelta

# Session state
if 'last_rsvp_time' not in st.session_state:
    st.session_state.last_rsvp_time = None

def can_submit_rsvp():
    if st.session_state.last_rsvp_time:
        elapsed = datetime.now() - st.session_state.last_rsvp_time
        if elapsed < timedelta(minutes=5):
            return False
    return True

# In form submit:
if not can_submit_rsvp():
    st.error("⏳ Please wait 5 minutes before submitting again")
else:
    # Save RSVP
    save_rsvp(data)
    st.session_state.last_rsvp_time = datetime.now()
```

---

## 📈 Monitoring

### Streamlit Cloud Metrics

Dashboard otomatis menampilkan:
- **Active users:** Real-time visitors
- **CPU usage:** Performance
- **Memory usage:** Resource consumption
- **Error logs:** Debugging

Access: Streamlit Cloud Dashboard → Your App → Metrics

---

## 🔄 Updates & Maintenance

### Update Content

```bash
# Edit config
nano config/wedding_config.py

# Commit & push
git add config/wedding_config.py
git commit -m "Update wedding details"
git push
```

Auto-redeploy dalam 1-2 menit.

### Update Code

```bash
# Edit component
nano components/hero.py

# Commit & push
git add components/hero.py
git commit -m "Update hero section"
git push
```

### Rollback

```bash
# Check git history
git log --oneline

# Rollback to previous commit
git revert HEAD
git push
```

---

## 💡 Tips & Best Practices

1. **Test locally first** — Always test perubahan di local sebelum push
2. **Commit sering** — Small commits easier to debug
3. **Semantic commit messages** — "Update event time" bukan "fix"
4. **Backup RSVP data** — Export regular jika pakai file-based
5. **Monitor analytics** — Track visitors untuk estimate catering
6. **Mobile-first** — Most guests akan buka di HP
7. **Optimize images** — Smaller file = faster load
8. **Test di banyak devices** — iPhone, Android, tablet
9. **Share early** — Get feedback dari keluarga dulu

---

## 🆘 Support

Stuck? Need help?

1. **Check logs:** Streamlit Cloud Dashboard → App → Logs
2. **GitHub Issues:** [Create issue](https://github.com/your-username/undangan-streamlit/issues)
3. **Streamlit Forum:** [forum.streamlit.io](https://forum.streamlit.io/)
4. **Email support:** your-email@example.com

---

Happy deploying! 🚀💒
