# https://docs.streamlit.io/library/api-reference/widgets/st.radio

import streamlit as st

genre = st.radio(
    "你喜歡的節目是什麼",
    ('卡通', '戲劇', '愛情'))  #預設是'卡通'

if genre == '卡通':
    st.write('You selected 卡通')
elif genre == '戲劇':
    st.write("You selected 戲劇")
elif genre == '愛情':
    st.write("You selected 愛情")
    