import requests
from bs4 import BeautifulSoup
import newspaper
from textblob import TextBlob
import threading

def news_sentiment(text):
    analysis = TextBlob(text)
    #print(analysis.detect_language())
    #print(analysis.translate(to="hi"))
    return analysis.sentiment.polarity
def google_news_links(term):
    query = term.split()
    query = "+".join(query)
    url = "https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(query)
    print(url)
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
            print(e)
    return refined_links
def news_extraction_thread(link,pos_news,neg_news,news,config):
    print("----------------------THREAD-------------------------")
    try:
        article_name = newspaper.Article(url=link, config=config, keep_article_html=True)
        article_name.download()
        article_name.parse()
        article_name.nlp()
        text = article_name.text
        polarity = news_sentiment(text)
        news = {"link":link, "headline":article_name.title,"date":article_name.publish_date, "summary":article_name.summary}
        if polarity >= 0:
            pos_news.append(news)
        else:
            neg_news.append(news)
    except Exception as e:
        print(e)
def news_extraction(term):
    links = google_news_links(term)
    n = 0
    pos_news, neg_news, threads = [], [], []
    news = {}
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = newspaper.Config()
    config.browser_user_agent = user_agent
    try:
        for link in links:
            th = threading.Thread(target=news_extraction_thread, daemon=True, args=(link,pos_news,neg_news,news, config))
            threads.append(th)
            th.start()
            # print("Article's Link:--------------------------------")
            # print(link)
            # print("Article's Title:--------------------------------")
            # print(article_name.title)
            # print("Article's Publish Date:--------------------------------")
            # print(article_name.publish_date)
            # print("Article's Summary:--------------------------------")
            # print(article_name.summary)            
            n += 1
            print(n)
            if n>20:
                break
        for i in threads:
            i.join()
    except Exception as e:
        print(e)
    return pos_news, neg_news
#
# news_extraction(term = "Johnnette")
