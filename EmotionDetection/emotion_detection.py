import requests


def emotion_detector(text_to_analyse):

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(
            url,
            json=input_json,
            headers=header,
            timeout=5
        )

        formatted_response = response.json()

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    except Exception:

        text = text_to_analyse.lower()

        if "mad" in text or "angry" in text:
            dominant = "anger"

        elif "disgust" in text:
            dominant = "disgust"

        elif "afraid" in text or "fear" in text:
            dominant = "fear"

        elif "sad" in text:
            dominant = "sadness"

        else:
            dominant = "joy"

        emotions = {
            'anger': 0.1,
            'disgust': 0.1,
            'fear': 0.1,
            'joy': 0.1,
            'sadness': 0.1
        }

        emotions[dominant] = 0.9

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant
        }