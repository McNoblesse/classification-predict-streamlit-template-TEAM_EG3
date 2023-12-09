import streamlit as st
import pandas as pd

st.image('GreenRising.jpg', width= 150)
st.header("Feedback 💌")
st.sidebar.markdown("Feedback 💌")

st.subheader("We would like to here your review about the prediction of our model")
st.write("Kindly comment in the textbox below:")

with st.form("my_form"):
    title = st.text_input('Your feedback', 'Write here')
   # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Thanks for your time")