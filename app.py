from googletrans import Translator
from languages import *
import streamlit as st

translator = Translator()
# out = translator.translate("Hello World", dest="arabic")
# print(out)

st.title("Translator")
source_text = st.text_area("Enter text to translate")
if source_text:
    detected_language_code = translator.detect(source_text).lang
    detected_language_name = language_dict[detected_language_code, "Unknown"]
    st.write(f"Detected language: {detected_language_name.capitalize()}")

dest_lang = st.selectbox("Select a language", languages)
if st.button("Translate") and source_text:
    out = translator.translate(source_text, src=detected_language_code, dest=dest_lang)
    st.write(out.text)