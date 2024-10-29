import streamlit as st
st.title("AI大模型应用产品")
col,col1 = st.columns(2)
with col:
    st.image("https://tse3-mm.cn.bing.net/th/id/OIP-C.LMcPm-3TvFYIGxlN1z3oDAHaHs?w=180&h=187&c=7&r=0&o=5&dpr=1.3&pid=1.7", use_container_width=True)
    flag = st.button("赛迩慧言",use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")
with col1:
    st.image("https://tse2-mm.cn.bing.net/th/id/OIP-C.93nEfEfjgXqLatCAFZi6mwHaJJ?w=151&h=186&c=7&r=0&o=5&dpr=1.3&pid=1.7", use_container_width=True)
    flag = st.button("赛迩绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textTolmage.py")
c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    flag = st.button("基础版")
    if flag:
        st.switch_page("pages/demo.py")
with c2:
    flag = st.button("进阶版1")
    if flag:
        st.switch_page("pages/demo01.py")
with c3:
    flag = st.button("进阶版2")
    if flag:
        st.switch_page("pages/demo02.py")
with c4:
    flag = st.button("进阶版3")
    if flag:
        st.switch_page("pages/huiyan.py")
with c5:
    flag = st.button("文生图")
    if flag:
        st.switch_page("pages/textTolmage.py")

