# pulls stock names, tickers and industries from wikipedia
import wikipedia
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

spx_wiki_page = wikipedia.page("list of S&P 500 companies")
url = spx_wiki_page.url
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'lxml')
#print(soup.prettify())
stocks_table = soup.find("table",class_="wikitable sortable")
#print(stocks_table)

symbols = []
names = []
sectors = []

for row in stocks_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) ==9:
        symbols.append(cells[0].find(text=True)) # symbols are listed in first column of table
        names.append(cells[1].find(text=True)) # names of companies are listed in second column of table
        sectors.append(cells[4].find(text=True)) # using sub-industry classification, which is listed in the fifth column of the table

# creates dataframe using pandas to store symbol, names, and industries in dataframe table
dataframe = pd.DataFrame(symbols,columns = ["Symbol"])
dataframe["Company"] = names
dataframe["Sector"] = sectors
dataframe

print(dataframe)

## creates dictionary with symbol as key and (name, sector) as value (not sure this is needed if we use dataframe above)
company_dict = {}
for i in range(0,len(symbols)):
    company_dict[symbols[i]] = [names[i],sectors[i]]

#print(company_dict)
