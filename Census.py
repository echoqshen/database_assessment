from sqlalchemy import create_engine
import pandas as pd

# # Path to sqlite, THIS MAY NOT MATCH YOUR PATH
database_path = "Census_Data.sqlite"

# # Create an engine that can talk to the database
engine = create_engine(f"sqlite:///{database_path}")
conn = engine.connect()

df=pd.read_sql ('SELECT * FROM Census_Data', conn )
print(len(df))
print(df.iloc[0])
# print(df.columns.tolist())
# Among the cities with populations equal to or greater
#  than 100,000 people, which city (CityState)
#   has the youngest median age?

big_cities  = df[df['Population'] > 100000]
print(len(big_cities))
print(big_cities[big_cities['Median Age'] == big_cities['Median Age'].min()]['CityState'])






