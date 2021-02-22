import requests
import pandas as pd


parameters = [{"offset": 0},
              {"offset": 100},
              {"offset": 200},
              {"offset": 300},
              {"offset": 400},
              {"offset": 500},
              {"offset": 600},
              {"offset": 700},
              {"offset": 800},
              {"offset": 900},
              {"offset": 1000}]

dfall = []

for x in parameters:
    response = requests.get("http://api.esportsearnings.com/v0/LookupHighestEarningPlayers?apikey=f3446cd4234b3d8b098f615a728954e444b77279a77ecf6466a0cb265258e5b9", params=x, timeout=5)
    data = response.json()
    df = pd.DataFrame.from_dict(data)
    dfall.append(df)

dfall = pd.concat(dfall)

dfall.to_excel('HighestEarningsPlayer.xlsx',index=False)


print(dfall)






