import requests
from bs4 import BeautifulSoup
#import newspaper
#import time
#from textblob import TextBlob


#query = input("enter name to search: ").split()
#term = "+".join(query)

def news_sentiment(text):
    analysis = TextBlob(text)
    #print(analysis.detect_language())
    #print(analysis.translate(to="hi"))
    print("ANALYSING SENTIMENTS...\n", analysis.sentiment)
def google_news_links(term):
    url = "https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(term)
    print(url)
    s, f = 0, 0
    source = requests.get(url)
    soup = BeautifulSoup(source.text,"lxml")
    unrefined_links = soup.find_all('div', {'class':"kCrYT"})
    refined_links = []
    try:      
        for link in unrefined_links:
            a = link.find('a')
            try:
                href = a.get('href')
            except Exception:
                pass
            link = href[7:].strip()
            link = link.split('&sa=U&ved')[0]
            refined_links.append(link)
    except Exception as e:
            f+=1
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@FAILED@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", f)
            print("EXCEPTION", href, "\n", link)
            print(e)
    return refined_links
def news_extraction(links):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = newspaper.Config()
    config.browser_user_agent = user_agent
    try:
        for link in links:
            article_name = newspaper.Article(url=link, config=config)
            article_name.download()
            article_name.parse()
            time.sleep(1)
            article_name.nlp()
            print("#############################SUCCESS##################################", s)
            print("Article's Title:--------------------------------")
            print(article_name.title)
            #print(href, "\n", link)
            text = article_name.text
            news_sentiment(text)
    except Exception as e:
        pass
#print("Success Downloads:", s,"\nFailed Downloads:", f)
#newsapikey#0b08dd648d5e433e801a4a8c2f86fb10