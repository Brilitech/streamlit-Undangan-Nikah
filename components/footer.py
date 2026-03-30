"""
Footer Section
"""
import streamlit as st
from components.utils import create_ornament

def render_footer(hashtag, groom_name, bride_name):
    """Render footer section"""
    
    st.markdown(f"""
    <div class="footer fade-in-up">
        {create_ornament()}
        
        <div class="hashtag">
            {hashtag}
        </div>
        
        <p class="body-text" style="margin: 1.5rem 0; font-size: 0.95rem;">
            Merupakan suatu kehormatan dan kebahagiaan bagi kami<br>
            apabila Bapak/Ibu/Saudara/i berkenan hadir<br>
            untuk memberikan doa restu kepada kami.
        </p>
        
        {create_ornament()}
        
        <p class="body-text" style="margin: 2rem 0; font-size: 1.1rem; font-weight: 600;">
            Atas kehadiran dan doa restunya,<br>
            kami ucapkan terima kasih.
        </p>
        
        <div style="margin: 2rem 0;">
            <p class="title-cursive" style="font-size: 2rem;">
                {groom_name} & {bride_name}
            </p>
        </div>
        
        {create_ornament()}
        
        <div style="margin: 2rem 0;">
            <p style="color: #7F8C8D; font-size: 0.85rem;">
                Made with ❤️ using Streamlit
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_social_share(groom_name, bride_name, hashtag):
    """Render social media share buttons"""
    
    url = "https://your-wedding-url.streamlit.app"  # Update with actual URL
    text = f"Undangan Pernikahan {groom_name} & {bride_name} {hashtag}"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h3 class="title-elegant" style="font-size: 1.5rem;">Bagikan Undangan</h3>
        <p class="body-text" style="margin: 1rem 0; color: #7F8C8D;">
            Bantu kami sebarkan kebahagiaan ini
        </p>
        
        <div style="margin: 1.5rem 0;">
            <a href="https://wa.me/?text={text}%20{url}" target="_blank" class="social-icon">
                💬
            </a>
            <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" class="social-icon">
                📘
            </a>
            <a href="https://twitter.com/intent/tweet?text={text}&url={url}" target="_blank" class="social-icon">
                🐦
            </a>
            <a href="https://t.me/share/url?url={url}&text={text}" target="_blank" class="social-icon">
                ✈️
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
