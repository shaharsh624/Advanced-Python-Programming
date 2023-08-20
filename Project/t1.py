import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Stock Market&'
       'from=2023-07-19&'
       'sortBy=popularity&'
       'apiKey=38b232c038634e84980bfec3ba2ae063')

response = requests.get(url)
print(response.json())