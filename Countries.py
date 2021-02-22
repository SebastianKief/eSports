from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import pandas as pd

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.esportsearnings.com/countries"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()


###Countrynames
Countrynames = []
containers = page_soup.find_all("td", {"class":"format_cell detail_list_player"})
for container in containers:
    Country = container.select("a")[1].get_text(strip=True)
    Countrynames.append(Country)

###Prizemoney & players
PrizePlayers = []
Players = []
Prizemoney = []
containers = page_soup.find_all("td", {"class":"format_cell detail_list_prize"})
for container in containers:
    PrizeAndPlayers = container.text
    PrizePlayers.append(PrizeAndPlayers)

Players.extend(PrizePlayers[1::2])
Prizemoney.extend(PrizePlayers[::2])

final=[]

for Countrynames, Prizemoney, Players in zip(Countrynames, Prizemoney, Players):
    final.append({"Countrynames":Countrynames, "Prizemoney":Prizemoney,"Players":Players})

###Add final array to dataframe
df = pd.DataFrame(final)

###Formatting
df['Prizemoney'] = df['Prizemoney'].str.replace('$', '')
df['Players'] = df['Players'].str.replace('Player', '')
df['Players'] = df['Players'].str.replace('s', '')

###To Numeric
df["Players"] = pd.to_numeric(df["Players"])


df.to_excel("output.xlsx", index=False)








