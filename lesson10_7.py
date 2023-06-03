# https://docs.streamlit.io/library/api-reference/widgets/st.text_input

import streamlit as st

title = st.text_input('Movie title', 'Life of Brian') #自行輸入文字
st.write('The current movie title is', title) 


number = st.number_input('Insert a number')  #自行輸入數字
st.write('The current number is ', number)



import datetime    #日期下拉選單

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)