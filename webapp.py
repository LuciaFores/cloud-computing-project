import streamlit as st # to be put in requirements for the containerized web app
import pickle
import numpy as np
import tensorflow as tf # to be put in requirements for the containerized web app
from tensorflow.keras.applications.resnet50 import preprocess_input
import keras.utils as image

# Title
st.header("Cloud Computing Machine Learning App")

# File Uploader
img = st.file_uploader("Image to be recognized", type=['png', 'jpg', 'jpeg'])

# If submit is pressed
if st.button("Submit"):
    # CIFAR-10 labels
    labels = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
    ]
    # Image pre-processing
    # 1. Image resizing
    res_img = image.load_img(img, target_size=(32,32))
    # 2. Batching the image
    img_array = image.img_to_array(res_img)
    img_batch = np.expand_dims(img_array, axis=0)
    # 3. Consistent pixels
    img_preprocessed = preprocess_input(img_batch)
    # Unpickle the model
    model = pickle.load(open('finalized_model.sav', 'rb'))
    prediction = labels[model.predict(img_preprocessed).argmax()]
    # Output the prediction
    st.text(f"This image represents a {prediction}")