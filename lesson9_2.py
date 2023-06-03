import numpy as np
import pandas as pd

socres_array = np.random.randint(50, high=101, size=(50,5))
student_dataFrame = pd.DataFrame(data=socres_array,
             columns=["國文","英文","數學","地理","社會"], 
             index=range(1,51)) 
#DataFrame([data, index, columns, dtype, copy])
#https://pandas.pydata.org/docs/reference/frame.html#constructor

print(student_dataFrame) #用.py檔時要改成print

#至終端機執行"python lesson9_2.py"