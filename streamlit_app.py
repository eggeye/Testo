import streamlit as st

# Sätt bakgrundsbilden med hjälp av CSS
def add_background(image_file):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{image_file}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Läs in och konvertera bilden till Base64
import base64
from pathlib import Path

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ange bildfilens sökväg
image_path = "background.jpg"
base64_image = get_base64_of_bin_file(image_path)

# Lägg till bakgrunden
add_background(base64_image)

# Exempel på app-innehåll
st.title("Min Streamlit-app med bakgrundsbild")
st.write("Här är min app med en snygg bakgrund!")

