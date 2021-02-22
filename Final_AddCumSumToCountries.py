import pandas as pd
import xlsxwriter

df = pd.read_excel(r"c:\Users\Sebas\PycharmProjects\eSports\venv\Scripts\test2.xlsx", index = False)

### Data cleaning
df['PrizemoneyYear'] = df['PrizemoneyYear'].str.replace(',', '')
df["PrizemoneyYear"] = pd.to_numeric(df["PrizemoneyYear"])
df["Countries"] = df["Countries"].str.lstrip()
df['PlayersYear'] = df['PlayersYear'].str.replace(' Player', '')
df['PlayersYear'] = df['PlayersYear'].str.lstrip()
df['PlayersYear'] = df['PlayersYear'].str.rstrip()
df["PlayersYear"] = pd.to_numeric(df["PlayersYear"])


dfs = {}

for country, df_Countries in df.groupby('Countries'):
    df_Countries = df_Countries.sort_values(by='Years', ascending=True)
    df_Countries["CumSum"] = df_Countries["PrizemoneyYear"].cumsum()
    dfs[country] = df_Countries

column_names = ["PrizemoneyYear", "PlayersYear", "Countries", "Years", "CumSum"]

dfall = pd.DataFrame(columns = column_names)


for key, value in dfs.items():
    df = pd.DataFrame.from_dict(value)
    dfall = df.append(dfall)


dfall.to_excel("dfall.xlsx", index=False)


print(dfall)
print(dfs["Sweden"])













##df["Countries"] = df["Countries"].str.lstrip()


##d = dict(tuple(df.groupby('Countries')))




##print(d["Sweden"])


