import streamlit as st
from utility import prompt
from processor import Processor

# Initialize the redrafter processor
processor = Processor()

# Define available tones
tones = [key.capitalize() for key in prompt.keys()]

# Set a visually appealing theme for the Streamlit app
st.set_page_config(
    page_title="Redrafter AI",
    layout="wide",  # Utilize more horizontal space
    initial_sidebar_state="expanded",  # Display sidebar by default
)

# Add a visually appealing header to the main content area
st.header("Redrafter AI")
st.subheader("Redraft your text into various tones with ease!")

# Create a sidebar for tone selection
with st.sidebar:
    st.title("Tone Selection")
    selected_tone = st.selectbox("Choose your tone:", tones)

# Main content area
st.write("Enter your text here:")
input_text = st.text_area(label="Enter the text:", height=50, label_visibility='collapsed')  # Adjust text area height

# Redraft button
if st.button("Redraft"):
    try:
        redrafted_text = processor.redraft(input_text, selected_tone)
        st.success("Redrafted text:")
        st.write(redrafted_text)  # Allow for richer formatting
        
    except Exception as e:
        st.error("An error occurred: " + str(e))