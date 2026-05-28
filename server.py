"""Flask server for Emotion Detector application."""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze emotions from user input."""

    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    response = emotion_detector(text_to_analyze)

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render home page."""

    return "Emotion Detector App Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)