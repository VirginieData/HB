import streamlit as st

from streamlit_extras.let_it_rain import rain
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Happy Birthday",
    page_icon="👋",
)

st.title("Joyeux Anniversaire Antoine !")


# création animation gateaux anniversaire
rain(
    emoji="🎂",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)
