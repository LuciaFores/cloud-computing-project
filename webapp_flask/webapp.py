from flask import Flask, render_template, request
from PIL import Image #pip3 install Pillow
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input #pip3 install tensorflow keras
import numpy as np
import pickle

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def success():
    if request.method == 'POST': 
        file = request.files['file']

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

        if file and allowed_file(file.filename):
            img = Image.open(file)
            img = img.resize((32, 32))
            img_array = np.array(img)
            img_batch = np.expand_dims(img_array, axis=0)
            img_preprocessed = preprocess_input(img_batch)
            
            model = pickle.load(open("finalized_model.sav", 'rb'))
            prediction = labels[model.predict(img_preprocessed).argmax()]

            return render_template('index.html', result = "Prediction Result", 
                                   prediction = f"This image represents a {prediction}")
        else:
            return render_template('index.html', prediction="Invalid file type. Please upload a PNG, JPG or JPEG file.")

if __name__ == '__main__':
    app.run()
