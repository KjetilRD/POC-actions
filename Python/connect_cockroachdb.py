

#This should connnect to Cockroachdb.


from sqlalchemy import create_engine
import os

engine = create_engine(os.environ['DATABASE_URL'])
engine.connect()

