from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
import pickle

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

chrome_path = r"C:\Users\Sebas\PycharmProjects\eSports\venv\chromedriver_win32\chromedriver.exe"

#url = ["https://www.esportsearnings.com/games/231-dota-2/top-players"]



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
    ###Pandas - Get Table
    try:
        dfs = pd.read_html(html)
        df = dfs[0]
    except:
        print("Error")



    ###BeautifulSoup - Get name of the game
    try:
        soup = BeautifulSoup(html, "html.parser")
        gameName = soup.find("h1", {"class":"info_box_title"}).text
        df.insert(0, "GameName", gameName)
        dfall.append(df)
    except:
        print("Error")

dfall = pd.concat(dfall)

dfall.to_excel("Games_TopPlayers.xlsx", index=False)
print(dfall)