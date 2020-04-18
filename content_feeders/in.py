import requests
from bs4 import BeautifulSoup

def getSummary(link):
    #Get page response
    response = requests.get(link)
    #Parse the pgae
    soup = BeautifulSoup(response.content,'html.parser')
    #Find first paragraph
    summary_p = soup.find('p')
    #Get the first text
    summary = summary_p.text[:40] + ' ...'
    #Return the text
    return summary

def crawl_page():
    #Available urls
    urls = ['https://www.in.gr/world/','https://www.in.gr/politics/','https://www.in.gr/economy/','https://www.in.gr/sports/','https://www.in.gr/culture/','https://www.in.gr/entertainment/','https://www.in.gr/tech/']
    #Types of articles
    content = ['global','politics','economy','sports','culture','entertainment','technology']
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
        articles = soup.find_all('article')
        #Loop through all articles
        for article in articles:
            #Title and url
            info = article.find('a',{'href':True})
            link = info['href']
            title = info['title']
            #Image
            image_element = article.find('div',{'class':'absg'})
            image = image_element['data-src']
            #Summary
            try:
                sum_span = article.find('span',{'class':'article-dd'})
                summary = sum_span.text
            except AttributeError:
                summary = getSummary(link)
            #Time
            time_elem = article.find('time')
            time = time_elem['datetime']
            #Complete data
            article_data = {
                'site':'in',
                'type':content[index],
                'title':title,
                'link':link,
                'image':image,
                'summary':summary,
                'date':time
            }
            #Add the article data to the complete list
            data_list.append(article_data)
    print(len(data_list))

if __name__ == '__main__':
    crawl_page()