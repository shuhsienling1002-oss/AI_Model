import streamlit as st
import google.generativeai as genai

# 設定頁面基礎
st.set_page_config(
    page_title="CRF v9.0 核心介面",
    layout="centered"
)

# 隱藏預設組件
st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>""", unsafe_allow_html=True)

# 核心架構：將互動區放入 Container (Tier 1 Hotzone)
with st.container(border=True):
    st.header("阿美語 AI 神隊友")
    
    # 輸入框與按鈕必須放在 container 內，這才是您要的「位置」
    user_input = st.text_area("請輸入您想詢問的阿美語問題：", height=150)
    
    if st.button("送出提問"):
        if user_input:
            st.info("AI 正在處理您的請求...")
            # 這裡之後可接回您的模型邏輯
        else:
            st.warning("請先輸入問題喔！")

# 系統狀態顯示
st.caption("System: Operational | Version: CRF v9.0")
