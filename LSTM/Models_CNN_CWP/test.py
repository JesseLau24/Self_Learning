# Import necessary libraries
import tensorflow as tf
from keras import layers, models
from keras.datasets import mnist # type: ignore
from keras.utils import to_categorical # type: ignore
import time

# Start Time
start_time = time.time()

# Step 1: Load and preprocess the data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape to (28, 28, 1) for CNN input and normalize pixel values
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255

# Convert labels to one-hot encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Step 2: Build the CNN model
model = models.Sequential()

# First Convolutional Layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))  # Dropout to prevent overfitting

# Second Convolutional Layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))  # Dropout for additional regularization

# Flatten the 3D feature maps to 1D feature vectors
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))  # Dropout before entering dense layers

# Dense Layer
model.add(layers.Dense(128, activation='relu'))

# Output Layer
model.add(layers.Dense(10, activation='softmax'))

# Display the model architecture
model.summary()

# Step 3: Set up Learning Rate Scheduler
initial_learning_rate = 0.0001
clr_schedule = tf.keras.optimizers.schedules.CosineDecayRestarts(
    initial_learning_rate=initial_learning_rate,
    first_decay_steps=500,
    t_mul=2.0,
    m_mul=0.9,
    alpha=0.0
)

# Step 4: Set up EarlyStopping
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,  # Reduce patience to prevent overfitting
    restore_best_weights=True
)

# Step 5: Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=clr_schedule),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 6: Train the model
model.fit(
    x_train, y_train,  # No data augmentation, using raw data
    epochs=200,  # Limited epochs with early stopping
    batch_size=64,
    validation_data=(x_test, y_test),
    callbacks=[early_stopping]
)

# Step 7: Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# End Time
end_time = time.time()

# Print Total Time Consumed
print(f"Elapsed time: {end_time - start_time:.2f} seconds")

# Save the model
model.save('/home/jesse/Projects/Self_Learning/LSTM/Models_CNN_CWP/test.keras')
