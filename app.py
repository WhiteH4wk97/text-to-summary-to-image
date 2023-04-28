import streamlit as st
from Utils import summarize, generate_image


st.title("Text to summary to image")
st.header("This is a sample web app that summarizes text and generates an image of the summary")

text = st.text("Enter your text below", "Astronaut riding a horse on the road")

if st.button("Summarize and Generate Image"):
    if not text:
        st.error("Please Input a text in the text box")
    else:
        with st.spinner("Summarizing...."):
            summary = summarize(text)
        with st.spinner("Geenerating Image...."):
            image = generate_image(summary)
        st.info(f"summary: {summary}")
        st.image(image)


