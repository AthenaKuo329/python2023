# https://docs.streamlit.io/library/api-reference/widgets/st.multiselect

import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
#預設選'Yellow', 'Red'，可以多選。

st.write('You selected:', options) #被選到的會依序列出於list