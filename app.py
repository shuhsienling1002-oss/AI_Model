import streamlit as st
import google.generativeai as genai
import os

# 1. 知識庫定義 (從 NotebookLM 遷移來的核心知識)
# 請將您的筆記本重點整理放入此變數
KNOWLEDGE_BASE = """
[在此處貼上您從 NotebookLM 導出的核心知識內容]
例如：我是阿美語教學助手，我的核心規則是...
"""

# 2. 初始化模型 (注入系統指令，實現知識與 APP 的強制綁定)
# 這就是您要的「對應到筆記本」的解決方案
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=f"你現在是阿美語專屬助手，請根據以下知識庫內容進行回答: {KNOWLEDGE_BASE}"
)

# 3. 核心介面 (Tier 1 Hotzone)
with st.container(border=True):
    st.header("阿美語 AI 神隊友")
    user_input = st.text_area("請輸入您想詢問的阿美語問題：", height=150)
    
    if st.button("送出提問"):
        if user_input:
            with st.spinner('AI 神隊友正在檢索筆記本知識...'):
                try:
                    response = model.generate_content(user_input)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"系統運行錯誤: {e}")
