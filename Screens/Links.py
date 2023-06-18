import streamlit as st
# import webbrowser
#
from Screens.Screen import Screen
#
#
class Links(Screen):
    name = 'Links'
    icon = 'link-45deg'

    def build(self):
        st.markdown("# Project Related Resources:")
        st.markdown("## Link to the project repositories")

        col1, col2, col3 = st.columns(3)
        with col1:
            self.html_button(name="FiTrivia Frontend", url="https://github.com/yinonh/FiTrivia-Frontend")

        with col2:
            self.html_button(name="FiTrivia Information", url="https://github.com/yinonh/fitrivia-information")

        with col3:
            self.html_button(name="FiTrivia Backend", url="https://github.com/yinonh/FiTrivia-Backend")

        # st.markdown("## Link to FiTrivia")
        # st.error("Game logic doesn't work - SCE server is down")
        # self.html_button(name="Personal Website", url="https://yinonh.github.io/#/")

        st.markdown("## Data Collection Tool")
        st.write("A tkinter based app that uses cv2 and MediaPipe to capture and track the user's movements while doing sports and saves the video as a series of skeleton images.")

        self.html_button(name="FiTrivia Backend Data Collection", url="https://github.com/yinonh/FiTrivia-Backend/tree/master/Data%20Collection")

        st.markdown("## Data Set")
        st.write(
            """The "Exercise Skeleton" Kaggle database contains over 300K images of people doing exercise in front of the camera. Each image is of size 128 x 128 and shows a skeleton of a person in various exercise positions. The database was created using the MediaPipe Pose Landmarker task, which uses machine learning models to detect the landmarks of human bodies in an image and render visual effects on them. The task outputs body pose landmarks in image coordinates and in 3-dimensional (x,y,z) world coordinates. The database could be a valuable resource for researchers, developers, and fitness enthusiasts interested in analyzing and improving human movement patterns and exercise techniques.""")

        self.html_button(name="Exercise Skeletons Dataset", url="https://www.kaggle.com/datasets/yinonhadad/exercise-skeletons")

        st.markdown("## LinkedIn Post")

        self.html_button(name="LinkedIn Post",
                         url="https://www.linkedin.com/feed/update/urn:li:activity:7062433407691046912?utm_source=share&utm_medium=member_desktop")

        st.title("FiTrivia documentation book")

        # Define the file path
        file_path = "Assets/FiTrivia.pdf"
        with open(file_path, "rb") as file:
            file_data = file.read()
            # Create a download button
            st.download_button("Download", file_data, file_name="FiTrivia.pdf", mime="application/pdf")

    def html_button(self, url, name):
        html_code = '''
        <a href="%s" target="_blank" class="button-link"><span class="button-text">%s</span></a>

        <style>
        .button-link {
        display: inline-block;
          padding: 10px 20px;
          background-color: white;
          text-decoration: none;
          border-radius: 4px;
          border: 2px solid #35a0cb;
          box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.15);
          cursor: pointer;
          text-align: center;
        }

        .button-text {
        color: black;
          text-decoration: none;
        }
        </style>
        '''% (url, name)

        st.markdown(html_code, unsafe_allow_html=True)




