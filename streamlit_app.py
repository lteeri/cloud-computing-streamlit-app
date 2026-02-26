import streamlit as st
from model import buildModel

st.title('Cloud Computing Module 3 Bonus Task')


model = buildModel()
# let's show to the user when the model is loaded
st.write("Model loaded: ", bool(model))