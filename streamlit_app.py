import streamlit as st
import datetime
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

st.subheader('Sentiment analysis tool')
if 'sentence' not in st.session_state:
    st.session_state.sentence = "-"


def analyse_sentence():
    analysis = model.predict([st.session_state.input_sentence])
    st.session_state.sentence = analysis


with st.form(key='my_form'):

    st.text_input('Enter your sentence', value="", placeholder="Sentence...", key="input_sentence")
    submit = st.form_submit_button(label='Analyze', on_click=analyse_sentence)

st.write(f'Analysis result = {st.session_state.sentence[0]}')