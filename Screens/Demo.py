import streamlit as st

from Screens.Screen import Screen


class Demo(Screen):
    name = 'Demo'
    icon = 'camera-reels-fill'

    def build(self):
        st.markdown("# Demo Videos 🎥📱")
        st.markdown('---')

        st.markdown(
            "We are thrilled to showcase the capabilities of our innovative FiTrivia app through captivating demo videos. "
            "Take a closer look at the exciting features and engaging experience that await you!")
        st.markdown("📹 Demo Video 1: FiTrivia App Overview Get a glimpse of the FiTrivia app in action! "
                    "This video provides an overview of the app's interface, highlighting its user-friendly design and seamless navigation. Discover how FiTrivia seamlessly combines fitness and knowledge, "
                    "making exercise an integral part of your trivia experience.")

        st.markdown("## New Demo")

        video_file = open('Assets/FiTrivia demo.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

        st.markdown("## Old Demo")

        video_file = open('Assets/old demo.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

        st.markdown(
            '📹 Demo Video 2:  you can see how our app helps users exercise while testing their knowledge, As the user performs an exercise that they believe matches the correct answer, our model classifies the video and marks the answer that it recognizes with a black border. At the end of each question, the correct answer is revealed, and the user gets a few seconds to rest before the next question. Finally, the user can see the score they achieved, making our app a fun and effective way to stay fit and learn!')

        st.markdown(
            '<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7062433379333419008?compact=1" height="399" width="710" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>',
            unsafe_allow_html=True)
