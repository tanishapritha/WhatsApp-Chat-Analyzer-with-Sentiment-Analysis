import streamlit as st
import preprocessor

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    df = preprocessor.preprocess(data)

    if df is None or df.empty:
        st.write("Error: No messages were processed. Please upload a valid WhatsApp chat file.")
    else:
        st.write("DataFrame loaded successfully!")
        st.dataframe(df)  # Only show if df is valid

    st.write(bytes_data)  # Debugging step

else:
    st.write("Upload a file to analyze WhatsApp chat data.")
