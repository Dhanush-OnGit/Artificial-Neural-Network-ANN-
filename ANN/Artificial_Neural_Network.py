import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train / 255.0  
x_test = x_test / 255.0
y_train = to_categorical(y_train, 10)  
y_test = to_categorical(y_test, 10)

# Build the ANN model
model = Sequential([
    Flatten(input_shape=(28, 28)),  
    Dense(128, activation='relu'), 
    Dense(64, activation='relu'),   
    Dense(10, activation='softmax') 
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Save the model
model.save("mnist_ann_model.h5")
print("Model saved as 'mnist_ann_model.h5'")
