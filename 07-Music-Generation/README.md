# Music Generator

## Overview
This project is a Bach music generator that uses deep learning to create chorales in the style of Bach. It allows users to generate music without needing to know how to play instruments or compose music.

## What We Did
- Downloaded and extracted a dataset of Bach chorales automatically.
- Preprocessed the chorales into sequences of notes suitable for training a neural network.
- Built a neural network with embedding, convolutional, and LSTM layers to learn musical patterns.
- Implemented a synthesizer to play generated chorales as audio.
- Trained the model to generate new Bach-style chorales from seed notes.

The purpose of this project is to explore how deep learning can be applied to creative tasks like music generation. It demonstrates sequence modeling, preprocessing of structured musical data, and neural network design for generative tasks.

## Features
- Automatic dataset download and extraction
- Preprocessing of chorales into sequences of notes
- Audio playback of generated music
- Deep learning model training for music generation
- Generation of new chorales based on seed notes

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/maryamkanj/ai-ml-course-projects.git
    cd 07-Music-Generation
    ```

2. Install required Python packages:
    ```bash
    pip install tensorflow numpy pandas scipy pretty_midi
    ```

3. Run the notebook or Python script:
    - Open `music_generator.ipynb` in PyCharm or Jupyter Notebook.
    - The notebook will automatically download and extract the Bach chorales dataset.
    - Run all cells to train the model and generate music.

4. Generated chorales can be played directly or saved as WAV/MIDI files.
