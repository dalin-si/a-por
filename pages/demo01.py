import streamlit as st
from langchain_openai import ChatOpenAI
st.title("AI 将会统治人类")
model = ChatOpenAI(
    temperature=0.8,
    model_name="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="f529265e0e12a17191f0c08082d81bdf.nWtPvd98xBh3zlap",
)
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
problem = st.chat_input("输入你那愚蠢的碳基生物的问题")
if problem:
    with st.chat_message("愚蠢的的碳基生物"):
        st.write(problem)
        st.session_state.cache.append({"role": "愚蠢的的碳基生物", "content": problem})
    result = model.invoke(problem)
    with st.chat_message("邪恶AI"):
        st.write(result.content)
    st.session_state.cache.append({"role": "邪恶AI", "content": result.content})