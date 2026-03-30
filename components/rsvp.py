"""
RSVP Section - Form konfirmasi kehadiran
"""
import streamlit as st
from components.utils import create_ornament, save_rsvp, load_rsvp

def render_rsvp_section():
    """Render RSVP form section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Konfirmasi Kehadiran</h2>
        {create_ornament()}
        <p class="body-text" style="margin-top: 1rem; color: #7F8C8D;">
            Mohon konfirmasi kehadiran Anda
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("rsvp_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Nama Lengkap *", placeholder="Nama Anda")
        
        with col2:
            attendance = st.selectbox(
                "Konfirmasi Kehadiran *",
                ["Hadir", "Tidak Hadir", "Masih Ragu"]
            )
        
        guests = st.number_input(
            "Jumlah Tamu",
            min_value=1,
            max_value=10,
            value=1,
            help="Termasuk Anda"
        )
        
        message = st.text_area(
            "Ucapan & Doa",
            placeholder="Tuliskan ucapan dan doa untuk kami...",
            height=120
        )
        
        submitted = st.form_submit_button("📨 Kirim Konfirmasi", use_container_width=True)
        
        if submitted:
            if not name:
                st.error("❌ Mohon isi nama Anda")
            else:
                rsvp_data = {
                    "name": name,
                    "attendance": attendance.lower().replace(" ", "_"),
                    "guests": guests,
                    "message": message
                }
                
                if save_rsvp(rsvp_data):
                    st.success("✅ Terima kasih! Konfirmasi Anda telah tersimpan")
                    st.balloons()
                else:
                    st.error("❌ Terjadi kesalahan. Silakan coba lagi")

def render_guest_messages():
    """Render guest messages section"""
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 class="title-elegant">Ucapan & Doa</h2>
        {create_ornament()}
    </div>
    """, unsafe_allow_html=True)
    
    # Load all RSVPs
    rsvps = load_rsvp()
    
    # Filter only those with messages
    messages = [r for r in rsvps if r.get('message')]
    
    if not messages:
        st.info("💬 Belum ada ucapan. Jadilah yang pertama!")
        return
    
    # Sort by timestamp (newest first)
    messages.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    
    # Display messages
    for msg in messages[:20]:  # Show last 20 messages
        attendance_emoji = {
            'hadir': '✅',
            'tidak_hadir': '❌',
            'masih_ragu': '🤔'
        }
        
        emoji = attendance_emoji.get(msg.get('attendance', 'hadir'), '💌')
        
        st.markdown(f"""
        <div class="message-card fade-in-up">
            <div class="message-name">
                {emoji} {msg['name']}
                {f" ({msg['guests']} orang)" if msg.get('guests', 1) > 1 else ""}
            </div>
            <div class="message-text">
                {msg['message']}
            </div>
            <div class="message-date">
                {msg.get('timestamp', '')}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    if len(messages) > 20:
        st.info(f"📝 Menampilkan 20 dari {len(messages)} ucapan")
