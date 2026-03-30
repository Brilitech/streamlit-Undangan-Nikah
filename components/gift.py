"""
Gift Section - Amplop digital
"""
import streamlit as st
from components.utils import create_ornament

def render_gift_section(gifts):
    """Render digital envelope section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Amplop Digital</h2>
        {create_ornament()}
        <p class="body-text" style="margin-top: 1rem; color: #7F8C8D;">
            Bagi yang ingin memberikan tanda kasih, dapat melalui:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    for gift in gifts:
        if gift['type'] == 'bank':
            render_bank_card(gift)
        elif gift['type'] == 'address':
            render_address_card(gift)

def render_bank_card(gift):
    """Render bank account card"""
    
    account_number = gift['account_number']
    
    st.markdown(f"""
    <div class="gift-card fade-in-up">
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🏦</div>
            
            <h3 class="title-elegant" style="font-size: 1.5rem; margin: 1rem 0;">
                {gift['bank_name']}
            </h3>
            
            <div class="account-number">
                {account_number}
            </div>
            
            <p class="body-text" style="font-weight: 600; margin: 1rem 0;">
                a.n. {gift['account_holder']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Copy button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(f"📋 Salin Nomor Rekening", key=f"copy_{account_number}"):
            st.code(account_number)
            st.success("✅ Nomor rekening siap disalin!")

def render_address_card(gift):
    """Render address card"""
    
    st.markdown(f"""
    <div class="gift-card fade-in-up">
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📦</div>
            
            <h3 class="title-elegant" style="font-size: 1.5rem; margin: 1rem 0;">
                {gift['label']}
            </h3>
            
            <div style="background: rgba(212, 175, 55, 0.1); padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                <p class="body-text" style="margin: 0.5rem 0;">
                    📍 {gift['address']}
                </p>
                <p class="body-text" style="margin: 0.5rem 0; font-weight: 600;">
                    📞 {gift['phone']}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
