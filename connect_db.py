import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
load_dotenv()



username = os.getenv('username')
password = quote_plus(os.getenv('password'))
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

dataset = pd.read_csv('data/cleaned_data.csv')
table_name = 'rider_data'
dataset.to_sql(table_name,engine,if_exists='replace',index=False)

print(f'Data successfully loaded into table {table_name} in database {database}')
