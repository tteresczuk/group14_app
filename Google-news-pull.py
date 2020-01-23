# function defined below gets top 10 headlines for inputted string from google news. I think we should use company name (not ticker) as input.
import requests
import urllib.request
from bs4 import BeautifulSoup

## search_company_news takes query as input and returns a dictionary of 10 news results. Key is headline of article and value is url of the article
def search_company_news(query):
    query=query.replace(" ","_")
    google_news_url = "http://news.google.com/search?q="+query
    #print (google_news_url)
    page = urllib.request.urlopen(google_news_url)
    soup = BeautifulSoup (page,'lxml')
    #print (soup.prettify())
    all_results = soup.find_all("article",class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne") # this long class name is the class name for articles on Google News
    all_headlines = soup.find_all("h3",class_="ipQwMb ekueJc RD0gLb") #this class name is where you can find headlines in the html
    #print (all_results)
    
    number_of_articles = 10 # gathers 10 results from Google News
    headline_url_pairing = {}
    for i in range (0,number_of_articles):
        url = "news.google.com/"+all_results[i].find('a').get('href')
        headline = all_headlines[i].find('a',class_="DY5T1d").get_text() 
        headline_url_pairing [headline] = url
               
    return headline_url_pairing
