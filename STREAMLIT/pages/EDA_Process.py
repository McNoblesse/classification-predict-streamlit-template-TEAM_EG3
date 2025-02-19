import streamlit as st
import pandas as pd

st.image('GreenRising.jpg', width= 150)

st.header("EDA PROCESS 🚧")
st.sidebar.markdown("EDA Process🚧")

st.subheader("Training Dataset")
st.image('dataset.jpg', caption= "Training Dataset")
#df_train = pd.read_csv(r'C:\Users\NOBLESSE\Documents\EXPLORE AI\ADVANCE CLASSIFICATION\classification-predict-streamlit-template-TEAM_EG3\STREAMLIT\pages\train.csv')
#df_test = pd.read_csv('test_with_no_labels.csv')
#st.dataframe(df_train)

st.divider()
st.subheader("Section table of the sentiment distribution of the training dataset")
st.image('sentiment.jpg', caption= "Sentiment Data Distribution")
#temp = df_train.groupby('sentiment').count()['message'].reset_index().sort_values(by='message',ascending=False)
#temp.style.background_gradient(cmap='Purples')
#st.dataframe(temp)

st.divider()
st.subheader("Frequency Distribution")
st.image('Sentiment_Chart.jpg', caption= "A Bar chart showing the frequency dsitribution of the Target Variable(Sentiment)")
st.text("Where the class values are represented below:")
st.write("➡ 2: Highly-Positive")
st.write("➡ 1: Positive")
st.write("➡ 0: Neutral")
st.write("➡ -1: Negative")

st.divider()
st.subheader("Pie Chart Representation")
st.image('pi_chart.jpg', caption= "A Pie chart showing the Percentage Distribution of the Target Variable(Sentiment)")
st.text("Where the class values are represented below:")
st.write("⏩ 2: News")
st.write("⏩ 1: Pro")
st.write("⏩ 0: Neutral")
st.write("⏩ -1: Anti")

st.divider()
st.subheader("Visualization of Hashtags")
st.write("As we know that the dataset used in creating this model is gotten from Twitter (X) and in refrence to the messages used in training the model.")
st.write("We have created a graphical representation of the Top 10 mostly twitted hashtags.")
st.write(" ")
st.image('hashtags.jpg', caption= "A Bar chart showing the frequency dsitribution of the Mostly Used Hashtags")

st.divider()
st.subheader("Wordcloud Visualization")
st.write("Visualization of the frequent words for the train dataset after preprocessing")
st.write("We have created a clustered visualization of words (also know as word bags) of the whole dataset.")
st.write(" ")
st.image('wordcloud.jpg', caption= "A WorldCloud plot showing the frequency dsitribution of the Mostly Used Words in the Dataset")

st.divider()
st.write("At the end of the EDA Process, it was deduced that most of tthe messages (comments) from various tweet ID are mostly of Positive Sentiment.")
st.write("With the Positive Sentiment (1) having total value count of 8,530 which is more that 50% of the whole dataset. This means people truly have inclination towards thiking that human actions have effect on the climate.")
st.write("Let's all do well to continue to create awareness and also look out for mother earth 🌐")
st.image('earth.jpg', caption= "Let's save Earth")