# Emotion Detector Project

## Overview
This project is a Flask-based web application developed for the IBM Emotion Detector assignment.

The application analyzes text input and returns emotion-related scores along with the dominant emotion.

## Features
- Emotion detection
- Dominant emotion identification
- Flask web deployment
- Error handling for blank inputs
- Unit testing
- Static code analysis

## Technologies Used
- Python
- Flask
- unittest
- pylint

## Project Structure

emotion-detector-project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── server.py
├── test_emotion_detection.py
├── README.md

## Running the Application

Install dependencies:

pip install flask pylint

Run the application:

python server.py

Open in browser:

http://127.0.0.1:5000/emotionDetector?textToAnalyze=I am happy

## Running Unit Tests

python test_emotion_detection.py

## Running Static Code Analysis

pylint server.py