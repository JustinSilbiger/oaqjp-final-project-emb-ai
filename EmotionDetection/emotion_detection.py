# Justin's code for Final Project IBM

import requests
import json

def emotion_detector(text_to_analyse):
    """Analyzes text for emotions and returns emotion scores with the dominant emotion.
    
    If the user's input is blank (400 error), the function will return a dictionary with all values set to none.
    """
    
    # API endpoint for emotion detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Prepare request payload
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Set model header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse JSON response
    formatted_response = json.loads(response.text)
    
    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Identify the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    

    # Return structured emotion data
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

# Test function with sample text
result = emotion_detector("I love cookies")
print(result)
