from textblob import TextBlob

def analyze(text: str) -> dict:
    blob = TextBlob(text)
    
    return {
        "subjecivity": blob.sentiment.subjectivity,
        "polarity": blob.sentiment.polarity
        }