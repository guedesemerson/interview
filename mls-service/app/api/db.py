import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

mls = Table(
    'mls',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('source_id', String(50)),
    Column('property_id', ARRAY(Integer)),
    Column('first_american_listing_id', String(250)),

)

database = Database(DATABASE_URI)