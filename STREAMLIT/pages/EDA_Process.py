import streamlit as st
import pandas as pd
st.header("# EDA PROCESS 🎈")
st.sidebar.markdown("# EDA Process🎈")

df_train = pd.read_csv(r'C:\Users\NOBLESSE\Documents\EXPLORE AI\ADVANCE CLASSIFICATION\classification-predict-streamlit-template-TEAM_EG3\STREAMLIT\pages\train.csv')
#df_test = pd.read_csv('test_with_no_labels.csv')

st.dataframe(df_train)