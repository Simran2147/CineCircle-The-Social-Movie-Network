import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
import requests

# Initialize the Amazon Cognito client
cognito_client = boto3.client('cognito-idp', region_name='us-east-1')

# Define the necessary parameters
client_id = '1h7dri082h30f99sqffaa6f3dp'
client_secret = 'du61dhendpjmuri03uu2o7em0qtdi6ftu4691ur2c6eick71aqb'
redirect_uri = 'http://localhost:8501/'  # Your redirect URI
code = st.query_params["code"] # The authorization code retrieved from the URL
 
# Step 1: Exchange Authorization Code for Access Token
token_url = 'https://cinecircle.auth.us-east-1.amazoncognito.com/oauth2/token'
 
token_payload = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'client_secret': client_secret,
    'code': code,
    'redirect_uri': redirect_uri
}
 
response = requests.post(token_url, data=token_payload)
token_data = response.json()
 
# Extract the access token
access_token = token_data.get('access_token')
 
# Step 2: Retrieve User ID using Access Token
user_info_url = 'https://cinecircle.auth.us-east-1.amazoncognito.com/oauth2/userInfo'
 
headers = {
    'Authorization': f'Bearer {access_token}'
}
 
user_info_response = requests.get(user_info_url, headers=headers)
user_info_data = user_info_response.json()
 
# Extract the user ID
user_id = user_info_data.get('sub')
 
if 'user_id' not in st.session_state:
    st.session_state.user_id = user_id

st.title("CineCircle: The Social Movie Network ")
st.write("Hello", st.session_state.user_id)

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

st.text(selected_genres)

# Add a button with text "Next" which is enabled when the user has more than 3 selections
if len(selected_genres) >= 3:
    if st.button("Next"):
        st.switch_page("pages/app.py")


