import streamlit as st

from Screens.Screen import Screen
import base64


class Model(Screen):
    name = 'Model'
    icon = 'diagram-2-fill'

    def build(self):
        st.markdown("# Our Model")
        st.markdown('---')

        st.write(
            "Our exercise classification model is a convolutional neural network (CNN) architecture designed to process input images and provide accurate classification results. "
            "The model consists of multiple layers, including convolutional, pooling, and fully connected layers, which collectively learn and extract meaningful features from the input data. "
            "Dropout layers are incorporated to prevent overfitting, while activation functions introduce non-linearity to capture complex patterns. "
            "The model undergoes a training phase where it learns from labeled data to optimize its performance. During this process, it adjusts its parameters based on a specific loss function and optimizer. "
            "The accuracy achieved by the model is a measure of its effectiveness in correctly classifying exercises based on the input images. The model's architecture and the specific number of classes it can recognize may vary depending on the project requirements.")
        st.write(
            "The current version of our model achieves an accuracy of 90% and supports the following six different exercise classes:")

        st.image(["https://s12.gifyu.com/images/side-stretch.gif", "https://s11.gifyu.com/images/arm-circles.gif",
                  "https://s12.gifyu.com/images/jumping-jacks.gif", "https://s12.gifyu.com/images/squat.gif",
                  "https://s11.gifyu.com/images/high-knee.gif", 'Assets/stand.png'], width=180,
                 caption=["side stretch", "arm circles", "jumping jacks", "squat", "high knee", "stand"])

        st.subheader("Confusion Matrix")
        st.image('Assets/confution matrix.png', caption="Confusion Matrix", use_column_width=True)

        st.subheader("Preprocessing Process")
        st.image('Assets/pipeline.png', caption="Preprocessing Process", use_column_width=True)

