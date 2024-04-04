

# # Get the user ID from Cognito (assuming you are using Amazon Cognito)
# user_id = st.session_state.get('user_id')

# st.write('Hello', user_id)

import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError

st.title("CineCircle")

# Define genres
genres = [
    "Fantasy",
    "Action",
    "Drama",
    "Adventure",
    "Comedy",
    "Crime and Mystery",
    "Historical",
    "Horror",
    "Romance",
    "Science fiction",
    "Thriller",
    "Animation",
]

# Display checkboxes for genres in a single line
selected_genres = []
st.write("Please select at least 3 genres to continue")
row_style = "display: flex; justify-content: center;"

st.write('<div style="{}">'.format(row_style), unsafe_allow_html=True)
for genre in genres:
    selected = st.checkbox(genre, key=genre)
    if selected:
        selected_genres.append(genre)
st.write('</div>', unsafe_allow_html=True)



# Add a button with text "Next" which is enabled when the user has more than 3 selections
if len(selected_genres) >= 3:
    st.button("Next")

