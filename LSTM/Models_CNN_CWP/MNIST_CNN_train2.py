# Import necessary libraries
import tensorflow as tf
from keras import layers, models # type: ignore
from keras.datasets import mnist # type: ignore
from keras.utils import to_categorical # type: ignore
import time

# Start Time
start_time = time.time()

# Step 1: Load and preprocess the data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape to (28, 28, 1) because CNN expects a 3D input: (height, width, channels)
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255

# Convert labels to one-hot encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Step 2: Build the CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, kernel size 3x3, and ReLU activation function
model.add(layers.Conv2D(64, (5, 5), activation='relu', input_shape=(28, 28, 1)))

# Add a max pooling layer to downsample the feature maps
model.add(layers.MaxPooling2D((2, 2)))

# Add a second convolutional layer with 64 filters
model.add(layers.Conv2D(128, (5, 5), activation='relu'))

# Add another max pooling layer
model.add(layers.MaxPooling2D((2, 2)))

# Add a third convolutional layer with 64 filters
model.add(layers.Conv2D(128, (3, 3), activation='relu'))

# Flatten the 3D feature maps to 1D feature vectors
model.add(layers.Flatten())

# Add a fully connected (Dense) layer with 64 units
model.add(layers.Dense(64, activation='relu'))

# Add the output layer with 10 units (one for each digit) and softmax activation for classification
model.add(layers.Dense(10, activation='softmax'))

# Step 3: Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 4: Train the model
model.fit(x_train, y_train, epochs=25, batch_size=64, validation_data=(x_test, y_test))

# Step 5: Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# End Time
end_time = time.time()

# Print Total Time Consumed
print(f"Elapsed time: {end_time - start_time:.2f} seconds")

# Save the model
model.save('/home/jesse/Projects/Self_Learning/LSTM/Models_CNN_CWP/cwp_cnn_mnist.keras')