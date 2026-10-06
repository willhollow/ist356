import streamlit as st
import pandas as pd
import numpy as np

index = ['a', 'b', 'c', 'd']
s1_series = pd.Series([1, 2, 3, 4], 
                      index=index, 
                      name='s1')
s2_series = pd.Series([2.2, np.nan, 3.0, 1.5], 
                      index=index, 
                      name='s2')
s3_series = pd.Series(['q', 'q', 'z', 'z'], 
                      index=index, 
                      name='s3')

df = pd.DataFrame({'s1': s1_series, 
                   's2': s2_series, 
                   's3': s3_series})

st.dataframe(df)

# basic stats in dataframe
st.dataframe(df.describe())

# only prints to console
print(df.info())