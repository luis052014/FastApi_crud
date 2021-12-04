from  sqlalchemy import create_engine, MetaData
import psycopg2

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/fastapi")

meta = MetaData()

conn = engine.connect()