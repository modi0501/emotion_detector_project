import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        response = emotion_detector("I am glad this happened")

        self.assertEqual(response['dominant_emotion'], 'joy')

if __name__ == '__main__':
    unittest.main()