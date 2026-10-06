import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
df = pd.read_csv(url)

# anti-pattern: DONT DO THIS
# df = [dddf]

df_ny = df[df['State'] == 'NY']
df_ny_info = df_ny[['First', 'Last', 'State', 'Total Purchased']]


st.dataframe(df)
st.dataframe(df_ny)
st.dataframe(df_ny_info)
 