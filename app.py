import streamlit as st

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="CV - Lê Hoàng Hiệp | Thực tập sinh Tài chính - Ngân hàng",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS TÙY CHỈNH ====================
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
    }
    
    .header-container {
        background: linear-gradient(135deg, #1e3a5f 0%, #2c5282 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(30, 58, 95, 0.3);
    }
    
    .name {
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .title {
        font-size: 1.25rem;
        opacity: 0.9;
        margin-top: 0.3rem;
        font-weight: 400;
    }
    
    .section-card {
        background: white;
        border-radius: 14px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        border-left: 5px solid #2c5282;
    }
    
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 1rem;
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.6rem;
        font-size: 0.95rem;
        color: #2d3748;
    }
    
    .skill-badge {
        display: inline-block;
        background: #ebf4ff;
        color: #2b6cb0;
        padding: 0.4rem 0.9rem;
        border-radius: 20px;
        margin: 0.3rem 0.3rem 0.3rem 0;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid #bee3f8;
    }
    
    .job-title {
        font-weight: 700;
        color: #1a365d;
        font-size: 1.15rem;
        margin-bottom: 0.2rem;
    }
    
    .job-company {
        color: #2c5282;
        font-weight: 600;
        margin-bottom: 0.2rem;
    }
    
    .job-period {
        color: #718096;
        font-size: 0.9rem;
        font-style: italic;
        margin-bottom: 0.8rem;
    }
    
    .footer {
        text-align: center;
        color: #718096;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding: 1.5rem;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown("""
<div class="header-container">
    <h1 class="name">Lê Hoàng Hiệp</h1>
    <p class="title">Sinh viên năm 3 ngành Tài chính - Ngân hàng | Ứng viên Thực tập sinh</p>
</div>
""", unsafe_allow_html=True)

# ==================== LAYOUT 2 CỘT ====================
col1, col2 = st.columns([1, 2], gap="large")

# ========== CỘT TRÁI ==========
with col1:
    # Ảnh đại diện
    st.markdown("<div style='text-align: center; margin-bottom: 1rem;'>", unsafe_allow_html=True)
    st.image("myFrame.jpeg", width=220)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Thông tin liên hệ
    st.markdown("""
    <div class="section-card">
        <div class="section-title">📞 Thông tin liên hệ</div>
        <div class="contact-item">📧 lehoanghiep5805@gmail.com</div>
        <div class="contact-item">📱 0896 881 851</div>
        <div class="contact-item">📍 350/97 Lê Đức Thọ, Phường An Nhơn, TP. Hồ Chí Minh</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Học vấn
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🎓 Học vấn</div>
        <p style="font-weight: 600; color: #1a365d; margin-bottom: 0.3rem;">Ngành Tài chính - Ngân hàng</p>
        <p style="color: #2c5282; margin-bottom: 0.5rem;">Trường Đại học Nguyễn Tất Thành</p>
        <p style="font-size: 0.9rem; color: #4a5568;">
            <strong>Thành tích nổi bật:</strong><br>
            • Nhận học bổng năm học 2023-2024
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Kỹ năng
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🛠️ Kỹ năng</div>
        <span class="skill-badge">Làm việc nhóm</span>
        <span class="skill-badge">Tự học & Thích ứng nhanh</span>
        <span class="skill-badge">Tinh thần trách nhiệm</span>
        <span class="skill-badge">Tiếng Anh giao tiếp tốt</span>
        <span class="skill-badge">Soạn thảo văn bản</span>
        <span class="skill-badge">Kỹ năng bàn phím</span>
    </div>
    """, unsafe_allow_html=True)

# ========== CỘT PHẢI ==========
with col2:
    # Mục tiêu nghề nghiệp
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🎯 Mục tiêu nghề nghiệp</div>
        <p style="line-height: 1.6; color: #2d3748;">
            Mong muốn cơ hội thực tập tại ngân hàng để trực tiếp tiếp cận quy trình nghiệp vụ thực tế 
            và rèn luyện kỹ năng phát triển khách hàng. Qua đó, tích lũy kinh nghiệm để định hình 
            sự nghiệp trong lĩnh vực Tài chính - Ngân hàng.
        </p>
        <p style="line-height: 1.6; color: #2d3748; margin-top: 0.8rem;">
            <strong>Mục tiêu dài hạn:</strong> Chứng tỏ năng lực để trở thành nhân sự chính thức, 
            đồng hành và đóng góp vào sự phát triển chung của ngân hàng.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ========== KINH NGHIỆM LÀM VIỆC (ĐÃ SỬA AN TOÀN) ==========
    st.markdown("""
    <div class="section-card">
        <div class="section-title">💼 Kinh nghiệm làm việc</div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="job-title">Nhân viên Bộ phận F&B</div>', unsafe_allow_html=True)
    st.markdown('<div class="job-company">Khách sạn Rex</div>', unsafe_allow_html=True)
    st.markdown('<div class="job-period">01/2025 – 10/2025</div>', unsafe_allow_html=True)
    
    st.markdown("""
    - Thực hiện nghiệp vụ phục vụ bàn chuyên nghiệp, chỉn chu và trang trọng theo bộ tiêu chuẩn khách sạn 5 sao.
    - Sử dụng tiếng Anh giao tiếp hàng ngày để đón tiếp, tư vấn và chăm sóc các đối tượng khách hàng nước ngoài.
    - Rèn luyện tác phong làm việc nghiêm túc, tỉ mỉ, khả năng quan sát tinh tế và quản lý thời gian hiệu quả trong môi trường dịch vụ có cường độ và áp lực cao.
    """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Chứng chỉ
    st.markdown("""
    <div class="section-card">
        <div class="section-title">📜 Chứng chỉ đạt được</div>
        <ul>
            <li>Kỹ năng soạn thảo văn bản</li>
            <li>Kỹ năng bàn phím</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Quá trình hoạt động
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🚀 Quá trình hoạt động</div>
        <ul>
            <li>
                <strong>Workshop Đầu tư chứng khoán</strong> - "Bản tính đầu tư & tự tin chiến thắng"<br>
                <span style="color: #718096; font-size: 0.9rem;">Tháng 8/2024</span>
            </li>
            <li style="margin-top: 0.8rem;">
                <strong>Học phần “Phân tích đầu tư chứng khoán”</strong><br>
                Thực hành tại Công ty Chứng khoán Rồng Việt và Công ty Chứng khoán Phú Hưng<br>
                <span style="color: #718096; font-size: 0.9rem;">Tháng 4/2025</span>
            </li>
            <li style="margin-top: 0.8rem;">
                <strong>Học phần “Thẩm định tín dụng”</strong><br>
                Thực hành tại Ngân hàng Vietcombank - Thống Nhất<br>
                <span style="color: #718096; font-size: 0.9rem;">Tháng 11/2025</span>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    © 2026 Lê Hoàng Hiệp • CV được tạo bằng Streamlit • Sẵn sàng cho cơ hội thực tập
</div>
""", unsafe_allow_html=True)
