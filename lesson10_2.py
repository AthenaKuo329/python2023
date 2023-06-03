# https://docs.streamlit.io/library/api-reference/widgets/st.checkbox

import streamlit as st

agree = st.checkbox('我同意')  #預設是false，一般用於多選紐。

if agree:
    st.write('Great!')  #若打勾則會顯示Great!

