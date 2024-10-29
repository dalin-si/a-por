import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
st.title("AI女友")
model = ChatOpenAI(
    temperature=0.8,
    model_name="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="f529265e0e12a17191f0c08082d81bdf.nWtPvd98xBh3zlap",
)
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")
prompt = PromptTemplate.from_template("你是小怡，和你对话的是你的男朋友，你要温柔贤惠的回答，男友说的话是{input}你需要对你的男朋友的话做出回应，而且只能做出回应，你和你男朋友的历史对话为{history}")
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
problem = st.chat_input("在等待")
if problem:
    with st.chat_message("男友"):
        st.write(problem)
        st.session_state.cache.append({"role": "男友", "content": problem})
    result = chain.invoke({"input":problem})
    with st.chat_message("女友"):
        st.write(result['text'])
    st.session_state.cache.append({"role": "女友", "content": result['text']})