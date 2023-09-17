import googletrans

def translate_text(text, target_language):
    translator = googletrans.Translator()
    translated_text = translator.translate(text, dest=target_language).text # type: ignore
    return translated_text

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

    target_languages = ['en', 'hi', 'ur']

    for article in news_articles:
        title = article['title']
        content = article['content']
        translations = {}

        for language in target_languages:
            translated_text = translate_text(content, language)
            translations[language] = translated_text

        print(f"Title: {title}")
        print(f"Content: {content}")
        print("Translations:")
        for language, translation in translations.items():
            print(f"{language}: {translation}")
        print()
