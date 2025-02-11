# Justin's code for Final Project IBM
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the home page (index.html)."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    """
    Process the input text using the emotion_detector function and return formatted response.
    
    Example:
        http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20my%20life
    """
    # Retrieve the text from the query parameter "textToAnalyze"
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "Error: 'textToAnalyze' parameter is missing. Please provide the text to analyze.", 400

    # Process the text to determine emotions
    response = emotion_detector(text_to_analyze)

    # If the dominant emotion is None, return an 400 error message
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    # Format the output as required by the customer
    formatted_response = (
        f"\n For the given statement, the system response is \n"
        f"'anger': {response['anger']}, \n"
        f"'disgust': {response['disgust']}, \n"
        f"'fear': {response['fear']}, \n"
        f"'joy': {response['joy']} and \n"
        f"'sadness': {response['sadness']}. \n"
        f"The dominant emotion is {response['dominant_emotion']}.\n \n"
    )

    return formatted_response

if __name__ == "__main__":
    # Deploy on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)