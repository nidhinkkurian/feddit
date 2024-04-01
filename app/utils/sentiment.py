from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity * 100  # Scale polarity score to range [0, 100]
    if polarity_score > 0:
        sentiment_classification = "positive"
    else:
        sentiment_classification = "negative"
    return polarity_score, sentiment_classification
