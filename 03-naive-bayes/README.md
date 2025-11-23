# Naive Bayes Spam Detector

This project is a practical implementation of a **spam message classifier** using the **Multinomial Naive Bayes** algorithm.
It was built to explore **text preprocessing**, **Bag-of-Words feature extraction**, and training a basic machine learning model for real-world spam detection.

## Project Overview

The goal of this project is to classify SMS and email messages as **spam** or **legitimate** using a small dataset stored in a `.txt` file.
Each line contains a label and a message, separated by a tab.

The workflow includes:

* Loading the dataset from a text file
* Preprocessing messages and encoding labels
* Splitting the data into training and testing sets
* Converting text into numerical features with **CountVectorizer**
* Training a **Multinomial Naive Bayes** model
* Evaluating accuracy and displaying a confusion matrix
* Testing the model on new messages

## Implementation Details

* Read the dataset manually from `spam-data.txt`
* Created a pandas DataFrame containing messages and labels
* Encoded labels (`ham → 0`, `spam → 1`)
* Split the dataset with `train_test_split`
* Converted text into Bag-of-Words features using `CountVectorizer`
* Trained a `MultinomialNB` Naive Bayes classifier
* Calculated accuracy and printed the confusion matrix
* Tested the model on new messages, including **spam and legitimate messages**, such as simulated job offers, scam texts, and normal emails

This project demonstrates how **Naive Bayes can be applied to text classification**, offering a simple, end-to-end workflow for detecting spam messages.
