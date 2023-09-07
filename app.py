import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Nizamani Chess Club", page_icon="♟️")

# Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Rating", "About"])

# Home Section
if menu == "Home":
    st.title("Welcome to Nizamani Chess Club")
    player_data = [
        {"name": "ishaque nizamani", "rating": 1388},
        {"name": "ammar nizamani", "rating": 1883},
        {"name": "hamid nizamani", "rating" : 1632},
        {"name": "salman nizamani", "rating": 832},
        {"name": "sarwan nizamani", "rating": 409},
        {"name": "zarar nizamani", "rating": 1414},
        {"name": "umar nizamani", "rating": 938},
        {"name": "Mali", "rating": 855}
        # Add more player data streamlit run d:/ChessClubWeb/app.py
    ]
 

    for player in player_data:
        st.write(f"**{player['name']}**")
        image_path = f"assets/{player['name']}.jpg"
        st.image(image_path, width=200, caption=player['name'])
        st.write(f"Rating: {player['rating']}")

# Rating Section
elif menu == "Rating":
        st.title("Player Ratings")
        players_data = [
        {"name": "ishaque nizamani", "rating": 1388},
        {"name": "ammar nizamani", "rating": 1883},
        {"name": "hamid nizamani", "rating" : 1632},
        {"name": "salman nizamani", "rating": 832},
        {"name": "sarwan nizamani", "rating": 409},
        {"name": "zarar nizamani", "rating": 1414},
        {"name": "umar nizamani", "rating": 938},
        {"name": "Mali", "rating": 855},
#Add more player data
    ]

        rating_data = {player['name']: player['rating'] for player in players_data}
        
        st.table({"Name": list(rating_data.keys()), "Rating": list(rating_data.values())})

# About Section
else:
    st.title("About Us")
    st.write("We are Nizamani Chess Club, dedicated to promoting the love of chess in Pakistan and beyond.")

# Footer
st.sidebar.write("All rights belong to Salman Nizamani")


