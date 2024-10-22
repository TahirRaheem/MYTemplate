import streamlit as st

# Set the background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of your portfolio
st.title("My Portfolio")

# Add your details here
st.header("About Me")
st.write("Your introduction or bio goes here.")

st.header("Projects")
st.write("List of your projects or a brief description.")

st.header("Skills")
st.write("List your skills here.")

st.header("Contact")
st.write("Your contact information or a contact form can go here.")

# You can continue adding sections as needed
