from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
import pickle

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

chrome_path = r"C:\Users\Sebas\PycharmProjects\eSports\venv\chromedriver_win32\chromedriver.exe"

#url = ["https://www.esportsearnings.com/games/231-dota-2/top-players"
#      ]

pickle_in = open("AllGameURLsX100-x400.pickle","rb")
url = pickle.load(pickle_in)

dfall = []

for url in url:
    browser = webdriver.Chrome(chrome_path, options=chrome_options)
    browser.set_window_size(3840, 6000, browser.window_handles[0])


    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    browser.close()

    soup = BeautifulSoup(html, "html.parser")

    try:
        Country = [item["alt"] for item in soup.find_all("img", width = {16})]
        PlayerID = [item.find(class_ = "format_cell detail_list_player").text for item in soup.find_all("tr", class_ = "format_row highlight")]
        Playername = [item.find(class_ = "format_cell detail_list_player").next_sibling.text for item in soup.find_all("tr", class_ = "format_row highlight")]
        PrizeMoneyTotalGame = [item.find(class_ = "format_cell detail_list_prize border_right").text for item in soup.find_all("tr", class_ = "format_row highlight")]
        PrizeMoneyTotalOverall = [item.find(class_ = "format_cell detail_list_prize border_left").text for item in soup.find_all("tr", class_ = "format_row highlight")]
        PercentOfTotal = [item.find(class_ = "format_cell detail_list_prize").text for item in soup.find_all("tr", class_ = "format_row highlight")]
        Game = [soup.find("h1", class_ = "info_box_title").text for len in range(len(Country))]
    except:
        print("error")

    all = []

    for Country, PlayerID, Playername, PrizeMoneyTotalGame, PrizeMoneyTotalOverall, PercentOfTotal, Game in zip (Country, PlayerID, Playername, PrizeMoneyTotalGame, PrizeMoneyTotalOverall, PercentOfTotal, Game):
      all.append({"Country":Country, "PlayerID":PlayerID, "Playername":Playername, "PrizeMoneyTotalGame":PrizeMoneyTotalGame, "PrizeMoneyTotalOverall":PrizeMoneyTotalOverall, "PercentOfTotal":PercentOfTotal, "Game":Game})

    df = pd.DataFrame(all)
    dfall.append(df)

dfall = pd.concat(dfall)

dfall["PrizeMoneyTotalGame"] = dfall["PrizeMoneyTotalGame"].str.replace("$", "")
dfall["PrizeMoneyTotalGame"] = dfall["PrizeMoneyTotalGame"].str.replace(",", "")
dfall["PrizeMoneyTotalOverall"] = dfall["PrizeMoneyTotalOverall"].str.replace("$", "")
dfall["PrizeMoneyTotalOverall"] = dfall["PrizeMoneyTotalOverall"].str.replace(",", "")

dfall.to_excel("Top500PlayersPerGame.xlsx", index=False)


print(dfall)

