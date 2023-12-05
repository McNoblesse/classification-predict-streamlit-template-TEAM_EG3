import streamlit as st
import pandas as pd
st.header("EDA PROCESS 🚧")
st.sidebar.markdown("EDA Process🚧")

st.subheader("Training Dataset")
df_train = pd.read_csv(r'C:\Users\NOBLESSE\Documents\EXPLORE AI\ADVANCE CLASSIFICATION\classification-predict-streamlit-template-TEAM_EG3\STREAMLIT\pages\train.csv')
#df_test = pd.read_csv('test_with_no_labels.csv')

st.dataframe(df_train)
st.divider()
st.subheader("Section table of the sentiment distribution of the training dataset")
temp = df_train.groupby('sentiment').count()['message'].reset_index().sort_values(by='message',ascending=False)
#temp.style.background_gradient(cmap='Purples')
st.dataframe(temp)

st.divider()
st.subheader("Frequency Distribution")
st.image('Sentiment_Chart.jpg', caption= "A Bar chart showing the frequency dsitribution of the Target Variable(Sentiment)")
st.text("Where the class values are represented below:")
st.write("➡ 2: Highly-Positive")
st.write("➡ 1: Positive")
st.write("➡ 0: Neutral")
st.write("➡ -1: Negative")
