import sqlite3
import pandas as pd

conn = sqlite3.connect('plasmid.db')

cursor = conn.cursor()

if __name__ == "__main__":
    mob_df = pd.read_csv("plasmid_mob_type.csv")
    mob_df.to_sql(con=conn,name="inctype")

