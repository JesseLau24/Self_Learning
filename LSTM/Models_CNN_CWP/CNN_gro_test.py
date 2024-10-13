from keras.models import load_model # type: ignore
from PIL import Image
import numpy as np
import os
from PIL import ImageEnhance

# Load Model
model = load_model('LSTM/Models_CNN_CWP/cnn_mnist_CLR.keras')

# Directory where the images are stored
image_dir = '/home/jesse/Projects/Self_Learning/LSTM/Pics/'

# Get a list of all image file paths in the directory (assuming .png format) and sort them
image_files = sorted([f for f in os.listdir(image_dir) if f.endswith('.png')])

# Iterate through each image file in sorted order
for image_file in image_files:
    # Load the image and convert to grayscale
    image = Image.open(os.path.join(image_dir, image_file)).convert('L')

    # Adjust contrast
    # enhancer = ImageEnhance.Contrast(image)
    # image = enhancer.enhance(2)  # Adjust contrast, 2 means double the contrast

    
    # Resize image (28x28) and choose resampling filter (NEAREST)
    image = image.resize((28, 28), Image.NEAREST)
    
    # Convert to Numpy Array and Normalize to [0, 1]
    image = np.array(image).astype('float32') / 255
    
    # Reshape to (1, 28, 28, 1) to match the input shape expected by the CNN model
    image = image.reshape(1, 28, 28, 1)
    
    # Make prediction
    prediction = model.predict(image)
    predicted_digit = np.argmax(prediction)
    
    # Output the filename and prediction
    print(f'{image_file}: The model predicts this digit is {predicted_digit}.')
