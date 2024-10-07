from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load Model
model = load_model('/home/jesse/Projects/Self_Learning/LSTM/Models/mnist_digit_recognizer.keras')

# Load Pic and Convert to Grey
image = Image.open('/home/jesse/Projects/Self_Learning/LSTM/Pics/test_1.png').convert('L')

# Resize image (28x28) and choose resampling filter (NEAREST)
image = image.resize((28, 28), Image.Resampling.NEAREST)

# Convert to Numpy Array and Normalize to [0, 1]
image = np.array(image).astype('float32') / 255

# Reshape to (1, 784)
image = image.reshape(1, 28*28)

# Make prediction
prediction = model.predict(image)
predicted_digit = np.argmax(prediction)

print(f'The model predicts this digit is {predicted_digit}.')
