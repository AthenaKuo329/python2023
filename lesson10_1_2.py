#https://docs.streamlit.io/library/api-reference/widgets
import streamlit as st

def button_click():
    st.write(st.session_state) #若是按按鈕變成true，則會存在此處

if st.button("say HELLO!", key='myButton', on_click=button_click):   #此default為false，故顯示goodbye!，當按下網頁的"say HELLO!"圖示時，程式又重新開始執行，此時為true，故顯示為say HELLO!，on_click為按鈕被按時要執行哪一個。
    st.write("why hello there?")
else:
    st.write("goodbye!")