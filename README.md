# American Sign Language Hand Sign Detection App

This project is an **American Sign Language (ASL) Hand Sign Detection App** that leverages computer vision and machine learning to recognize hand signs and classify them into corresponding ASL letters. The app uses a webcam for real-time detection and classification of hand gestures, displaying the recognized sign on screen.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

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

### Dependencies

This project requires the following Python packages:

- cv2 (OpenCV)
- cvzone (for hand tracking and classification)
- numpy
- tensorflow (for the Keras model)
- tkinter
- matplotlib
- keras (for machine learning model) -> but it should be already included in the Tensorflow dependency.

These dependencies should be listed in the requirements.txt file, and you can install them using:

  ```bash
  pip install -r requirements.txt
  ```

But first create a requirements.txt file in the project directory and include the necessary dependencies within the .txt file.


### Steps to Install
1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/american-sign-language-hand-sign-detection-app.git
   cd american-sign-language-hand-sign-detection-app

2. **Create a virtual environment if you want to**
   
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

  On Windows:
   ```bash
   venv\Scripts\activate
   ```

  On macOS or Linux:
   ```bash
   source venv/bin/activate
   ```
4. **Download or Train the Model**

If you already have a trained model, place it in the Model/ folder as keras_model.h5, and make sure the corresponding labels.txt file is also there.

If you don't have the trained model, you can train it using the data collected by the dataCollection.py script. The trained model and labels should be saved as keras_model.h5 and labels.txt in the Model/ folder.

I would recommend using the "https://teachablemachine.withgoogle.com" website to train your model.

## Usage 
Run the Tkinter app in order to start the ASL hand sign detection app with the GUI, we will run:

```bash
python app.py
```

For the GUI interface:
- Press the **Start Prediction** button to start detecting hand signs. (PS: You may have to click onto the button several times to get the app started.)
- Press the **Exit** button to terminate the app and close any active windows. (PS: You may actually have to close some of the windows manually by yourself if this doesn't work.)


## File Structure 

The project directory for this project looks like this:

```
american-sign-language-hand-sign-detection-app/
├── app.py                # Main Tkinter GUI application
├── dataCollection.py     # Data collection script for hand signs
├── test.py               # Real-time prediction script
├── Model/                # Folder containing the trained model
│   ├── keras_model.h5    # Trained Keras model for hand sign classification
│   └── labels.txt        # Corresponding labels for ASL letters
├── Data/                 # Folder for storing collected hand sign images
│   └── A-Z/                # Subfolder for 'A' to 'Z' hand sign images
```





