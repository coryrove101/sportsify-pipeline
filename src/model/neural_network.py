import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self, input_dim):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_dim=input_dim))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(16, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, X, y, epochs=100, batch_size=10):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X, y):
        return self.model.evaluate(X, y)
    
    


# Define the SIREN activation function
def siren(x, w0=1.0):
    return tf.sin(w0 * x)

# Create a SIREN layer
class SirenLayer(tf.keras.layers.Layer):
    def __init__(self, units, w0=1.0):
        super(SirenLayer, self).__init__()
        self.units = units
        self.w0 = w0

    def build(self, input_shape):
        self.kernel = self.add_weight("kernel",
                                      (int(input_shape[-1]), self.units),
                                      initializer="random_normal",
                                      trainable=True)

    def call(self, inputs):
        return siren(tf.matmul(inputs, self.kernel) + 0.0)

# Build the SIREN neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Input layer
    SirenLayer(128),                   # Hidden layer 1
    SirenLayer(128),                   # Hidden layer 2
    SirenLayer(128),                   # Hidden layer 3
    tf.keras.layers.Dense(1)           # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Generate synthetic data for training (e.g., a sine wave)
x = np.linspace(0, 10, 1000)
y = np.sin(x)

# Train the model
model.fit(x, y, epochs=1000, verbose=1)

# Test the model on new data (e.g., extrapolation)
x_test = np.linspace(0, 20, 2000)
y_pred = model.predict(x_test)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Ground Truth (Sine Wave)")
plt.plot(x_test, y_pred, label="SIREN Model Prediction", linestyle='--')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("SIREN Neural Network")
plt.show()