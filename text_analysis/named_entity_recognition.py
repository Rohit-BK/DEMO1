import spacy

def extract_named_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    named_entities = []

    for entity in doc.ents:
        named_entities.append({
            'text': entity.text,
            'label': entity.label_
        })

    return named_entities

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
        named_entities = extract_named_entities(content)

        print(f"Title: {title}")
        print("Named Entities:")
        for entity in named_entities:
            print(f"Text: {entity['text']}, Label: {entity['label']}")
        print()
