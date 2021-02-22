from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

chrome_path = r"C:\Users\Sebas\PycharmProjects\eSports\venv\chromedriver_win32\chromedriver.exe"

url = ["https://www.esportsearnings.com/games/231-dota-2/countries",
       "https://www.esportsearnings.com/games/245-counter-strike-global-offensive/countries"

       ]

dfall = []


for url in url:

    browser = webdriver.Chrome(chrome_path, options=chrome_options)
    browser.set_window_size(3840, 6000, browser.window_handles[0])
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    browser.close()
    ###Pandas - Get Table
    dfs = pd.read_html(html)
    df = dfs[0]

    ###BeautifulSoup - Get name of the game
    soup = BeautifulSoup(html, "html.parser")
    gameName = soup.find("h1", {"class":"info_box_title"}).text
    df.insert(0, "GameName", gameName)
    dfall.append(df)

dfall = pd.concat(dfall)

dfall.columns = ["GameName", "Rank", "Country", "PrizeMoneyInDollar", "NumberOfPlayers"]
dfall.drop(["Rank"], axis=1, inplace=True)


dfall["PrizeMoneyInDollar"] = dfall["PrizeMoneyInDollar"].str.replace("$", "")
dfall["PrizeMoneyInDollar"] = dfall["PrizeMoneyInDollar"].str.replace(",", "")
dfall["NumberOfPlayers"] = dfall["NumberOfPlayers"].str.replace("Player", "")
dfall["NumberOfPlayers"] = dfall["NumberOfPlayers"].str.replace("s", "")

dfall.to_excel("gamesNames.xlsx", index=False)






