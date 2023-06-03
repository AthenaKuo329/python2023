#https://docs.streamlit.io/library/api-reference/widgets
import streamlit as st

if st.button("say HELLO!", key='myButton'):   #此default為false，故顯示goodbye!，當按下網頁的"say HELLO!"圖示時，程式又重新開始執行，此時為true，故顯示為say HELLO!
    st.write("why hello there?")
else:
    st.write("goodbye!")