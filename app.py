import streamlit as st
from PIL import Image
import os

# 1. Cấu hình trang
st.set_page_config(page_title="CV - Lê Hoàng Hiệp", layout="wide", initial_sidebar_state="collapsed")

# 2. Tùy chỉnh CSS để giống giao diện dark theme của Ảnh 3
st.markdown("""
    <style>
        /* Đặt nền tối cho toàn bộ app */
        .stApp {
            background-color: #0e1117;
        }
        /* Style cho Header */
        .header-container {
            background-color: #1e3a63;
            padding: 30px;
            border-radius: 10px;
            color: white;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .header-name {
            font-size: 2.8rem;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .header-title {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        /* Style cho các Card nội dung */
        .cv-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 20px;
            color: #333333;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .card-heading {
            color: #1e3a63;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 15px;
            border-bottom: 2px solid #f0f2f6;
            padding-bottom: 10px;
        }
        /* Style cho thẻ Kỹ năng (Pills) */
        .skill-pill {
            background-color: #e0f2fe;
            color: #0369a1;
            padding: 8px 16px;
            border-radius: 20px;
            display: inline-block;
            margin: 5px 5px 5px 0;
            font-size: 0.9rem;
            font-weight: 500;
            border: 1px solid #bae6fd;
        }
        /* Style đặc biệt cho phần Kinh nghiệm (Dark box) */
        .exp-box {
            background-color: #1a1a24;
            color: #e0e0e0;
            padding: 20px;
            border-radius: 8px;
            margin-top: 10px;
            border-left: 4px solid #3b82f6;
        }
        .job-title { color: #ffffff; font-size: 1.2rem; font-weight: bold; }
        .job-company { color: #9ca3af; font-size: 1rem; margin-top: 3px; }
        .job-period { color: #6b7280; font-size: 0.9rem; margin-bottom: 10px; }
        .exp-list { margin-top: 10px; padding-left: 20px; }
        .exp-list li { margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

# 3. Phần Header
st.markdown("""
    <div class="header-container">
        <div class="header-name">Lê Hoàng Hiệp</div>
        <div class="header-title">Tốt nghiệp ngành Tài chính - Ngân hàng | Ứng viên Ngân hàng</div>
    </div>
""", unsafe_allow_html=True)

# 4. Chia Layout 2 cột (Tỷ lệ 1:2.2 giống Ảnh 3)
col1, col2 = st.columns([1, 2.2])

# ================= CỘT TRÁI =================
with col1:
    # PHẦN HIỂN THỊ VÀ DÁN ẢNH (Theo yêu cầu của người dùng)
    st.markdown('<div class="cv-card" style="padding:15px; text-align:center;">', unsafe_allow_html=True)
    
    # Ưu tiên hiển thị ảnh mặc định nếu có, hoặc cho phép tải lên
    img_path = 'myFrame.jpg'
    uploaded_file = st.file_uploader("Đổi ảnh đại diện", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
    elif os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    else:
        st.info("Chưa tìm thấy ảnh. Vui lòng tải ảnh lên.")
        
    st.markdown('</div>', unsafe_allow_html=True)

    # THÔNG TIN LIÊN HỆ
    st.markdown("""
        <div class="cv-card">
            <div class="card-heading">📞 Thông tin liên hệ</div>
            <p style="margin-bottom: 8px;">📧 lehoanghiep5805@gmail.com</p>
            <p style="margin-bottom: 8px;">📱 0896 881 851</p>
            <p style="margin-bottom: 0;">📍 350/97 Lê Đức Thọ, Phường An Nhơn, TP. Hồ Chí Minh</p>
        </div>
    """, unsafe_allow_html=True)

    # HỌC VẤN
    st.markdown("""
        <div class="cv-card">
            <div class="card-heading">🎓 Học vấn</div>
            <p style="font-weight: bold; color: #1e3a63; margin-bottom: 5px;">Ngành Tài Chính - Ngân Hàng</p>
            <p style="margin-bottom: 15px;">Trường Đại Học Nguyễn Tất Thành</p>
            <p style="font-weight: bold; margin-bottom: 5px;">Thành tích nổi bật:</p>
            <ul style="margin-top: 0; padding-left: 20px;">
                <li>Nhận được học bổng năm học 2023-2024</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # KỸ NĂNG
    st.markdown("""
        <div class="cv-card">
            <div class="card-heading">⚡ Kỹ năng</div>
            <span class="skill-pill">Làm việc nhóm</span>
            <span class="skill-pill">Tự học & Thích ứng nhanh</span>
            <span class="skill-pill">Tinh thần trách nhiệm</span>
            <span class="skill-pill">Tiếng Anh giao tiếp tốt</span>
            <span class="skill-pill">Soạn thảo văn bản</span>
            <span class="skill-pill">Kỹ năng bàn phím</span>
        </div>
    """, unsafe_allow_html=True)

# ================= CỘT PHẢI =================
with col2:
    # MỤC TIÊU NGHỀ NGHIỆP
    st.markdown("""
        <div class="cv-card">
            <div class="card-heading">🎯 Mục tiêu nghề nghiệp</div>
            <p style="margin-bottom: 10px; line-height: 1.6;">Mong muốn cơ hội thực tập tại ngân hàng để trực tiếp tiếp cận quy trình nghiệp vụ thực tế và rèn luyện kỹ năng phát triển khách hàng. Qua đó, tích lũy kinh nghiệm để định hình sự nghiệp trong lĩnh vực Tài chính - Ngân hàng.</p>
            <p style="line-height: 1.6;">Mục tiêu dài hạn: Chứng tỏ năng lực để trở thành nhân sự chính thức, đồng hành và đóng góp vào sự phát triển chung của ngân hàng.</p>
        </div>
    """, unsafe_allow_html=True)

    # KINH NGHIỆM LÀM VIỆC (Đã sửa lỗi hiển thị HTML so với Ảnh 3)
    st.markdown("""
        <div class="cv-card">
            <div class="card-heading">💼 Kinh nghiệm làm việc</div>
            <div class="exp-box">
                <div class="job-title">Nhân viên Bộ phận F&B</div>
                <div class="job-company">KHÁCH SẠN REX</div>
                <div class="job-period">01/2025 - 10/2025</div>
                <ul class="exp-list">
                    <li>Thực hiện nghiệp vụ phục vụ bàn chuyên nghiệp, chỉn chu và trang trọng theo bộ tiêu chuẩn khách sạn 5 sao.</li>
                    <li>Sử dụng tiếng Anh giao tiếp hàng ngày để đón tiếp, tư vấn và chăm sóc các đối tượng khách hàng nước ngoài.</li>
                    <li>Rèn luyện tác phong làm việc nghiêm túc, tỉ mỉ, khả năng quan sát tinh tế và quản lý thời gian hiệu quả trong môi trường dịch vụ có cường độ và áp lực cao.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # CHỨNG CHỈ ĐẠT ĐƯỢC
    st.markdown("""
        <div class="cv-card">
            <div class="card-heading">📜 Chứng chỉ đạt được</div>
            <ul style="line-height: 1.8; padding-left: 20px;">
                <li>Kỹ năng soạn thảo văn bản</li>
                <li>Kỹ năng bàn phím</li>
                <li>Chứng chỉ thực tập sinh xuất sắc</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # QUÁ TRÌNH HOẠT ĐỘNG
    st.markdown("""
        <div class="cv-card" style="margin-bottom: 0;">
            <div class="card-heading">🚀 Quá trình hoạt động</div>
            <ul style="line-height: 1.8; padding-left: 20px;">
                <li><strong>Tháng 8/2024:</strong> Tham gia Workshop Đầu tư chứng khoán - "Bản lĩnh đầu tư & tự tin chiến thắng"</li>
                <li><strong>Tháng 4/2025:</strong> Tham gia học tập và thực hành học phần "Phân tích đầu tư chứng khoán" tại Công ty Chứng khoán Rồng Việt và Công ty Chứng khoán Phú Hưng</li>
                <li><strong>Tháng 11/2025:</strong> Tham gia học tập và thực hành học phần "Thẩm định tín dụng" tại Ngân hàng Vietcombank - Chi nhánh Thống Nhất</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
