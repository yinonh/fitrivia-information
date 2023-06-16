import streamlit as st

from Screens.Screen import Screen


class HomePage(Screen):
    name = 'Home'
    icon = 'house'

    def build(self):
        st.title("FiTrivia")
        st.subheader('Combine learning and exercise in an engaging way!')

        # Add a short description of the app
        st.markdown(
            'FiTrivia is a cross-platform application that combines trivia questions with physical exercises. '
            'Users must perform various exercises to answer multiple-choice questions, and a machine learning model accurately tracks the quality of exercises performed.')

        st.markdown('The app is a trivia application that combines exercise and cutting-edge technology. It is developed with Flutter for the user-friendly front-end and Python/Django for the back-end REST API. '
            'This app utilizes camera technology and a Convolutional Neural Network (CNN) model to create an interactive experience. '
            'Players are required to perform designated exercises in front of their cameras to submit their responses.')

        # Add a list of features
        st.subheader('Key features include:')
        st.write('🤖 Machine learning model for exercise classification')
        st.write('📊 Exercise tracking and real-time feedback')
        st.write('📱 Cross-platform compatibility')
        st.write('🏋️‍♂️ Gamification of exercise for added engagement')
        st.write('👥 Adaptable for different populations')

        st.subheader('Main Technologies:')

        institutions_images1 = [
            'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png',
            'https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_flutter_icon_130599.png',
            'https://www.svgrepo.com/show/353657/django-icon.svg',
            'https://i.ibb.co/MgPJtY1/New-Project-1.png']

        for index, col in enumerate(st.columns(len(institutions_images1))):
            with col:
                st.image(institutions_images1[index], width=100)

        institutions_images2 = [
            'https://i.ibb.co/jrzzV0S/New-Project-1-1.png',
            'https://raw.githubusercontent.com/wiki/opencv/opencv/logo/OpenCV_logo_no_text.png',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7RiM9Z5UItq-TJVnmJvQL_Kr88NzjJU_ZdA&usqp=CAU']

        for index, col in enumerate(st.columns(len(institutions_images2))):
            with col:
                st.image(institutions_images2[index], width=100)






