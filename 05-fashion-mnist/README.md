# Fashion MNIST Classification

A simple deep learning project that classifies images of clothing from the Fashion MNIST dataset into 10 categories.

## Project Overview

This project uses a neural network to predict the type of clothing in grayscale images. The model is trained on the Fashion MNIST dataset and outputs prediction probabilities for each class.

## Dataset

- **Dataset:** Fashion MNIST (available in TensorFlow/Keras datasets)
- **Number of images:** 70,000 (60,000 training, 10,000 testing)
- **Image size:** 28x28 pixels, grayscale
- **Classes (10):** 
  - T-shirt/top
  - Trouser
  - Pullover
  - Dress
  - Coat
  - Sandal
  - Shirt
  - Sneaker
  - Bag
  - Ankle boot

## Libraries Used

- `numpy`
- `matplotlib`
- `opencv-python` (`cv2`)
- `tensorflow` / `keras`
- `pandas`

## Model Architecture

- Input layer: 28x28 images
- Flatten layer
- Dense layer: 128 neurons, ReLU activation
- Output layer: 10 neurons (one per class)
- Optimizer: Adam
- Loss: Categorical Crossentropy
- Metrics: Categorical Accuracy

## Data Preprocessing

- Images are scaled to values between 0 and 1
- Labels are converted to one-hot encoding

## Training

- Epochs: 15
- Validation using the test set
- Training history is plotted to visualize accuracy and loss

## Predictions

- The trained model is saved as `fashion_mnist.h5`
- The model outputs **probabilities for each clothing class** when predicting new images

## How to Use

1. Load the model using TensorFlow/Keras.
2. Preprocess new images (grayscale, resize to 28x28, scale to 0-1).
3. Use the model to get prediction probabilities for each class.
