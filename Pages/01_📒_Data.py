import streamlit as st
import pandas as pd


st.set_page_config(
    page_title = 'Data',
    page_icon = '📒',
    layout = 'wide'
)

data = pd.read_csv('Data/full_train_data.csv')

st.title('Database')

st.write(data)