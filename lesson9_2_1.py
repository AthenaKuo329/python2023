import numpy as np
import pandas as pd 
import streamlit as st

socres_array = np.random.randint(50, high=101, size=(50,5))
student_dataFrame = pd.DataFrame(data=socres_array,
             columns=["國文","英文","數學","地理","社會"], 
             index=range(1,51)) 

st.header("3年5班成績表") 
#st.table(data=student_dataFrame)  資料固定呈現
st.dataframe(data=student_dataFrame) #資料可以移動呈現

# ctrl+ j (呼叫終端機)
# 終端機執行streamlit run lesson9_2_1.py
