import streamlit as st

from Screens.Screen import Screen


class Architecture(Screen):
    name = 'Architecture'
    icon = 'diagram-3-fill'

    def build(self):
        st.title("Architectures")
        st.markdown("## System architecture")
        st.image("Assets/sys_arc.png", width=528)
        st.markdown("""
        1. Front-End (Flutter): The front-end is built using Flutter, a popular cross-platform framework for developing cross platform applications. Flutter allows you to create a visually appealing and interactive user interface for your app.

        2. Firebase Database: Firebase provides a real-time NoSQL database as a service. The user's interactions and any relevant data are saved in the Firebase database. This data can include user profiles, chat messages, and other application-specific information.

        3. Django REST API Backend: Django is a powerful and scalable Python web framework. The Django backend includes a model for image classification, allowing to process images and obtain classification results.

        4. Image Classification Model: Within our Django backend, we have implemented an image classification model. This model is trained to classify images into our train classes. When the front-end sends an image to the Django backend through the REST API, the image classification model processes the image and returns the classification results.
        """)

        st.markdown("## Model architecture")

        st.markdown("""The model is a sequential neural network designed for image classification. It consists of convolutional layers to extract features, followed by pooling and dropout layers to reduce overfitting. The flattened features are passed through dense layers with ReLU activation. The output layer predicts the image category using categorical cross-entropy loss and an appropriate activation function. The goal is to accurately classify images into predefined categories.""")


        st.image("Assets/Arc.png", width=528)

