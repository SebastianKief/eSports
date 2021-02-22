from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import pandas as pd

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_urls = ["https://www.esportsearnings.com/players",
    "https://www.esportsearnings.com/players/highest-overall-x100",
    "https://www.esportsearnings.com/players/highest-overall-x200",
    "https://www.esportsearnings.com/players/highest-overall-x300",
    "https://www.esportsearnings.com/players/highest-overall-x400"]

all = []

for page_url in page_urls:

    # opens the connection and downloads html page from url
    uClient = uReq(page_url)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    ###Country
    Countries = []
    containers = page_soup.find_all("td", {"class": "format_cell detail_list_player"})
    for container in containers:
        Country = container.find('div', {'class': 'image'})
        Country = container.find("img").get("alt")
       # containers[0].find("img").get("alt")

       # Countries.append(Country)



    ###Nicknames
    PlayernamesAndNicknames = []
    Nicknames = []
    containers = page_soup.find_all("td", {"class":"format_cell detail_list_player"})

    for container in containers:
        Playername = container.text
        PlayernamesAndNicknames.append(Playername)
    Nicknames.extend(PlayernamesAndNicknames[0::2])

    ###Total overall prizemoney
    TotalOverallPrizemoney = []
    containers = page_soup.find_all("td", {"class":"format_cell detail_list_prize border_right"})

    for container in containers:
        PrizeMoney = container.text
        TotalOverallPrizemoney.append(PrizeMoney)

    ###HighestPlayingGame
    HighestPlayingGame = []

    containers = page_soup.find_all("td", {"class":"format_cell detail_list_game border_left"})
    for container in containers:
        Game = container.text
        HighestPlayingGame.append(Game)

    for Countries, Nicknames, TotalOverallPrizemoney, HighestPlayingGame in zip (Countries, Nicknames, TotalOverallPrizemoney, HighestPlayingGame):
        all.append({"Countries":Countries,"Nicknames": Nicknames, "TotalOverallPrizemoney": TotalOverallPrizemoney, "HighestPlayingGame": HighestPlayingGame})


###Add final array to dataframe
df = pd.DataFrame(all)

###Formatting
df['TotalOverallPrizemoney'] = df['TotalOverallPrizemoney'].str.replace('$', '')

df.to_excel("Top500Players.xlsx", index=False)

print(df)


