import streamlit as st
from transformers import pipeline


def main():
    # Set page title
    st.set_page_config(page_title="Language Translation App")

    # Set app title
    st.title("Language Translation App")

    # Create text input box
    text_input = st.text_input(label="Enter text to translate:")

    # Create translation buttons
    if st.button("Translate to Hindi"):
        # Load Hindi translation model
        model_checkpoint = "VinayakMane47/finetuned-en-to-hi"
        translator = pipeline("translation", model=model_checkpoint)

        # Translate text
        translated_text = translator(text_input)

        # Display translated text
        st.write(translated_text[0]["translation_text"])

    if st.button("Translate to Marathi"):
        # Load Marathi translation model
        model_checkpoint = "VinayakMane47/finetuned-en-to-mar"
        translator = pipeline("translation", model=model_checkpoint)

        # Translate text
        translated_text = translator(text_input)

        # Display translated text
        st.write(translated_text[0]["translation_text"])


if __name__ == "__main__":
    main()
