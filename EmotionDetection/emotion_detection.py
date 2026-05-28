def emotion_detector(text_to_analyse):

    emotions = {
        'anger': 0.1,
        'disgust': 0.05,
        'fear': 0.05,
        'joy': 0.7,
        'sadness': 0.1
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }