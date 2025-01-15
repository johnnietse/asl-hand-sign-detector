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
- keras (for machine learning model) -> but it should already be included in the Tensorflow dependency.

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

If you don't have the trained model, you can train it using the data collected by the dataCollection.py script. I would recommend using the "https://teachablemachine.withgoogle.com" website to train your model. The website should generate the trained model and labels as these two files: keras_model.h5 and labels.txt. Then, you will have to import these two files into the Model/ folder within the project to get the project to run correctly.

### How to Train the Model Using Teachable Machine

This guide will walk you through training a machine learning model for American Sign Language (ASL) hand sign detection using **Google Teachable Machine**.

#### Step-by-Step Instructions

##### 1. Start a New Project
1. Go to [Teachable Machine](https://teachablemachine.withgoogle.com/).
2. Select the **Image Project** option.
3. Choose the **Standard Image Model** option.

##### 2. Configure Classes
1. Rename the classes as alphabets from **A to Z**.
2. You can add additional classes if desired.
3. For each class, upload the images you collected using the `dataCollection.py` file.

##### 3. Train the Model
1. Once all your images are uploaded, proceed to the next step.
2. Click the **Train Model** button.
3. Wait for the training process to complete. This may take some time depending on the amount of data.

##### 4. Export the Model
1. Turn the input **Off** for the webcam.
2. Click the **Export Model** button.
3. For the export options:
   - Select **TensorFlow**.
   - Choose **Keras** as the model conversion type.
4. Download the resulting zip file.

##### 5. Extract the Model Files
1. The downloaded zip file contains two important files:
   - **`labels.txt`**: A file containing the class labels (e.g., A, B, C, ... Z).
   - **`keras_model.h5`**: The trained Keras model for ASL hand sign detection.

##### 6. Integrate with Your Project
1. Place the extracted files in your project directory:

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





