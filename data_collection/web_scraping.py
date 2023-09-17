
import requests
from bs4 import BeautifulSoup

def scrape_news_articles():
    regional_media_websites = [
        "https://example1.com",
        "https://example2.com",
        # Add more regional media websites here
    ]

    news_articles = []

    for website in regional_media_websites:
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            title = article.find('h2').text.strip()
            content = article.find('div', class_='content').text.strip()

            news_articles.append({
                'title': title,
                'content': content,
                'website': website
            })

    return news_articles

if __name__ == "__main__":
    news_articles = scrape_news_articles()
    for article in news_articles:
        print(article['title'])
        print(article['content'])
        print(article['website'])
        print()

