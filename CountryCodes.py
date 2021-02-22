from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import pandas as pd

dfs = pd.read_html("https://www.iban.com/country-codes")


df = dfs[0]

df.to_excel("CountryCodes.xlsx",index=False, sheet_name="CountryCodes")

