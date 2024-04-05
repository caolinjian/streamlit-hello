import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Demo')

st.write("""
## Line *Chart!*
""")
 
df = pd.read_csv("data.csv")
st.line_chart(df, x="年份", y="数量")

st.write("""
## Table
""")
df2 = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
st.table(df2)
