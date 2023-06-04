import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the saved .h5 model
model = keras.models.load_model('src/model/calorties_model.h5')

# Define a list of food labels
food_labels = [
    'Apple',
    'Banana',
    'Beetroot',
    'Cabbage',
    'Carrot',
    'Corn',
    'Cucumber',
    'Grapes',
    'Kiwi',
    'Lemon',
    'Lettuce',
    'Mango',
    'Orange',
    'Pear',
    'Pineapple',
    'Pomegranate',
    'Potato',
    'Spinach',
    'Tomato',
    'Watermelon',
]

# Preprocess the image
def preprocess_image(img):
    img = img.resize((150, 150))  # Adjust target_size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = np.vstack([img_array])
    return preprocessed_img

# Make predictions on the image
def predict_food_from_image(img):
    preprocessed_img = preprocess_image(img)
    pred = model.predict(preprocessed_img, batch_size=32)
    pred_index = int(np.argmax(pred, axis=1))
    return food_labels[pred_index]
