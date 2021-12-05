import pandas as pd
import numpy as np
from sqlalchemy import create_engine


df = pd.read_csv('CTA_list_of_L_stops.csv')
print(df.columns.tolist())
# find the number of unique stations by MAP_ID.

df2 = df.groupby('MAP_ID')
len(df2.first())
print(df2.first().count()['STOP_ID'])

l_stops_df = pd.read_csv('CTA_list_of_L_stops.csv')
station_bools = l_stops_df[['MAP_ID','ADA','RED','BLUE','G','BRN','P','Pexp','Y','Pnk','O']].groupby('MAP_ID').any()
l_stations_df = l_stops_df[['MAP_ID','STATION_NAME','STATION_DESCRIPTIVE_NAME','Location']] \
    .merge(station_bools, how='left', left_on='MAP_ID', right_index=True).drop_duplicates()
print(l_stations_df)

l_stations_df[['latitude','longitude']] = \
   l_stations_df['Location'].str.replace('\(|\)','',regex=True) \
   .str.split(',', expand=True).apply(pd.to_numeric)
l_stations_df.drop('Location', axis=1, inplace=True)

ridership_df = pd.read_csv('CTA_ridership_daily_totals.csv')
print(ridership_df)

# use the pandas to_sql() method to load the l_stations_df and ridership_df DataFrames into PostgreSQL tables.

engine = create_engine('postgresql://postgres:password@localhost:5432/cta_db')


# with engine.connect() as con:
#     sql = "drop table if exists stations;"
#     con.execute(sql)
#     sql = "drop table if exists ridership;"
#     con.execute(sql)

# l_stations_df.to_sql(name='stations', con=engine, index=False)
# ridership_df.to_sql(name='ridership', con=engine, index=False)

# print(l_stations_df.head())
# print(ridership_df.head())

 #Consider any station with a latitude below 41.881 to be a station on the South side. 
 # Using pandas, calculate the number of total daily rides for stations on the South side.

## merge both tables joined on station name to create a wide table 

# stationname, rides from ridership 
# station name and latitude from station table 
# we want a left join of all info in ridership with latitude tacked on 

# lets get the columns we need first into seperate dfs 

ridership_filter_df = ridership_df[['stationname', 'rides', 'date']].copy()
print(ridership_filter_df.head())
print(len(ridership_filter_df))
l_stations_filter_df = l_stations_df[['STATION_NAME', 'latitude']].copy()

print(len(l_stations_filter_df))
l_stations_filter_df.rename(columns={'STATION_NAME': 'stationname'}, inplace=True)
print(l_stations_filter_df.head())

res_df = ridership_filter_df.merge(l_stations_filter_df, on='stationname', how='left')
print(len(res_df))
print(res_df.head())

all_total_rides = res_df['rides'].sum()
print(all_total_rides)

southern_df  = res_df[res_df['latitude'] < 41.881]
print(len(southern_df))

#print(807747323/46696)










res_df_clean = res_df.dropna()
print(len(res_df_clean))
print(res_df_clean.head())

southern_df  = res_df_clean[res_df_clean['latitude'] < 41.881]
print(len(southern_df))

total_rides = southern_df['rides'].sum()
print("total rides: ")
print(total_rides*2)

# distinct_dates= len(pd.unique(southern_df['date']))
# print("distinct_dates")
# print(distinct_dates)

# print("rides per day")
# print(total_rides/distinct_dates)




