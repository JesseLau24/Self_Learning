# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import time

# Start Time
start_time = time.time()

# Step 1: Load and preprocess the data
# MNIST dataset is included in Keras, we can load it directly
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to be between 0 and 1 (improves model performance)
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# The data is in (28, 28) shape, we need to flatten it to (28*28,) = (784,)
x_train = x_train.reshape((x_train.shape[0], 28 * 28))
x_test = x_test.reshape((x_test.shape[0], 28 * 28))

# Convert the labels to one-hot encoded format (because we have 10 classes, for digits 0-9)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Step 2: Build the neural network model
model = models.Sequential()  # Initialize a Sequential model (stack of layers)

# Add a fully connected (Dense) layer with 128 neurons and ReLU activation function
model.add(layers.Dense(128, activation='relu', input_shape=(28*28,)))

# Add another Dense layer with 64 neurons
model.add(layers.Dense(64, activation='relu'))

# Add the output layer with 10 neurons (one for each digit) and softmax activation (for classification)
model.add(layers.Dense(10, activation='softmax'))

# Step 3: Compile the model
# Define the loss function, optimizer, and metrics to track
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 4: Train the model
# Fit the model to the training data
model.fit(x_train, y_train, epochs=30, batch_size=128, validation_data=(x_test, y_test))

# Step 5: Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)

# Print the test accuracy
print(f'Test accuracy: {test_acc}')

# End Time
end_time = time.time()

# Print Total Time Consumed
print(f"Elapsed time: {end_time - start_time:.2f} seconds")

# Save Model to Directory
model.save('/home/jesse/Projects/Self_Learning/LSTM/Models/mnist_digit_recognizer.keras')
