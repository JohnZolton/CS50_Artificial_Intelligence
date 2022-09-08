## Testing Neural Network Architectures  

Based the initial model on the example given in class lecture:
```# Create a convolutional neural network
model = tf.keras.models.Sequential([
    # Convolutional layer. Learn 32 filters using a 3x3 kernel
    tf.keras.layers.Conv2D(
        32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    ),

    # Max-pooling layer, using 2x2 pool size
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Flatten units
    tf.keras.layers.Flatten(),

    # Add a hidden layer with dropout
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.5),

    # Add an output layer with output units for all categories of signs
    tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
])

# Train neural network
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```
Which yielded: loss: 4.2431e-07 - accuracy: 1.0000 - 263ms/epoch - 24ms/step

Dropping 32 filters to 16 filters yielded: loss: 0.0541 - accuracy: 0.9970 - 230ms/epoch - 21ms/step

Further decreasing to 10 filters yielded: loss: 6.4920e-07 - accuracy: 1.0000 - 230ms/epoch - 21ms/step

Decreasing the hidden layer from 128 to 64 yielded: loss: 0.0151 - accuracy: 0.9970 - 237ms/epoch - 22ms/step

Further decreasing to 32 yielded: loss: 0.1010 - accuracy: 0.9345 - 228ms/epoch - 21ms/step

A significant decrease from 64

increasing to 45: loss: 0.2365 - accuracy: 0.8125 - 263ms/epoch - 24ms/step

increasing to 55: loss: 0.2192 - accuracy: 0.8125 - 279ms/epoch - 25ms/step
