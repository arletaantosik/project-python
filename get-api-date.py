import requests #HTTP requests

def get_news(topic, from_date, to_date, language='en',
            api_key='890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url) # http request to url
  content = r.json() # from json to dict in py
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

print(get_news(topic='space', from_date='2022-11-25', to_date='2022-11-28')) #run function and print the result
