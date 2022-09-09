## Testing Neural Network Architectures  

The goal is to identify the type of a road sign from an image. Data from the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs.


Based the initial model on the example given in class lecture that identified handwritten numbers:
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
### Testing using a smaller dataset with 3 categories of signs

Which yielded: 
- loss: 4.2431e-07 - accuracy: 1.0000 - 263ms/epoch - 24ms/step

Testing different filters:

|Filters|Result|
|-------|------|
|16|loss: 0.0541 - accuracy: 0.9970 - 230ms/epoch - 21ms/step|
|10|loss: 6.4920e-07 - accuracy: 1.0000 - 230ms/epoch - 21ms/step|
|1|loss: 0.9238 - accuracy: 0.6369 - 228ms/epoch - 21ms/step|

1 filter was pretty bad. But its interesting that # of filters doesn't seem to impact speed.

Testing different hidden layers:

|Layers|Result|
|------|------|
|64|loss: 0.0151 - accuracy: 0.9970 - 237ms/epoch - 22ms/step|
|32|loss: 0.1010 - accuracy: 0.9345 - 228ms/epoch - 21ms/step|
|45|loss: 0.2365 - accuracy: 0.8125 - 263ms/epoch - 24ms/step|
|55|loss: 0.2192 - accuracy: 0.8125 - 279ms/epoch - 25ms/step|

|Filters|Layers|Result|
|-------|------|------|
|8|55|loss: 0.0290 - accuracy: 0.9911 - 205ms/epoch - 19ms/step|
|8|55|loss: 0.0189 - accuracy: 0.9940 - 255ms/epoch - 23ms/step|

After some testing it seems like 8 filters with 55 dense hidden layers has a good balance of accuracy with speed.

### Testing on the full 43-sign dataset:
|Filters|Layers|Result|
|-------|------|------|
|8|55|loss: 3.5032 - accuracy: 0.0548 - 1s/epoch - 4ms/step|
|8|128|loss: 3.5026 - accuracy: 0.0548 - 1s/epoch - 4ms/step|
|16|128|loss: 0.7627 - accuracy: 0.7642 - 1s/epoch - 4ms/step|
|32|128|loss: 3.5110 - accuracy: 0.0492 - 1s/epoch - 4ms/step|
|16|256|loss: 2.7311 - accuracy: 0.2692 - 1s/epoch - 4ms/step|
|32|256|loss: 3.4953 - accuracy: 0.0563 - 2s/epoch - 5ms/step|
|20|100|loss: 3.5024 - accuracy: 0.0549 - 1s/epoch - 4ms/step|
|16|150|loss: 3.4979 - accuracy: 0.0540 - 1s/epoch - 4ms/step|
|16|128|loss: 3.4931 - accuracy: 0.0542 - 1s/epoch - 4ms/step|

Why are my results so terrible?

Okay lets strip this down:
```    
model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ])
```
|Testing Set|Result|
|-----------|------|
|3|loss: 0.2274 - accuracy: 0.9911 - 135ms/epoch - 12ms/step|
|43|loss: 36.2052 - accuracy: 0.7949 - 525ms/epoch - 2ms/step|

Wow that's way better than what I was getting. 

Lets add some hidden layers
```
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(10, activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ])
```
|Testing Set|Result|
|-----------|------|
|3|loss: 1.0276 - accuracy: 0.6488 - 136ms/epoch - 12ms/step|
|43|loss: 3.4984 - accuracy: 0.0553 - 499ms/epoch - 1ms/step|

Why are my results so garbage? After some hunting I found that I wasn't normalizing the pixel intensity of my pictures. Normalizing input values improves learning because the model is less likely to get trapped in a local minima. Normalization ensures that each input variable is treated equally and one doesn't dominate the set (ex: if inputs were age and salary, age is a 2 digit number and salary is 5-7 digits, salary would dominate). 
