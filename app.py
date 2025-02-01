from googletrans import Translator
from languages import languages, language_dict
import streamlit as st
from unidecode import unidecode

# Initialize the Translator
translator = Translator()

st.title("Translator")

# Input text area for the source text
source_text = st.text_area("Enter text to translate")

# Automatically detect language and get translation
if source_text:
    detected_language = translator.detect(source_text)
    detected_language_code = detected_language.lang
    detected_language_name = language_dict.get(detected_language_code, "Unknown")
    
    # Perform translation
    translated_text = translator.translate(source_text, src=detected_language_code, dest="en").text
    
    translated_pronunciation = unidecode(translated_text)  # For other languages, use unidecode
    # Get pronunciation (transliteration) for any language
    
    
    st.write(f"Detected language: {detected_language_name}")
    st.write(f"Translated text: {translated_text}")
    st.write(f"Pronunciation: {translated_pronunciation}")

# Select destination language
dest_lang = st.selectbox("Select a language", languages)

# Translation process
if st.button("Translate") and source_text:
    # Perform translation to selected language
    out = translator.translate(source_text, src=detected_language_code, dest=dest_lang)
    translated_pronunciation_dest = unidecode(out.text)  # For other languages, use unidecode
    
    st.write(f"Translation: {out.text}")
    st.write(f"Pronunciation: {translated_pronunciation_dest}")
