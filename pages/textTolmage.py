import streamlit as st
from zhipuai import ZhipuAI

model = ZhipuAI(api_key="f529265e0e12a17191f0c08082d81bdf.nWtPvd98xBh3zlap")
st.title("设计大师")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role'] == 'user':
            with st.chat_message(message['role']):
                st.write(message["content"])
        else:
            with st.chat_message(message['role']):
                st.image(message["content"],width=300)
desc = st.chat_input("请输入图片的描述")
if desc:
    with st.chat_message("user"):
        st.write(desc)
    st.session_state.cache.append({"role": "user",  "content": desc})
    response = model.images.generations(
        model="cogview-3-plus",
        prompt=desc,
    )
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=300)
    st.session_state.cache.append({"role": "assistant", "content": response.data[0].url})