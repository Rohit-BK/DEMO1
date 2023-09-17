import langdetect

def detect_language(text):
    return langdetect.detect(text)

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
        language = detect_language(content)

        print(f"Title: {title}")
        print(f"Content: {content}")
        print(f"Language: {language}")
        print()
