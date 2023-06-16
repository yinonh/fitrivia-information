import streamlit as st
import webbrowser

from Screens.Screen import Screen


class Links(Screen):
    name = 'Links'
    icon = 'link-45deg'

    def build(self):
        st.markdown("# Project Related Resources:")
        st.markdown("## Link to the project repositories")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("FiTrivia Frontend", on_click=self.open_url,
                      args=("https://github.com/yinonh/FiTrivia-Frontend",))

        with col2:
            st.button("FiTrivia Information", on_click=self.open_url,
                      args=("https://github.com/yinonh/fitrivia-information",))

        with col3:
            st.button("FiTrivia Backend", on_click=self.open_url, args=("https://github.com/yinonh/FiTrivia-Backend",))

        st.markdown("## Link to FiTrivia")
        st.error("Game logic doesn't work - SCE server is down")
        st.button("Personal Website", on_click=self.open_url, args=("https://yinonh.github.io/#/",))

        st.markdown("## Data Collection Tool")
        st.write("A tkinter based app that uses cv2 and MediaPipe to capture and track the user's movements while doing sports and saves the video as a series of skeleton images.")

        st.button("FiTrivia Backend Data Collection", on_click=self.open_url,
                  args=("https://github.com/yinonh/FiTrivia-Backend/tree/master/Data%20Collection",))

        st.markdown("## Data Set")
        st.write(
            """The "Exercise Skeleton" Kaggle database contains over 300K images of people doing exercise in front of the camera. Each image is of size 128 x 128 and shows a skeleton of a person in various exercise positions. The database was created using the MediaPipe Pose Landmarker task, which uses machine learning models to detect the landmarks of human bodies in an image and render visual effects on them. The task outputs body pose landmarks in image coordinates and in 3-dimensional (x,y,z) world coordinates. The database could be a valuable resource for researchers, developers, and fitness enthusiasts interested in analyzing and improving human movement patterns and exercise techniques.""")

        st.button("Exercise Skeletons Dataset", on_click=self.open_url,
                  args=("https://www.kaggle.com/datasets/yinonhadad/exercise-skeletons",))

        st.markdown("## LinkedIn Post")

        st.button("LinkedIn Post", on_click=self.open_url, args=(
        "https://www.linkedin.com/feed/update/urn:li:activity:7062433407691046912?utm_source=share&utm_medium=member_desktop",))

        st.title("FiTrivia documentation book")

        # Define the file path
        file_path = "Assets/FiTrivia.pdf"
        with open(file_path, "rb") as file:
            file_data = file.read()
            # Create a download button
            st.download_button("Download", file_data, file_name="FiTrivia.pdf", mime="application/pdf")

    def open_url(self, url):
        webbrowser.open_new_tab(url)




