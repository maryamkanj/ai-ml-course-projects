# Aladdin Face Recognition System

A facial recognition system that identifies characters from Aladdin and implements access control using computer vision techniques.

## What This Project Does

This system uses face recognition to identify characters from the Aladdin movie and grants or denies access based on their identity. It can recognize Aladdin, Jasmine, Genie, and Jafar, with Jafar being specifically blocked from access.

## Technologies Used

- **MTCNN**: For face detection and extraction from images
- **FaceNet (Inception ResNet V1)**: Pre-trained model for generating 128-dimensional face embeddings
- **TensorFlow/Keras**: Deep learning framework
- **NumPy & PIL**: For image processing and array manipulation
- **Matplotlib**: For visualizing extracted faces

## How It Works

1. **Face Detection**: MTCNN detects and extracts faces from input images
2. **Face Processing**: Faces are resized to 160x160 pixels for FaceNet compatibility
3. **Feature Extraction**: FaceNet generates unique embeddings for each face
4. **Database Creation**: Stores embeddings of known characters (Aladdin cast)
5. **Recognition**: Compares new faces against database using L2 distance
6. **Access Control**: Grants access to approved characters, denies access to banned ones

## Code Structure

The main components include:
- `load_facenet()`: Loads the pre-trained FaceNet model
- `extract_image()`: Extracts faces using MTCNN detector
- `load_dataset()`: Loads training images from directory structure
- `extract_embedding()`: Generates face embeddings using FaceNet
- `who_is_it()`: Main recognition and access control function

## Access Policy
- ✅ **Aladdin**, **Jasmine**, **Genie**: Access granted
- ❌ **Jafar**: Access denied (security threat)
- ❌ **Unknown persons**: Not recognized

## Requirements
- TensorFlow
- mtcnn
- keras-facenet
- Pillow
- NumPy
- Matplotlib

## Usage
Run the Jupyter notebook to see the system recognize Aladdin characters and enforce access control policies.
