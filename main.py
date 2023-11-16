import json, os, csv

#import scripts
from scripts.collect_us_sources import collect_us_sources
from scripts.collect_us_taylor_swift_sources import collect_taylor_swift_sources
from scripts.collect_taylor_swift_articles import collect_taylor_swift_articles

#API_KEY = '3389f02aebef4ae7b1bcbd8715728e93'
#API_KEY = '6bd5e85171254b97aa4dc413d4200bb4'
API_KEY = 'a97cf19abea3413f9c2657e4f19a8721'

def filter_unique_titles(articles):
    unique_titles = set()
    unique_articles = []

    for article in articles:
        title = article['title']
        if title not in unique_titles:
            unique_titles.add(title)
            unique_articles.append(article)

    return unique_articles

def revised_articles():

    path = os.path.join(os.getcwd(), "data")
    with open ('{}/taylor_swift_articles.json'.format(path), 'r') as infile:
        data = json.load(infile)
    
    filtered_articles = filter_unique_titles(data)

    # output into csv file with only title and description cols
    with open ('filtered_articles.csv', 'w') as outfile:

        writer = csv.writer(outfile)
        writer.writerow(['Title', 'Description', 'Coding'])
        
        for article in filtered_articles:
            title = article.get("title")
            description = article.get("description")
            writer.writerow([title, description])
    
if __name__ == "__main__":
    #collect_us_sources(API_KEY=API_KEY)
    #collect_taylor_swift_sources(API_KEY=API_KEY)
    #collect_taylor_swift_articles(API_KEY=API_KEY)
    revised_articles()