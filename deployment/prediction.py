#import library
import pandas as pd
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow_hub.keras_layer import KerasLayer 
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

#import pickle
import pickle

#load model
def run():
    file = st.file_uploader("Upload an image", type=["jpg", "png"])

    model = load_model('model_best.keras', custom_objects={'KerasLayer': KerasLayer})

    def import_and_predict(image_data, model):
        image = Image.open(image_data).convert('L')  # Convert image to grayscale
        image = image.resize((48, 48))  # Resize the image
        img_array = np.array(image).astype('float32')
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        # Normalize the image
        img_array = img_array / 255.0

        # Make prediction
        predictions = model.predict(img_array)

        # Get the class with the highest probability
        idx = np.argmax(predictions).item()
        # predicted_class = np.argmax(predictions)

        jenis = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
        result = f"Prediction: {jenis[idx]}"

        return result

    if file is None:
        st.text("Please upload an image file")
    else:
        result = import_and_predict(file, model)
        st.image(file)
        st.write(result)
        
if __name__ == "__main__":
    run()
