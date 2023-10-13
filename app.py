# Import libraries
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Load model
model = load_model('model.h5')

# Create Flask app
app = Flask(__name__)

# Create predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # If no files are sent
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    img_pil = Image.open(file)  # Open image using pillow
    # Process image for prediction
    resized_img = img_pil.resize((200, 200))  # Resize image
    img_array = np.array(resized_img)  # Convert to numpy array
    img_array = img_array / 255  # Normalize image
    img_array = np.expand_dims(img_array, axis=0)  # Reshape to (Sample size, 200, 200, 3)
    prediction = model.predict(img_array)  # Make prediction

    if np.argmax(prediction) == 0:
        return 'female'
    else:
        return 'male'

if __name__ == '__main__':
    app.run(host='0.0.0.0', os.environ.get('PORT', 5000))  # Use provided port or 5000 if not provided
