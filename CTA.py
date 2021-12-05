import pandas as pd
import numpy as np

df = pd.read_csv('CTA_list_of_L_stops.csv')
print(df.columns.tolist())
# # find the number of unique stations by MAP_ID.

df2 = df.groupby('MAP_ID')
len(df2.first())
print(df2.first().count()['STOP_ID'])


l_stops_df = pd.read_csv('CTA_list_of_L_stops.csv')
print(l_stops_df['location'])
station_bools = l_stops_df[['MAP_ID','ADA','RED','BLUE','G','BRN','P','Pexp','Y','Pnk','O']].groupby('MAP_ID').any()
l_stations_df = l_stops_df[['MAP_ID','STATION_NAME','STATION_DESCRIPTIVE_NAME','Location']] \
    .merge(station_bools, how='left', left_on='MAP_ID', right_index=True).drop_duplicates()
l_stations_df.columns= l_stations_df.columns.str.lower()

l_stations_df[['latitude','longitude']] = \
   l_stations_df['Location'].str.replace('\(|\)','',regex=True) \
   .str.split(',', expand=True).apply(pd.to_numeric)
l_stations_df.drop('Location', axis=1, inplace=True)

ridership_df = pd.read_csv('CTA_ridership_daily_totals.csv')