import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:Postgres@localhost/Paintings'
# 'postgresql://<username>:<password>@localhost/<database name>'
db = create_engine(conn_string)
conn = db.connect()

# name of the csv files in the folder name given to be added to the database
tables = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for table in tables:
    df = pd.read_csv(f'D:\My_Folder\Data_Analysis\SQL_Projects\Paintings\Data_Tables_CSV\{table}.csv')
    df.to_sql(table, con=conn, if_exists='replace', index=False)
