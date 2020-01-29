import requests
import json

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient as BAC



client_id = r'LnwER6D1cvADWcrXJr2PaH2Wjo8a'
client_secret = r'kB6GKnsJzhxqsBcI5S2jzVyoe9Ua'

client = BAC(client_id=client_id)
oauth = OAuth2Session(client=client)
myToken = oauth.fetch_token(token_url='https://api-test.pgatourhq.com:8243/token', client_id=client_id, client_secret=client_secret)
s = str(myToken)
pieces = s.split(',')
piece = pieces[0].split('\'')
token = piece[3]
print(token)


myUrl = 'https://api-test.pgatourhq.com:8243/SyndLeaderboard/?format=json&T_ID=R2019004&sim&start_pnt_type=R1&start_datetime=12/1/2019&current_datetime=NOW&speed=100'
result = requests.get(myUrl, headers={'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(token)})
data = result.json()
for key, value in data.iteritems():
    print(key, value)
