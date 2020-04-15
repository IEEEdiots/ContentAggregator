import requests
from bs4 import BeautifulSoup

def crawl_page():
    #Available urls
    urls = ['https://www.news247.gr/politiki/','https://www.news247.gr/koinonia/','https://www.news247.gr/oikonomia/','https://www.news247.gr/kosmos/']
    #Types of artiles
    content = ['politics','society','economy','global']
    #Adding headers
    headers = {
        'User-agent':'Mozilla/5.0'
    }
    #Complete list of article data
    data_list = list()
    #For given urls
    for index,url in enumerate(urls):
        #User report
        print(f'---- Scrapping from url:{url}')
        #Get page response
        response = requests.get(url, headers=headers)
        #Parse the page 
        soup = BeautifulSoup(response.content,'html.parser')
        articles = soup.find_all('article')
        #Loop through all articles
        for article in articles:
            if article.find('figure') is None:
                continue
            #Title and url
            info = article.find('a',{'class':'article__image'})
            title = info['title']
            link = info['href']
            #Image
            image_element = info.find('img')
            image = image_element['src']
            #Summary
            try:
                summary_p = article.find('p')
                summary = summary_p.text
            except AttributeError:
                continue
            time_element = article.find('time')
            time = time_element['datetime']
            #Complete data
            article_data = {
                'type':content[index],
                'title':title,
                'link':link,
                'image':image,
                'summary':summary,
                'time':time
            }
            #Add the article data to the complete list
            data_list.append(article_data)
    print(len(data_list))

if __name__ == '__main__':
    crawl_page()