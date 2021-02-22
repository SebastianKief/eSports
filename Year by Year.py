from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import pandas as pd

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.esportsearnings.com/history/2012/countries"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

###Year
Year = page_soup.find("h2", {"class":"detail_box_title"})
Year = Year.text

Year =Year[-4:]

###All totals from upper table
AllTotals = []
containers = page_soup.find_all("span", {"class":"format_cell detail_list_prize"})
for container in containers:
        Totals = container.text
        AllTotals.append(Totals)

x = AllTotals[:7]
TotalPrizeMoney = x[0]
TotalTournaments = x[1]
TotalActivePlayers = x[2]
MeanTournamentPrizePool = x[3]
MeanEarningsPlayer = x[4]
MedianTournamentPrizePool = x[5]
MedianEarningsPlayer = x[6]

all = []
all.append({"TotalPrizeMoney": TotalPrizeMoney, "TotalTournaments": TotalTournaments, "TotalActivePlayers": TotalActivePlayers, "MeanTournamentPrizePool":MeanTournamentPrizePool, "MeanEarningsPlayer":MeanEarningsPlayer, "MedianTournamentPrizePool":MedianTournamentPrizePool, "MedianEarningsPlayer":MedianEarningsPlayer })

df = pd.DataFrame(all)
df.insert(0, "Year", Year)


df.to_excel("YearByYear.xlsx", index=False)



###Country
Countries = []
containers = page_soup.find_all("td", {"class":"format_cell detail_list_player"})
for container in containers:
    Country = container.text
    Countries.append(Country)

###Prizemoney and Players by year
PrizemoneyYearAndPlayersYear = []
PrizemoneyYear = []
PlayersYear = []

containers = page_soup.find_all("td", {"class":"format_cell detail_list_prize"})
for container in containers:
    PrizemoneyYearAndPlayersYears = container.text
    PrizemoneyYearAndPlayersYear.append(PrizemoneyYearAndPlayersYears)

PrizemoneyYear.extend(PrizemoneyYearAndPlayersYear[::2])
PlayersYear.extend(PrizemoneyYearAndPlayersYear[1::2])







print(TotalPrizeMoney)





