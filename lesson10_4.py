# https://docs.streamlit.io/library/api-reference/widgets/st.selectbox

#下拉式選單
import streamlit as st

option = st.selectbox(
    '你想要如何聯絡?',
    ('Email', '電話', '手機'))

st.write('You selected:', option) #只要點選項目就顯示
