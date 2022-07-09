from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_largest_banks'
html_data  = requests.get(url).text 

print(html_data[101:124])



soup = BeautifulSoup(html_data, 'html5lib')
data = pd.DataFrame(columns=['Name', 'Market Cap (US$ Billion)'])

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    if col:
        bank_name = col[1].find_all("a")[1].text
        market_cap = float(col[2].text)
        data = data.append({'Name': bank_name, 'Market Cap (US$ Bilion)': market_cap}, ignore_index=True)


print(data.header)