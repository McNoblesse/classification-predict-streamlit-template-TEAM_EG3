import streamlit as st

st.header("About Us 🎈")
st.sidebar.markdown("About Us🎈")
st.divider()
st.subheader("Company Overview:")
st.write("Founded in 2017, GreenRising is an NGO that seeks to educate corporate entities and individuals on the importance of climate change, sustainable development and responsible custodianship of our planet and it's resources")
st.header("")

st.caption("What Sets Us Apart:")
st.write("➡Expertise in advanced data analytics and machine learning")
st.write("➡Committed to delivering high-quality, impactful results")

st.divider()
st.subheader("Meet Our Team:")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('Vicky.jpg', width= 200)
        st.subheader("Victoria Chukwuno")
        st.caption("Team Lead")

    with col2:
        st.image('Lesiba.jpg', width= 200)
        st.subheader("Lesiba Victoria")
        st.caption("Data Analyst")
            
    with col3:
        st.image('Bakwe.jpg', width= 200)
        st.subheader("Bakwe Chokoe")
        st.caption("Project Manager")

with st.container():
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image('Fabian.png', width= 200)
        st.subheader("Fabian Dafat")
        st.caption("Data Engineer")

    with col5:
        st.image('Josh.jpg', width= 200)
        st.subheader("Joshua Oluwole")
        st.caption("Software Engineer")
            
    with col6:
        #st.image('Kemi.jpg', width= 200)
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("Data Specialist")
        st.caption("Data Specialist")