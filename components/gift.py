"""
Gift Section - Amplop digital
"""
import streamlit as st
from components.utils import create_ornament

def render_gift_section(gifts):
    """Render digital envelope section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk mencegah bug Markdown Code Block
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Amplop Digital</h2>
<div style="margin: 1rem 0;">{ornament}</div>
<p class="body-text" style="margin-top: 1rem; color: var(--text-light); font-size: 1.1rem;">
Bagi yang ingin memberikan tanda kasih, dapat melalui:
</p>
</div>
""", unsafe_allow_html=True)
    
    for gift in gifts:
        if gift['type'] == 'bank':
            render_bank_card(gift)
            # Menambah jarak antar kartu
            st.markdown("<br>", unsafe_allow_html=True)
        elif gift['type'] == 'address':
            render_address_card(gift)
            st.markdown("<br>", unsafe_allow_html=True)

def render_bank_card(gift):
    """Render bank account card"""
    
    account_number = gift['account_number']
    
    # Desain kartu rekening dengan gaya amplop elegan (max-width: 600px agar tidak terlalu lebar di PC)
    st.markdown(f"""
<div class="gift-card fade-in-up" style="max-width: 600px; margin: 0 auto; background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 2.5rem 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
<div style="font-size: 3.5rem; margin-bottom: 1rem;">💳</div>
<h3 class="title-elegant" style="font-size: 1.8rem; margin: 1rem 0; color: var(--primary);">
{gift['bank_name']}
</h3>
<div class="account-number" style="background-color: rgba(212, 175, 55, 0.05); border: 1px dashed var(--primary); border-radius: 10px; padding: 1.5rem; margin: 1.5rem 0; font-size: 1.8rem; letter-spacing: 3px; font-weight: bold; color: var(--primary-dark);">
{account_number}
</div>
<p class="body-text" style="font-weight: bold; font-size: 1.1rem; margin: 1rem 0; color: var(--text-color);">
a.n. {gift['account_holder']}
</p>
</div>
""", unsafe_allow_html=True)
    
    # Copy button (Diposisikan tepat di bawah kartu)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div style='margin-top: 1rem;'>", unsafe_allow_html=True)
        # Menambahkan nama bank di tombol agar tidak bingung jika ada lebih dari 1 rekening
        if st.button(f"📋 Salin Nomor Rekening {gift['bank_name']}", key=f"copy_{account_number}", use_container_width=True):
            st.code(account_number)
            st.success(f"✅ Nomor rekening {gift['bank_name']} siap disalin!")
        st.markdown("</div>", unsafe_allow_html=True)

def render_address_card(gift):
    """Render address card"""
    
    st.markdown(f"""
<div class="gift-card fade-in-up" style="max-width: 600px; margin: 0 auto; background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 2.5rem 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
<div style="font-size: 3.5rem; margin-bottom: 1rem;">🎁</div>
<h3 class="title-elegant" style="font-size: 1.8rem; margin: 1rem 0; color: var(--primary);">
{gift['label']}
</h3>
<div style="background-color: rgba(212, 175, 55, 0.05); border: 1px dashed var(--primary); padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0;">
<p class="body-text" style="margin: 0.5rem 0; font-size: 1.05rem; color: var(--text-color); line-height: 1.6;">
📍 {gift['address']}
</p>
<p class="body-text" style="margin: 1rem 0 0.5rem 0; font-weight: bold; font-size: 1.1rem; color: var(--text-color);">
📞 {gift['phone']}
</p>
</div>
</div>
""", unsafe_allow_html=True)
