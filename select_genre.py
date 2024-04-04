import streamlit as st

st.title("CineCircle")

# Define genres and their corresponding images
genres = {
    "Fantasy":"images/thriller.webp",
    "Action":"images/action.jpg",
    "Drama":"images/drama.jpg",
    "Adventure":"images/adventure.jpg",
    "Comedy":"images/comedy.jpg",
    "Crime and Mystery":"images/crime.jpg",
    "Historical":"images/historical.jpg",
    "Horror":"images/horror.jpg",
    "Romance":"images/romance.png",
    "Science fiction":"images/scifi.png",
    "Thriller":"images/thriller.webp",
    "Animation":"images/animation.webp",
}

# Display images as checkboxes
selected_genres = []
genre_col_width = 150
row_style = "display: flex; flex-wrap: wrap; justify-content: space-around;"

st.write("Select your favorite genres")
st.write('<div style="{}">'.format(row_style), unsafe_allow_html=True)
for genre, image_url in genres.items():
    selected = st.checkbox("", key=genre)
    st.write('<div style="display: flex; flex-direction: column; align-items: center;">', unsafe_allow_html=True)
    st.image(image_url, width=genre_col_width)
    st.write(genre)
    st.write('</div>', unsafe_allow_html=True)
    if selected:
        selected_genres.append(genre)
st.write('</div>', unsafe_allow_html=True)

# Display selected genres in a list
if selected_genres:
    st.write("Selected genres:")
    st.write(selected_genres)
