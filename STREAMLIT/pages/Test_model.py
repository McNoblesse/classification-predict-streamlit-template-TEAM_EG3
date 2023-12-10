"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import pandas as pd

st.image('GreenRising.jpg', width= 150)
#st.header("Test Model ♻")
st.sidebar.markdown("Test Model ♻")
# Vectorizer
news_vectorizer = open("resources/tfidf_vectorizer.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

news_vectorizer2 = open("resources/tfidfvect.pkl","rb")
tweet_cv2 = joblib.load(news_vectorizer2) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages

	st.subheader("Climate change tweet classification")

	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Prediction", "Information"]
	selection = st.sidebar.selectbox("Choose Option", options)

	# Building out the "Information" page
	if selection == "Information":
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some information here")

		st.subheader("Raw Twitter data and label")
		if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			st.write(raw[['sentiment', 'message']]) # will write the df to the page

	# Building out the predication page
	if selection == "Prediction":
		st.info("Prediction with ML Models")

	tab1, tab2, tab3 = st.tabs(["SVC", "Random Forest", "Linear Regression"])

	with tab1:
		
	# Creating a text box for user input
		tweet_text1 = st.text_area("SVC Model Test","Type Here")

		if st.button("SVM Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text1]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/svm_model.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

	with tab2:
		
	# Creating a text box for user input
		tweet_text2 = st.text_area("Random Forest Model Test","Type Here")

		if st.button("RF Classify"):
			# Transforming user input with vectorizer
			vect_text2 = tweet_cv2.transform([tweet_text2]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
			prediction = predictor.predict(vect_text2)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

	with tab3:
		
		# Creating a text box for user input
		tweet_text3 = st.text_area("Linear Regression Model Test","Type Here")

		if st.button("LR Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text3]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/logistic_regression_model.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))
   
          
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()