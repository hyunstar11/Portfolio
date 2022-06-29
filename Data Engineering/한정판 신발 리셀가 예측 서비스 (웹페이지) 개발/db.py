import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# CSV 파일 불러오기 1
df1 = pd.read_csv('StockX-Data-Contest-2019-3.csv')

#df1['Order Date'] = pd.to_datetime(df1['Order Date']) # to_datetime을 통해 시간과 날짜를 다루기 쉬운 datetime64 형태로 변환
#df1['Release Date'] = pd.to_datetime(df1['Release Date'])

#df1["Premium %"] = (df1["Sale Price"] / df1["Retail Price"]) * 100 
#df1['Days_Since_Release'] = df1['Order Date'] - df1['Release Date']
#df1['Days_Since_Release'] = df1['Days_Since_Release'].dt.days.astype('int16')
#df1 = df1[df1['Days_Since_Release'] >= 0]

# Sneakers2 라는 데이터베이스 만들기 
# Sqlite   
con = sqlite3.connect("Sneakers8.db")
df1.to_sql("shoe", con, if_exists="append", index=False)
con.commit()

#CSV 파일 불러오기 2
#df = pd.read_csv('StockX3.csv')

# Sneakers 라는 데이터베이스 만들기 
# Sqlite   
#con = sqlite3.connect("Sneakers.db")
#df.to_sql("shoe", con, if_exists="append", index=False)
#con.commit()


#engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

# 데이터베이스 연결
#engine = create_engine('postgresql://zgyrldjf:ngcUoDi8jpQyKMP8I5QHBTRK16ja6pfy@castor.db.elephantsql.com/zgyrldjf')
#df.to_sql("database1234567", engine)

