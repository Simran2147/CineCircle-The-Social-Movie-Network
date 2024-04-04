import streamlit as st

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
st.write("Select your favorite genres")
row_style = "display: flex; justify-content: center;"

st.write('<div style="{}">'.format(row_style), unsafe_allow_html=True)
for genre in genres:
    selected = st.checkbox(genre, key=genre)
    if selected:
        selected_genres.append(genre)
st.write('</div>', unsafe_allow_html=True)

# Display selected genres in a list
if selected_genres:
    st.write("Selected genres:")
    st.write(selected_genres)
