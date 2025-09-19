import pandas as pd
##get data from file
df = pd.read_csv('car_sales_data.csv')

#print(df.head())

#average price of cars 
df['Car'] = df['Manufacturer'] + " " + df['Model'] + " " + df['Price'].astype(str)
averagecars = df['Car'].value_counts().head(3)
print(averagecars)
#get average