from bs4 import BeautifulSoup
from pip._vendor import requests
from pprint import pprint
import json

arr = []

def find_articles(i):
    genres = 'csgo, mobileesports, esports, dota2'
    if i in genres:
        find_articles_afk_gaming(i)
        if i == 'dota2':
            find_articles_one_esports(i)
            i = 'dota-2'
            find_articles_estnn(i)
        if i == 'csgo':
            i = 'counter-strike'
            find_articles_estnn(i)
    else:
        find_articles_estnn(i)
        find_articles_one_esports(i) 
    
def store_data_in_array(game_name,title,image_url,article_url):
    pyt_obj = {"Game_name":None,"Title":None,"Image_Url":None,"Article_Url":None}
    pyt_obj['Game_name'] = game_name
    pyt_obj['Title'] = title
    pyt_obj['Image_Url'] = image_url
    pyt_obj['Article_Url'] = article_url
    arr.append(pyt_obj)

def find_articles_afk_gaming(i):
    html_text = requests.get(f'https://afkgaming.com/{i}').text
    soup = BeautifulSoup(html_text,'lxml')
    news = soup.find_all('div',class_='card-border _3LEm9 _2SX5L')
    for new in news:
        posted_date = new.find('div',class_="_1ma2y").text.split()[-2]
        type_of_content = new.find_all('a',class_='WUZu8')[1].text
        if posted_time == posted_date:
            if 'News' in type_of_content:
                image_url = new.find('figure',class_='_2wf_Q _1Tlx_').img['data-src']
                game_name = new.find('a',class_='WUZu8').text
                article_title = new.find('div',class_='_2er0y').h2.text
                article_url = new.find('a',class_='card-container')['href']
                store_data_in_array(game_name,article_title,image_url,article_url)

def find_articles_one_esports(i):
    html_text = requests.get(f'https://www.oneesports.gg/{i}').text
    soup = BeautifulSoup(html_text,'lxml')
    news = soup.find_all('article',class_='post-card')
    for new in news:
        image_url = new.find('div',class_='image-wrap-16by9').img['src']
        game_name = new.find('a',class_='category').text
        article_title = new.find('h2',class_='title').a.text
        article_url = new.find('h2',class_='title').a['href']
        store_data_in_array(game_name,article_title,image_url,article_url)

def find_articles_estnn(i):
    html_text = requests.get(f'https://estnn.com/tag/{i}').text
    soup = BeautifulSoup(html_text,'lxml')
    news = soup.find_all('article',class_='elementor-post')
    temp = 1
    for new in news:
        if temp <= 5:
            image_url = new.find('img',class_='attachment-thumbnail size-thumbnail')['src']
            game_name = i.title()
            article_title = new.find('h3',class_='elementor-post__title').a.text.strip()
            article_title.replace('\n','')
            article_url = new.find('h3',class_='elementor-post__title').a['href']
            store_data_in_array(game_name,article_title,image_url,article_url)
        temp+=1

def main_method():
    print('Enter any of the given Genre (csgo, mobileesports, esports, gaming, mobile-legends, valorant)')
    genre = input('>').lower().split(',')
    print('Enter posted_time for ex :- (hour ,hours ,day ,days).')
    global posted_time
    posted_time = input('>')
    print(f'Searching for {genre} News...')
    for i in genre:  
        if i == 'csgo' or 'counter_strike':
            find_articles(i)
        elif i == 'mobileesports':
            find_articles(i)
        elif i == 'esports':
            find_articles(i)
        elif i == 'gaming':
            find_articles(i)
        elif i == 'mobile-legends':
            find_articles(i)
        elif i == 'cod' or 'call-of-duty':
            find_articles(i)
        elif i == 'culture':
            find_articles(i)
        elif i == 'wild-rift':
            find_articles(i)
        elif i == 'fortnite' or 'fortnite-esports':
            find_articles(i)
        elif i == 'lol' or 'league-of-legends':
            find_articles(i)
        elif i == 'dota2' or 'dota-2':
            find_articles(i)
    pprint(arr)
    json_data = json.dumps(arr)
    return json_data

main_method()



# def find_articles_win_gg(i):
#     html_text = requests.get(f'https://win.gg/{i}').text
#     soup = BeautifulSoup(html_text,'lxml')
#     news = soup.find_all('div',class_='ant-col ant-col-sm-12 ant-col-md-24 ant-col-lg-24')
#     print(news)

# def find_articles_dot_esports(i):
#     html_text = requests.get(f'https://dotesports.com/{i}').text
#     soup = BeautifulSoup(html_text,'lxml')
#     news = soup.find_all('article',class_='list-item post-423981 post type-post status-publish format-standard has-post-thumbnail hentry category-counter-strike article_type-news pmpro-has-access')
#     for new in news:
#         image_url = new.find('img',class_='attachment-medium_large size-medium_large wp-post-image')['src']
#         game_name = new.find('ul',class_='post-categories').li.a.text
#         article_title = new.find('h3',class_='entry-title').a.text
#         article_url = new.find('a',class_='post-thumbnail')['href']
#         store_data_in_array(game_name,article_title,image_url,article_url)