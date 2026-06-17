from sqlalchemy import create_engine,text

db_url = "postgresql://postgres:_dhruv._.9@localhost:5432/olist_analytics_db"
engine = create_engine(db_url)