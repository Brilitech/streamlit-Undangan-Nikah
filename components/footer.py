"""
Footer Section
"""
import streamlit as st
import urllib.parse
from components.utils import create_ornament

def render_footer(hashtag, groom_name, bride_name):
    """Render footer section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk mencegah bug Markdown Code Block
    st.markdown(f"""
<div class="footer fade-in-up" style="background-color: var(--card-bg); text-align: center; padding: 4rem 1rem 2rem 1rem; border-top: 2px solid var(--border-color); margin-top: 3rem;">
<div style="margin-bottom: 2rem;">{ornament}</div>
<div class="hashtag" style="font-family: 'Georgia', serif; font-size: 1.5rem; font-style: italic; color: var(--primary); letter-spacing: 2px; margin: 1rem 0;">
{hashtag}
</div>
<p class="body-text" style="margin: 1.5rem 0; font-size: 1rem; color: var(--text-color); line-height: 1.8;">
Merupakan suatu kehormatan dan kebahagiaan bagi kami<br>
apabila Bapak/Ibu/Saudara/i berkenan hadir<br>
untuk memberikan doa restu kepada kami.
</p>
<div style="margin: 2rem 0;">{ornament}</div>
<p class="body-text" style="margin: 2rem 0; font-size: 1.1rem; font-weight: 600; color: var(--text-color);">
Atas kehadiran dan doa restunya,<br>
kami ucapkan terima kasih.
</p>
<div style="margin: 2rem 0;">
<p style="font-size: 3rem; color: var(--primary); font-family: 'Great Vibes', 'Brush Script MT', cursive, serif; margin: 0; line-height: 1.2; text-shadow: 1px 1px 2px rgba(212, 175, 55, 0.2);">
{groom_name} & {bride_name}
</p>
</div>
<div style="margin: 2rem 0;">{ornament}</div>
<div style="margin-top: 3rem;">
<p style="color: var(--text-light); font-size: 0.85rem; letter-spacing: 1px;">
Made with ❤️ using Streamlit
</p>
</div>
</div>
""", unsafe_allow_html=True)

def render_social_share(groom_name, bride_name, hashtag):
    """Render social media share buttons"""
    
    url = "https://your-wedding-url.streamlit.app"  # Ganti dengan URL asli Anda nanti
    raw_text = f"Undangan Pernikahan {groom_name} & {bride_name} {hashtag}"
    
    # Mengamankan teks untuk URL (URL Encoding)
    text_encoded = urllib.parse.quote(raw_text)
    url_encoded = urllib.parse.quote(url)
    
    # Gaya untuk tombol sosial media
    icon_style = "display: inline-block; width: 45px; height: 45px; line-height: 45px; border-radius: 50%; background-color: var(--card-bg); border: 1px solid var(--primary); color: var(--primary); text-decoration: none; font-size: 1.2rem; margin: 0 0.5rem; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.1); transition: all 0.3s ease;"
    
    # Rata kiri untuk HTML
    st.markdown(f"""
<div style="text-align: center; padding: 3rem 0 1rem 0;">
<h3 class="title-elegant" style="font-size: 1.8rem; color: var(--primary); margin-bottom: 0.5rem;">Bagikan Undangan</h3>
<p class="body-text" style="margin-bottom: 2rem; color: var(--text-light);">
Bantu kami sebarkan kebahagiaan ini
</p>
<div style="margin: 1.5rem 0;">
<a href="https://wa.me/?text={text_encoded}%20{url_encoded}" target="_blank" style="{icon_style}">💬</a>
<a href="https://www.facebook.com/sharer/sharer.php?u={url_encoded}" target="_blank" style="{icon_style}">📘</a>
<a href="https://twitter.com/intent/tweet?text={text_encoded}&url={url_encoded}" target="_blank" style="{icon_style}">🐦</a>
<a href="https://t.me/share/url?url={url_encoded}&text={text_encoded}" target="_blank" style="{icon_style}">✈️</a>
</div>
</div>
""", unsafe_allow_html=True)
