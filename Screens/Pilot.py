import streamlit as st

from Screens.Screen import Screen


class Pilot(Screen):
    name = 'Pilot'
    icon = 'bar-chart-fill'

    def build(self):
        st.title("Pilot at Begin School in Dimona")

        st.image(["Assets/school.jpg"], width=512,
                 caption=["Begin School in Dimona"])

        # Pilot Overview
        st.header("Pilot Overview")
        st.markdown(
            "The pilot included three groups of students from Begin School in Dimona. The objective was to assess the usability, effectiveness, and enjoyment of the FiTrivia app across different age groups and learning abilities.")

        st.markdown(
            "The first group consisted of three students with ADHD. The app was tested to determine if it could be used by all students together, if the machine learning model accurately tracked exercise quality, and most importantly, if the students enjoyed and learned from using the app.")

        st.image(["Assets/G1.jpeg", "Assets/G12.png"], width=256)

        st.markdown(
            "The second group comprised three 4th-grade students. A trivia room about math was created by their teacher, and the students played the game using the FiTrivia app. This test aimed to evaluate the engagement and educational impact of the app at this grade level.")

        st.markdown(
            "The third group consisted of eight 6th-grade students who also played the trivia game and completed exercises using the app. This larger group allowed for additional insights into scalability and overall user experience.")

        st.image(["Assets/G2.jpeg", "Assets/G3.jpeg"], width=256)

        # Feedback and Future Possibilities
        st.header("Feedback and Future Possibilities")
        st.markdown(
            "The pilot at Begin School in Dimona received positive feedback from both students and teachers. Students found the app enjoyable and engaging, while teachers appreciated its potential as an educational tool.")

        st.markdown(
            "The results of this successful pilot suggest that the FiTrivia app can be effectively integrated into school settings to enhance learning experiences.")

        st.markdown("# Video")

        video_file = open('Assets/pilot video.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

        st.markdown(
            "The valuable feedback received from the teachers and users will be used to further improve the app and address any issues or suggestions. With its combination of trivia questions, physical exercises, and cutting-edge technology, FiTrivia holds great promise as an innovative and interactive learning platform.")

        st.info("Consent obtained from students and parents for photo publication.")
