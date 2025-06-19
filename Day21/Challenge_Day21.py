
import requests
from bs4 import BeautifulSoup

html_text_news = requests.get('https://www.indiatoday.in/india').text

soup = BeautifulSoup(html_text_news, 'lxml')

news = soup.find_all('h2')

for index, top_news in enumerate(news, 1):
    headline = top_news.a.text
    link = top_news.a["href"]

    print(f"Headline {index}\n")
    print(f"{headline}\nFor more info: {link} \n")