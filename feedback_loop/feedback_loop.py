
import requests

from text_analysis.sentiment_analysis import analyze_sentiment

def provide_feedback(article_id, feedback):
    # Code to provide feedback on the sentiment of a news article
    # Replace this with the actual implementation

    response = requests.post("https://example.com/feedback", json={
        "article_id": article_id,
        "feedback": feedback
    })

    if response.status_code == 200:
        print("Feedback submitted successfully.")
    else:
        print("Failed to submit feedback.")

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
        feedback = analyze_sentiment(content)

        print(f"Title: {title}")
        print(f"Content: {content}")
        print(f"Feedback: {feedback}")
        print()

        article_id = 123  # Replace with the actual article ID
        provide_feedback(article_id, feedback)

