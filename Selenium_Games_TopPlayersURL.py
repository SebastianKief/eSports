import pandas as pd
import pickle



allUrls = []

#GameCodes = ["371-heroes-of-the-storm", "231-dota-2"]

pickle_in = open("AllGamecodes.pickle","rb")
GameCodes = pickle.load(pickle_in)

for GameCodes in GameCodes:
    players = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players"
    playersx100 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x100"
    playersx200 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x200"
    playersx300 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x300"
    playersx400 = "https://www.esportsearnings.com/games/" + str(GameCodes) + "/top-players-x400"
    allUrls.extend([players,playersx100,playersx200,playersx300,playersx400])

pickle_out = open("AllGameURLsX100-x400.pickle","wb")
pickle.dump(allUrls, pickle_out)
pickle_out.close()

print(allUrls)