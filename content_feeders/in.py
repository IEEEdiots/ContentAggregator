import requests
from bs4 import BeautifulSoup
#Available urls
urls = ['https://www.in.gr/greece/','https://www.in.gr/greece/page/2','https://www.in.gr/greece/page/3']
#Adding headers 
headers = {
    'User-agent':'Mozilla/5.0'
}
#Complete list of article data
data_list = list()
#For given urls
for url in urls:
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
        image_div = info.find('div')
        image = image_div['data-src']
        #Summary
        sum_span = article.find('span',{'class':'article-dd'})
        summary = sum_span.text
        #Time
        time_elem = article.find('time')
        time = time_elem['title']
        #Complete data
        article_data = {
            'title':title,
            'link':link,
            'image':image,
            'summary':summary,
            'time':time
        }
        #Add the article data to the complete list
        data_list.append(article_data)
print(len(data_list))