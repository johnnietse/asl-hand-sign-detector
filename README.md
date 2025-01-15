# American Sign Language Hand Sign Detection App

This project is an **American Sign Language (ASL) Hand Sign Detection App** that leverages computer vision and machine learning to recognize hand signs and classify them into corresponding ASL letters. The app uses a webcam for real-time detection and classification of hand gestures, displaying the recognized sign on screen.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Overview
The app consists of the following components:
- **Data Collection**: Collects images of hand signs for training the model.
- **Training**: Uses the collected images to train a machine learning model for gesture recognition.
- **Prediction**: Uses the trained model to predict ASL signs in real-time using a webcam.

The main files involved are:
- `dataCollection.py`: Captures hand gesture images for training.
- `test.py`: Classifies hand gestures in real-time using the trained model.
- `app.py`: A GUI interface built with Tkinter for controlling the hand sign detection process.

## Features
- **Real-Time Hand Sign Detection**: Classify ASL hand signs in real-time using a webcam.
- **Data Collection**: Collect images of hand signs for training a classification model.
- **ASL Letter Prediction**: Recognize and display the ASL letter corresponding to the detected hand gesture.
- **Tkinter GUI**: A simple interface with buttons to start and stop the hand sign detection process.

## Installation

Follow these steps to set up the project locally.

### Prerequisites
- Python 3.x
- OpenCV
- cvzone (for hand tracking and classification)
- Keras (for machine learning model)

### Steps to Install
1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/american-sign-language-hand-sign-detection-app.git
   cd american-sign-language-hand-sign-detection-app

2. **Create a virtual environment if you want to**
   
   ```bash
   python -m venv venv


3. **Activate the virtual environment**

  On Windows:
   ```bash
   venv\Scripts\activate
   ```

  On macOS or Linux:
   ```bash
   source venv/bin/activate
  
4. **Install dependencies**

  ```bash
  pip install -r requirements.txt









