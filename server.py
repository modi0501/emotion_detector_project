from flask import Flask
from flask import request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():

    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    response = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"{response}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return "Emotion Detector App Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)