import requests
from bs4 import BeautifulSoup

def crawl_page():
    #Available urls
    urls = ['https://www.tovima.gr/category/politics','https://www.tovima.gr/category/world/','https://www.tovima.gr/category/sports/','https://www.tovima.gr/category/culture/']
    #Types of articles
    content = ['politics','global','economy','sports','culture']
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
        #Find the article element
        div_containter = soup.find('div',{'id':'full-article-list'})
        ul = div_containter.find('ul')
        #Loop through all articles
        for article in ul.find_all('li'):
            #Title and url
            info = article.find('a',{'href':True})
            link = info['href']
            title = info['title']
            #Image
            image_element = article.find('div',{'class':'absimage'})
            image = image_element['style'].split('(')[1].split(')')[0]
            #Summary
            sum_span = article.find('span',{'class':'normal-desc'})
            summary = sum_span.text
            #Time
            time_elem = article.find('span',{'class':'grey-c'})
            time = time_elem.text[2:]
            #Complete data
            article_data = {
                'site':'tovima',
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