import streamlit as st

from Screens.Screen import Screen


class More(Screen):
    name = 'More'
    icon = 'three-dots'

    def build(self):
        st.title("We will add more information soon...")