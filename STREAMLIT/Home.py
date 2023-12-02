import streamlit as st

st.markdown("# GreenRising 🎈")
st.sidebar.markdown("# Home Page")

st.header("Welcome to GreenRising, where data meets insight.!")
st.write("Discover the power of data analytics and machine learning")

st.header("Our Mission:")
st.write("Our mission is to catalyze positive environmental change by fostering awareness, implementing eco-friendly solutions, \and advocating for policies that mitigate climate change's impact. Through collaborative efforts, we strive to build resilient  communities that actively contribute to the well-being of the Earth, ensuring a legacy of sustainability \for generations to come.")
st.write("➡Empowering businesses through data-driven decision-making.")
st.write("➡Transforming raw data into actionable insights.")

st.header("Our Vision:")
st.write("Empowering communities for a sustainable future, where the delicate balance of our planet \is respected, and all individuals thrive in harmony with nature.")

st.header("Key Features:")
st.write("➡Advanced Data Analytics: Uncover hidden patterns and trends.")
st.write("➡Machine Learning Models: Predictive modeling for informed decisions.")
st.write("➡Insightful Visualizations: Communicate complex data in a clear manner.")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Explore our EDA Report for in-depth insights.")
    st.link_button("EXPLORE EDA", "http://localhost:8501/EDA_Process")

with col2:
    st.subheader("See the performance of our models on the Model Test page.")
    st.link_button("Test Model", "http://localhost:8501/Test_model")