import time
import requests
import json
import xlwt
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient as BAC


#Client ID and Secret acquired through PGA Website
client_id = r'id'
client_secret = r'secret'

#Create Backend App Client for OAuth
client = BAC(client_id=client_id)
oauth = OAuth2Session(client=client)
#Generate Token from PGA Tour API
myToken = oauth.fetch_token(token_url='url', client_id=client_id, client_secret=client_secret)

#Parse through to eliminate unneccesary data
s = str(myToken)
pieces = s.split(',')
piece = pieces[0].split('\'')
token = piece[3]
print(token) #print token for test purposes, remove later

#Request leaderboard data from pgatour link using a point in time example
myUrl = 'PointInTimeURL'
result = requests.get(myUrl, headers={'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(token)})

#Convert request data into json data
data = result.json()

#Get all values from leaderboard section
leaderboard = []
for key in data[0]:
    if key == 'leaderboard':
        leaderboard = data[0].get(key)

#Parse through data until a readable format is attained
values = []
for key in leaderboard:
    values.append(key)
players = []
for key in values:
    players.append(key)

keys = ['p_id', 'name', 'first_name', 'last_name', 'amateur', 'country',
'status', 'GrpNum', 'feat_grp', 'start_hole', 'tee_time', 'position',
'total', 'round_score', 'thru', 'movement', 'maxrnd', 'courseacronym', 'course_id']

print("Creating Excel Sheet...")
book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

i = 0
for k in keys:
    sheet1.write(0, i, k)
    i = i+1

i = 1
j = 0
for s in players:
    j = 0
    for k in keys:
        sheet1.write(i, j, s[k])
        j = j+1
    i = i+1
book.save("PGAData.xls")
print("Excel Sheet Successfully created.")
#Wait 60 seconds so the program does not overload the server
print("waiting...")
time.sleep(60)
print("done")
