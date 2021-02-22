import pandas as pd



allUrls = []

GameCodes = ["371-heroes-of-the-storm", "231-dota-2"]

for GameCodes in GameCodes:
    players = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players"
    playersx100 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x100"
    playersx200 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x200"
    playersx300 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x300"
    playersx400 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x400"
    allUrls.extend([players,playersx100,playersx200,playersx300,playersx400])



print(allUrls)



