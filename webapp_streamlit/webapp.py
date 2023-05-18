import streamlit as st
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input
import keras.utils as image
import boto3

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
    # Connect to the S3 Bucket
    s3 = boto3.client('s3')
    # Retrieve the model
    s3.download_file('cloud-computing-model-bucket', 'finalized_model.sav', 'finalized_model.sav')
    # Unpickle the model
    model = pickle.load(open("finalized_model.sav", 'rb'))
    prediction = labels[model.predict(img_preprocessed).argmax()]
    # Output the prediction
    st.text(f"This image represents a {prediction}")