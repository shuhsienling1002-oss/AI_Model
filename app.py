import streamlit as st
import time

# 1. 介面基礎設定 (隱藏預設的 Streamlit 選單與頁腳，達到極簡視覺)
st.set_page_config(page_title="阿美語AI神隊友", page_icon="🌿", layout="centered")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. 標題設計
st.title("🌿 阿美語AI神隊友")
st.markdown("---")

# 3. 初始化對話歷史狀態 (State Flow)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. 顯示歷史對話 (輸出方框)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 使用者輸入方框 (Input Zone)
if prompt := st.chat_input("請輸入您想查詢的阿美語或中文..."):
    # 將使用者輸入加入歷史紀錄並顯示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 6. AI 回應區塊 (這裡預留了串接 API 的位置)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # 模擬 AI 思考與打字效果 (未來此處替換為實際的 Gemini API 呼叫)
        full_response = ""
        # 這裡的假回應只是為了展示介面，之後需換成真實模型回應
        simulated_response = f"這是一個模擬回應。未來只要將您的 NotebookLM 語料匯入 Gemini API，我就能用阿美語回答關於「{prompt}」的問題！" 
        
        for chunk in simulated_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    # 將 AI 回應加入歷史紀錄
    st.session_state.messages.append({"role": "assistant", "content": full_response})
