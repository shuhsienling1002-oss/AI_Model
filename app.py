import streamlit as st
import google.generativeai as genai

# 1. 設定頁面標題
st.set_page_config(page_title="阿美語 AI 神隊友", page_icon="💡")
st.title("阿美語 AI 神隊友")

# 2. 設定 API Key (請至 Google AI Studio 取得)
# 建議使用 st.secrets 來管理敏感資訊，測試時可暫時放在這裡
GOOGLE_API_KEY = "您的_API_KEY_放在這裡" 
genai.configure(api_key=GOOGLE_API_KEY)

# 3. 初始化模型 (這裡選用 Gemini 1.5 Flash，適合快速回應)
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. 輸入框與邏輯
user_input = st.text_area("請輸入您想詢問的阿美語問題：", height=150)

if st.button("送出提問"):
    if user_input:
        with st.spinner('AI 神隊友正在思考中...'):
            try:
                # 呼叫 AI
                response = model.generate_content(f"你是一位阿美語專家，請回答以下問題: {user_input}")
                st.subheader("阿美語 AI 回應：")
                st.write(response.text)
            except Exception as e:
                st.error(f"發生錯誤: {e}")
    else:
        st.warning("請先輸入問題喔！")
