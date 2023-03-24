# All Dependencies Below.
import pandas as pd
import json
import psycopg2

from sqlalchemy import create_engine, Table, MetaData, Column, String, Float, Numeric, Integer, JSON, schema
from collections import deque
from config import config
from datetime import datetime
from shared.constant import *
##

def read_csv(csv):
    read_csv = pd.read_csv(csv)

    print(read_csv)

def setup_db(query):
    """ Connect to the PostgreSQL Database Server """
    conn = None

    try:
        params = config()
        print("Connecting to the PostgreSQL Database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(query)
        conn.commit()
        cur.close()
        print('Setting up DB Success!')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# read_csv(RAW_DATA_PATH_PRECI)

def buat_table_yelp_business():
    setup_db('CREATE TABLE IF NOT EXISTS public.yelp_business_2 (no Integer)')

buat_table_yelp_business()