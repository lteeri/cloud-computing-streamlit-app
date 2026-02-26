import streamlit as st
from model import buildModel

st.title('Cloud Computing Module 3 Bonus Task')


model = buildModel()

st.write("This tool was an assignment on my Cloud Computing course. " \
"We trained our own sentiment analysis tool using Skikit learn Pyhton " \
"libraries.")
st.write("This tool will analyze whether your sentence is positive, " \
"neutral or negative.")

# let's show to the user when the model is loaded
st.write("Model loaded: ", bool(model))