import streamlit as st
import time
import random # 🌟 新增這個工具：用來產生隨機的漂浮特效

# 1. 設定手機上看到的網頁標題與圖示
st.set_page_config(page_title="祝妳生日快樂🎂", page_icon="💖", layout="centered")

# ==========================================
# 加入精美的 CSS 動畫：滿版無限循環漂浮特效
# ==========================================
page_bg_css = """
<style>
/* 隱藏預設的頂部和底部選單 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 改變背景顏色為淡淡的粉紅色漸層 */
.stApp {
    background: linear-gradient(to bottom, #fff0f5, #ffe4e1);
}

/* 製作飄浮圖案的動畫 (無限循環，加入淡入淡出效果) */
@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0.5); opacity: 0; }
    10% { opacity: 0.9; }
    90% { opacity: 0.9; }
    100% { transform: translateY(-20vh) scale(1.2); opacity: 0; }
}

/* 定義漂浮圖案的樣式 */
.floating-emoji {
    position: fixed;
    bottom: -10%;
    z-index: 9999;
    pointer-events: none;
    animation-name: floatUp;
    animation-iteration-count: infinite;
    animation-timing-function: linear; /* 讓上升速度保持均勻均速 */
}

/* 讓祝福語的卡片更精美，加入圓角和陰影 */
.message-card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
    text-align: center;
    margin-top: 20px;
    position: relative;
}
</style>
"""

# 🌟 魔法升級：用 Python 自動產生 40 個隨機的漂浮圖案！
floating_html = ""
emojis = ['💖', '🎆', '🌸', '✨', '💕', '🎂']
for _ in range(40):
    emoji = random.choice(emojis)
    left = random.randint(0, 100)           # 在畫面左右 0%~100% 隨機分配位置
    duration = random.uniform(8, 20)        # 漂浮速度 (8秒到20秒不等，有快有慢)
    delay = random.uniform(0, 15)           # 出現的時間差 (0到15秒隨機出現，才不會擠在一起)
    size = random.uniform(1.0, 2.5)         # 隨機大小
    floating_html += f'<div class="floating-emoji" style="left: {left}%; font-size: {size}rem; animation-duration: {duration}s; animation-delay: {delay}s;">{emoji}</div>\n'

# 將 CSS 和 滿滿的漂浮圖案套用到網頁的背景上
st.markdown(page_bg_css + floating_html, unsafe_allow_html=True)


# ==========================================
# 2. 專屬祝福語
# ==========================================
CUSTOM_MESSAGE = """
<p style="font-size: 1.1rem; color: #555; line-height: 1.8; font-family: sans-serif;">
李芯貝祝妳20歲生日快樂！<br><br>
恭喜妳也成為一個20歲的小大人了<br>
雖然妳總是對我很客氣也不願意收下我的禮物<br>
但是我還是寫了這個小網頁給妳一下<br>
希望妳在未來不要再常常被擊垮或者是不開心<br>
也不要再被那些討厭的人和事給左右<br>
遵循自己所想做自己想做同時也要保護好自己<br>
有事情呢還是可以找我幫忙妳可以不用不好意思<br><br>
還有什麼時候才要吃飯我都找不到人吃飯💢💢<br><br>
祝妳的20歲順利也開心持續有淡淡的幸福出現🎂🎂🎂
</p>
"""
# ==========================================

# 製作一點期待感的小讀取動畫
with st.spinner("正在為你準備驚喜，請稍等喔..."):
    time.sleep(2.5) 

# 一進來時施放的大氣球特效 (保留原本打開網頁第一瞬間的驚喜感)
st.balloons()

# 顯示精美的卡片與文字
st.markdown(f'<div class="message-card">{CUSTOM_MESSAGE}</div>', unsafe_allow_html=True)

# 顯示無限循環的漂亮煙火動圖 (GIF)
st.markdown("<br>", unsafe_allow_html=True) 
st.image("https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True) 
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjduZjBva3phdDJmamFsbDVydzl1eG11a3oydG5zZ2hnc2xtY2tmciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IFjSbBHETzzr6GJdwW/giphy.gif", use_container_width=True)
