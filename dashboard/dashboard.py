import pandas as pd

from text_analysis.sentiment_analysis import analyze_sentiment

def display_dashboard(news_articles):
    df = pd.DataFrame(news_articles)
    df['tonality'] = df['content'].apply(analyze_sentiment)
    df['department'] = df['content'].apply(extract_department)

    print("Dashboard")
    print("---------")
    print(df)

def extract_department(text):
    # Replace this with the actual code to extract department names from the text
    department = "Unknown"
    return department

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

    display_dashboard(news_articles)
