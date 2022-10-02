import requests
from bs4 import BeautifulSoup
import string
import os.path

def save_article(the_article_type, cwd,url):
    # url = "https://www.nature.com/nature/articles"
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        title_news = []
        puncs = string.punctuation
        for x in soup.find_all('article'):
            # article_type = x.find('span', attrs={'data-test': 'article.type'}).text
            article_type = x.find("span", "c-meta__type").text
            # <span class="c-meta__type">Research Summary</span>
            # print(article_type)
            # if article_type == f'\n{article_type}\n':
            if article_type == the_article_type:
                # print('article_type == the_article_type')
                title = x.find('a', {'data-track-action': "view article"}).text
                aurl = x.find("a").get("href")
                name = title.strip(' ').translate(str.maketrans(" ", "_", puncs)) + '.txt'
                print(name)
                title_news.append(name)
                # article_url = f"https://www.nature.com{x.a.get('href')}"
                # print(article_url)
                r2 = requests.get(f"https://www.nature.com{aurl}")
                soup2 = BeautifulSoup(r2.content, 'html.parser')
                text = soup2.find('div', class_="c-article-body u-clearfix").text.strip()
                # print(text)
                # with open(name, 'w') as file:
                #   file.write(text)
                print('cwd', cwd)
                print('real cwd', os.getcwd())
                # os.chdir(cwd) if os.getcwd() != cwd else print('no')
                print('changed dir')
                file = open(name, 'wb')
                file.write(text.strip().encode('utf-8'))
                file.close()
                # with open(name, "r", encoding="UTF-8") as file:
                #     file.write(text.strip().encode('utf-8'))
            else:
                continue


def save_articles():
    pages = int(input())
    _type = input()
    for x in range(pages):
        print(x)
        cwd = f'Page_{x + 1}'
        print(cwd)
        url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={x + 1}'
        print(url)
        # os.mkdir(cwd)
        # os.chdir(cwd)
        os.mkdir(f'C:/Users/maciej.baginski/Desktop/Podyplomowe Big Data/Web Scraper/Web Scraper/task/{cwd}')
        os.chdir(f'C:/Users/maciej.baginski/Desktop/Podyplomowe Big Data/Web Scraper/Web Scraper/task/{cwd}')
        save_article(_type, cwd, url)


save_articles()