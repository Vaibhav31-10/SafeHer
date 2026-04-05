import streamlit as st
from sos import show_sos_page
from contacts import show_contacts_page
from location import show_location_page

st.set_page_config(
    page_title="SafeHer",
    page_icon="🛡️",
    layout="centered"
)

page = st.sidebar.radio(
    "Navigation",
    ["SOS", "Contacts", "Location"],
)

if page == "SOS":
    show_sos_page()
elif page == "Contacts":
    show_contacts_page()
elif page == "Location":
    show_location_page()