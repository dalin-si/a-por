import streamlit as st
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    temperature=0.8,
    model_name="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="f529265e0e12a17191f0c08082d81bdf.nWtPvd98xBh3zlap",
)
st.title("AI 将会统治人类")
problem = st.chat_input("输入你那愚蠢的碳基生物的问题")
if problem:
    with st.chat_message("愚蠢的的碳基生物"):
        st.write(problem)
    result = model.invoke(problem)
    with st.chat_message("assistant"):
        st.write(result.content)