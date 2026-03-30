"""
RSVP Section - Form konfirmasi kehadiran
"""
import streamlit as st
from components.utils import create_ornament, save_rsvp, load_rsvp

def render_rsvp_section():
    """Render RSVP form section"""
    
    ornament = create_ornament()
    
    # Rata kiri untuk judul section
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Konfirmasi Kehadiran</h2>
<div style="margin: 1rem 0;">{ornament}</div>
<p class="body-text" style="margin-top: 1rem; color: var(--text-light); font-size: 1.1rem;">
Mohon konfirmasi kehadiran Anda
</p>
</div>
""", unsafe_allow_html=True)
    
    # Menggunakan container untuk memberikan batas form agar tidak terlalu lebar
    with st.container():
        # Membungkus form dalam kolom tengah agar lebih rapi di PC
        _, col_center, _ = st.columns([1, 6, 1])
        with col_center:
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
                    help="Termasuk Anda (Maksimal 10 orang)"
                )
                
                message = st.text_area(
                    "Ucapan & Doa",
                    placeholder="Tuliskan ucapan dan doa untuk kami...",
                    height=120
                )
                
                # Menggunakan markdown untuk memberi jarak sebelum tombol
                st.markdown("<br>", unsafe_allow_html=True)
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
                            st.success("✅ Terima kasih! Konfirmasi dan doa Anda telah tersimpan.")
                            st.balloons()
                        else:
                            st.error("❌ Terjadi kesalahan saat menyimpan. Silakan coba lagi.")

def render_guest_messages():
    """Render guest messages section"""
    
    ornament = create_ornament()
    
    # Rata kiri HTML
    st.markdown(f"""
<div style="text-align: center; padding: 2rem 0 1rem 0;">
<h2 class="title-elegant" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem;">Buku Tamu</h2>
<div style="margin: 1rem 0;">{ornament}</div>
</div>
""", unsafe_allow_html=True)
    
    # Load all RSVPs
    rsvps = load_rsvp()
    
    # Filter only those with messages
    messages = [r for r in rsvps if r.get('message')]
    
    if not messages:
        st.info("💬 Belum ada ucapan. Jadilah yang pertama memberikan doa!")
        return
    
    # Sort by timestamp (newest first)
    # Note: Pastikan utils.py menambahkan 'timestamp' saat save_rsvp
    messages.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    
    # Membuat scrollable container untuk pesan tamu agar halaman tidak terlalu panjang
    st.markdown("""
    <style>
    .message-container {
        max-height: 500px;
        overflow-y: auto;
        padding-right: 10px;
        scrollbar-width: thin;
        scrollbar-color: var(--primary) var(--card-bg);
    }
    .message-container::-webkit-scrollbar {
        width: 8px;
    }
    .message-container::-webkit-scrollbar-track {
        background: var(--card-bg);
        border-radius: 4px;
    }
    .message-container::-webkit-scrollbar-thumb {
        background-color: var(--primary);
        border-radius: 4px;
    }
    </style>
    <div class="message-container">
    """, unsafe_allow_html=True)
    
    # Display messages
    for msg in messages[:20]:  # Show last 20 messages
        attendance_status = msg.get('attendance', 'hadir')
        if attendance_status == 'hadir':
            emoji = '✅'
            status_color = '#27AE60' # Hijau
        elif attendance_status == 'tidak_hadir':
            emoji = '❌'
            status_color = '#E74C3C' # Merah
        else:
            emoji = '🤔'
            status_color = '#F39C12' # Orange
        
        # Style kartu pesan (Buku Tamu) yang diadaptasi dengan tema emas
        st.markdown(f"""
<div class="message-card fade-in-up" style="background-color: var(--card-bg); border-left: 4px solid var(--primary); border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
<div class="message-name" style="font-weight: bold; font-size: 1.1rem; color: var(--text-color); margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
<span>
<span style="font-size: 1.5rem; margin-right: 0.5rem;">💌</span> 
{msg['name']}
<span style="color: var(--text-light); font-size: 0.9rem; font-weight: normal; margin-left: 0.5rem;">
{f"({msg['guests']} orang)" if msg.get('guests', 1) > 1 else ""}
</span>
</span>
<span style="font-size: 0.9rem; background-color: rgba(0,0,0,0.03); padding: 0.2rem 0.6rem; border-radius: 12px; border: 1px solid {status_color};">
{emoji}
</span>
</div>
<div class="message-text" style="color: var(--text-color); line-height: 1.6; font-style: italic; background-color: white; padding: 1rem; border-radius: 5px; border: 1px dashed var(--border-color); margin: 1rem 0;">
"{msg['message']}"
</div>
<div class="message-date" style="color: var(--text-light); font-size: 0.8rem; text-align: right;">
{msg.get('timestamp', '')}
</div>
</div>
""", unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True) # Tutup message-container
    
    if len(messages) > 20:
        st.info(f"📝 Menampilkan 20 ucapan terbaru dari total {len(messages)} ucapan.")
