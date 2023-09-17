import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment

if __name__ == "__main__":
    news_articles = [
        {
            'title': 'Example News Article 1',
            'content': 'This is an example news article in English.',
            'website': 'https://example1.com'
        },
        {
            'title': 'उदाहरण समाचार लेख 2',
            'content': 'यह हिंदी में एक उदाहरण समाचार लेख है।',
            'website': 'https://example2.com'
        },
        # Add more news articles here
    ]

    for article in news_articles:
        title = article['title']
        content = article['content']
        sentiment = analyze_sentiment(content)

        print(f"Title: {title}")
        print(f"Content: {content}")
        print(f"Sentiment: {sentiment}")
        print()
