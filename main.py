import streamlit as st
from streamlit_option_menu import option_menu

from Screens.Home import HomePage
from Screens.Demo import Demo
from Screens.Data import Data
from Screens.Model import Model
from Screens.Architecture import Architecture
from Screens.Pilot import Pilot
from Screens.Links import Links



IMAGE_PATH = "Assets/logo.png"
THEAM_COLOR = "#35a0cb"


class Managment:

    def __init__(self, *args, **kwargs):
        super(Managment, self).__init__(*args, **kwargs)
        self.window = None

        st.set_page_config(page_title="Fitrivia Information", page_icon="Assets/icon.ico")


        with st.sidebar:
            st.image(IMAGE_PATH)
            st.title("Navigation Bar")
            choice = option_menu(menu_title=None,
                                 options=[HomePage.name, Demo.name, Data.name, Model.name, Pilot.name, Architecture.name, Links.name],
                                 icons=[HomePage.icon, Demo.icon, Data.icon, Model.icon, Pilot.icon, Architecture.icon, Links.icon], default_index=0)
            #st.info("Welcome to the website")

        if choice == HomePage.name:
            self.window = HomePage()

        elif choice == Demo.name:
            self.window = Demo()

        elif choice == Data.name:
            self.window = Data()

        elif choice == Model.name:
            self.window = Model()

        elif choice == Pilot.name:
            self.window = Pilot()

        elif choice == Architecture.name:
            self.window = Architecture()

        elif choice == Links.name:
            self.window = Links()

        self.window.build()




if __name__ == "__main__":
    Managment()