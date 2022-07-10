import requests
import pandas as pd

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=NMeIHa4ko5sQcPnB0tJI9BvgE7P3oTvj"  #Make sure to change ******* to your API key.
response = requests.get(url)
print(response.json())

dataframe = pd.DataFrame(response.json())
print(dataframe)

# Drop unnescessary columns
dataframe.drop(columns=["success", "timestamp", "base", "date"], inplace=True)
print(dataframe)

# Save the Dataframe
dataframe.to_csv("/home/gustavo/Documents/Working_dir/DataEngineerIBM/Course3/exchange_rates_1.csv")