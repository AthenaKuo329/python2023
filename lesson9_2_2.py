# https://docs.streamlit.io/library/api-reference/data/st.metric

import streamlit as st

st.metric(label="溫度1", value="70 °F", delta="1.2 °F")
st.metric(label="溫度2", value="70 °F", delta="-1.2 °F")


#https://docs.streamlit.io/library/api-reference/data/st.json
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})