import json
import os
import mysql.connector
import steam.webapi
from mysql.connector import errorcode
from steam.webapi import WebAPI

from dotenv import load_dotenv

load_dotenv()
STEAM_API_KEY = os.getenv('STEAM_API_KEY')
SQL_USER=os.getenv('SQL_USER')
SQL_PASSWORD=os.getenv('SQL_PASSWORD')
SQL_HOST=os.getenv('SQL_HOST')
SQL_DB=os.getenv('SQL_DB')

print(SQL_USER, SQL_HOST, SQL_DB, SQL_PASSWORD)

class friends:
    def __init__(self,id, name, steamID, discordID, epicID, eaID, rockstarID, playstationID, xboxID):
        self.id = id
        self.name = name
        self.steamID = steamID
        self.discordID = discordID
        self.epicID = epicID
        self.eaID = eaID
        self.rockstarID = rockstarID
        self.playstationID = playstationID
        self.xboxID = xboxID

friendsList = []
config = {
  'user': SQL_USER,
  'password': SQL_PASSWORD,
  'host': SQL_HOST,
  'database': SQL_DB,
  'raise_on_warnings': True
}

try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  query = "SELECT * FROM friends"
  cursor.execute(query)
  for (id, name, steamID, discordID, epicID, eaID, rockstarID, playstationID, xboxID) in cursor:
      friendsList.append(friends(id, name, steamID, discordID, epicID, eaID, rockstarID, playstationID, xboxID))
      cursor.close()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

greg = friendsList[0]

api = steam.webapi.WebAPI(key=STEAM_API_KEY,
                          format='json',
                          raw='false',
                          https=True,
                          http_timeout=30,
                          apihost='api.steampowered.com',
                          auto_load_interfaces=True
                          )

getOwnedGamesParams = {
    "key": str(STEAM_API_KEY),
    "steamid": str(greg.steamID)
}

response = steam.webapi.get(interface='IPlayerService',
                            method='GetOwnedGames',
                            version='0001',
                            apihost='api.steampowered.com',
                            https=True,
                            params=getOwnedGamesParams
                            )

responsJson = json.dumps(response, indent=4)
responseLoad = json.load(response)

#STEAM_API_KEY + "&steamid=" + str(greg.steamID) + "&format=json")
#response = api.call('', vanityurl="", url_type=2)
print(responsJson)




gamesList = sorted(responsJson,key=games)

print(gamesList)
#print(responsJson)





# friendGameLists = []
#
# for obj in friendsList:
#     response = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + STEAM_API_KEY + "&steamid=" + str(obj.steamID) + "&format=json")
#     print(response.text)
#     #data = json.load(response.text)
#     print(response.text['games'])
#     friendGameLists.append(response.json())
#     print(obj.name)
#
#
# for game in friendGameLists:
#     g




#print(response.text)