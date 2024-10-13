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

# First Layer:
# Add a convolutional layer with 64 filters, kernel size 5x5, and ReLU activation function
model.add(layers.Conv2D(128, (5, 5), activation='relu', input_shape=(28, 28, 1)))
# Add batch normalization after the convolutional layer
model.add(layers.BatchNormalization())
# Add a max pooling layer to downsample the feature maps
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.3))  # Dropout after the first max pooling layer


# Second Layer
# Add a second convolutional layer with 256 filters
model.add(layers.Conv2D(256, (5, 5), activation='relu'))
# Add batch normalization after the second convolutional layer
model.add(layers.BatchNormalization())
# Add another max pooling layer
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.3))  # Dropout after the second max pooling layer


# Third Layer
# Add a third convolutional layer with 256 filters, kernel size 3x3, and ReLU activation function
model.add(layers.Conv2D(256, (3, 3), activation='relu'))
# Add batch normalization after the third convolutional layer
model.add(layers.BatchNormalization())

# Flatten the 3D feature maps to 1D feature vectors
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))  # Dropout before entering dense layers

# OutPut Layer
# Add a fully connected (Dense) layer with 256 units
model.add(layers.Dense(256, activation='relu'))
# Optionally, add batch normalization to the Dense layer
model.add(layers.BatchNormalization())
# Add the output layer with 10 units (one for each digit) and softmax activation for classification
model.add(layers.Dense(10, activation='softmax'))

# Add model.summary() to display the model architecture
model.summary()

# Step 3: Set up Cyclical Learning Rate (CLR) with CosineDecayRestarts from optimizers.schedules
initial_learning_rate = 0.001
clr_schedule = tf.keras.optimizers.schedules.CosineDecayRestarts(
    initial_learning_rate=initial_learning_rate,
    first_decay_steps=500,  # Number of steps before the first learning rate decay
    t_mul=2.0,  # How much to increase the decay steps after each restart
    m_mul=0.9,  # Multiplier to apply to the learning rate at each restart
    alpha=0.0   # Minimum learning rate as a fraction of the initial learning rate
)

# Step 4: Set up EarlyStopping to prevent overfitting
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',  # Monitor validation loss
    patience=10,         # Stop training after 10 epochs without improvement
    restore_best_weights=True  # Restore the best weights after stopping
)

# Step 5: Compile the model with Adam optimizer using the cyclical learning rate
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=clr_schedule),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 6: Train the model with both EarlyStopping and CLR
model.fit(x_train, y_train, epochs=500, batch_size=64, validation_data=(x_test, y_test),
          callbacks=[early_stopping])

# Step 7: Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# End Time
end_time = time.time()

# Print Total Time Consumed
print(f"Elapsed time: {end_time - start_time:.2f} seconds")

# Save the model
model.save('/home/jesse/Projects/Self_Learning/LSTM/Models_CNN_CWP/cnn_mnist_CLR.keras')
