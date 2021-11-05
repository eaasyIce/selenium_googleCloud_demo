import requests
# params = {'filter[domain]':'https://www.g2.com/products/genesys-dx/reviews'}
params = {'filter[slug]':'genesys-cloud-cx'}

my_headers = {'Content-Type': 'application/vnd.api+json', 'Authorization' : 'Token token=3797f45675b4b9fc7586f9805cd963538695c7b3de6fc15648e8308519a5d87b'}
response = requests.get('https://data.g2.com/api/v1/products', headers=my_headers,params=params) #
r = response.json()
r['data'][0]['attributes']['review_count']
r['data'][0]['attributes']['star_rating']