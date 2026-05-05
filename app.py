import streamlit as st
import time

# 1. 設定手機上看到的網頁標題與圖示
st.set_page_config(page_title="祝妳生日快樂🎂", page_icon="💖", layout="centered")

# ==========================================
# 加入精美的 CSS 動畫：無盡的粉色愛心與煙火特效
# ==========================================
page_bg_css = """
<style>
/* 隱藏預設的頂部和底部選單，讓畫面更乾淨像獨立 APP */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 改變背景顏色為淡淡的粉紅色漸層 */
.stApp {
    background: linear-gradient(to bottom, #fff0f5, #ffe4e1);
}

/* 製作飄浮圖案的動畫 (無限循環) */
@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0.5); opacity: 1; }
    100% { transform: translateY(-20vh) scale(1.5); opacity: 0; }
}

/* 定義漂浮圖案的樣式 */
.floating-emoji {
    position: fixed;
    bottom: -10%;
    font-size: 2.5rem;
    z-index: 9999;
    pointer-events: none;
    animation: floatUp 6s infinite ease-in;
}

/* 讓祝福語的卡片更精美，加入圓角和陰影 */
.message-card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
    text-align: center;
    margin-top: 20px;
}
</style>

<!-- 產生許多不同位置和速度的粉色愛心與圖案 -->
<div class="floating-emoji" style="left: 10%; animation-duration: 5s; animation-delay: 0s;">💖</div>
<div class="floating-emoji" style="left: 25%; animation-duration: 7s; animation-delay: 1s;">🎆</div>
<div class="floating-emoji" style="left: 40%; animation-duration: 6s; animation-delay: 2s;">🌸</div>
<div class="floating-emoji" style="left: 60%; animation-duration: 8s; animation-delay: 0.5s;">💖</div>
<div class="floating-emoji" style="left: 75%; animation-duration: 5.5s; animation-delay: 3s;">✨</div>
<div class="floating-emoji" style="left: 90%; animation-duration: 7.5s; animation-delay: 1.5s;">💖</div>
"""
# 將特效套用到網頁上
st.markdown(page_bg_css, unsafe_allow_html=True)

# ==========================================
# 2. 這裡可以自己輸入/修改你想對他說的專屬祝福語
# ==========================================
# 使用 HTML 讓文字更有層次感，可以改顏色跟大小
CUSTOM_MESSAGE = """
<h2 style="color: #ff69b4; font-family: sans-serif;">5/16 生日快樂！ 🎉</h2>
<p style="font-size: 1.1rem; color: #555; line-height: 1.8; font-family: sans-serif;">
這是我偷偷用 Python 為你寫的一個小程式。<br><br>
雖然平常可能沒有機會說太多，<br>
但希望能透過這個小驚喜，讓你知道我的心意。<br><br>
希望你的每一天，都像煙火一樣燦爛，<br>
像這些愛心一樣充滿溫暖！🎂
</p>
"""
# ==========================================

# 製作一點期待感的小讀取動畫
with st.spinner("正在為你準備驚喜，請稍等喔..."):
    time.sleep(2.5) # 停頓 2.5 秒製造期待感

# Streamlit 內建的氣球特效（打開網頁時放一次）
st.balloons()

# 顯示精美的卡片與文字
st.markdown(f'<div class="message-card">{CUSTOM_MESSAGE}</div>', unsafe_allow_html=True)

# 顯示無限循環的漂亮煙火動圖 (GIF)
st.markdown("<br>", unsafe_allow_html=True) # 空一行
st.image("https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif", use_container_width=True)