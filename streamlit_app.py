import streamlit as st
from mplsoccer import Pitch

# Page setup
st.set_page_config(page_title="ZED FC Analytics", layout="wide")

st.title("⚽ ZED FC Match Analysis Dashboard")
st.sidebar.header("Navigation")

# Youth Team Selector
team_select = st.sidebar.selectbox("Select Squad", ["2005", "2007", "2009"])
st.write(f"Displaying data for the **{team_select}** youth team.")

# Create the ZED FC branded pitch
# Black background with Gold lines
pitch = Pitch(pitch_type='statsbomb', pitch_color='#000000', line_color='#D4AF37')
fig, ax = pitch.draw(figsize=(12, 8))

# Example tracking point (e.g., a shot from the edge of the box)
pitch.scatter(90, 40, s=600, c='#D4AF37', edgecolors='white', marker='football', ax=ax)

st.pyplot(fig)
