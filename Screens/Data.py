import streamlit as st

from Screens.Screen import Screen


class Data(Screen):
    name = 'Data'
    icon = "images"

    def build(self):
        st.markdown("# Our Data Base")
        st.markdown('---')

        st.subheader("Data Collection Process")
        st.write("The data for this project was collected using a custom program that utilizes OpenCV and MediaPipe.")
        st.write(
            "This program captures user images while performing exercises and processes them to extract skeletal information.")
        st.write("The resulting skeleton images are stored for use in the project.")
        st.write(
            "To explore the code and learn more about the data collection process, you can visit the following GitHub link:")
        st.markdown(
            "[FiTrivia Data Collection GitHub Repository](https://github.com/yinonh/FiTrivia-Backend/tree/master/Data%20Collection)")

        st.image(["Assets/student1.jpeg", "Assets/student2.jpeg"], width=512,
                 caption=["", "Consent obtained from students and parents for photo publication."])
        #st.write("We have obtained the consent of both the students and their parents to publish these photos.")

        st.markdown("---")

        st.subheader("Data Structure")

        st.write(
            "The 'Exercise Skeleton' Kaggle database is a collection of over 300K images depicting people performing exercises in front of the camera.")
        st.write(
            "Each image is of size 128 x 128 and displays a skeleton representation of a person in various exercise positions.")
        st.write(
            "The database was created using the MediaPipe Pose Landmarker task, which employs machine learning models to detect body landmarks and render visual effects.")
        st.write(
            "The task outputs body pose landmarks in both image coordinates and 3-dimensional (x, y, z) world coordinates.")
        st.write(
            "This database serves as a valuable resource for researchers, developers, and fitness enthusiasts interested in analyzing and improving human movement patterns and exercise techniques.")

        st.subheader("Examples of Database Images")
        st.image(["Assets/st.png", "Assets/ac.png", "Assets/jj.png", "Assets/s.png"], width=128,
                 caption=["side stretch", "arm circles", "jumping jacks", "squat"])


        st.subheader("Access the 'Exercise Skeleton' Database")
        st.write("To access the 'Exercise Skeleton' database on Kaggle, please visit the following link:")
        st.markdown(
            "[Exercise Skeleton Kaggle Database](https://www.kaggle.com/datasets/yinonhadad/exercise-skeletons)")

