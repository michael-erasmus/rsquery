#!/usr/bin/env python
import os
import sys
import fileinput
import argparse
from tabulate import tabulate
import pandas as pd
from pandas.io.sql import SQLTable, pandasSQL_builder
from sqlalchemy import create_engine
from sqlalchemy import text


#TODO: Replace this with rsdf
def get_engine():
    redshift_db_name = os.getenv('REDSHIFT_DB_NAME')
    redshift_user = os.getenv('REDSHIFT_USER')
    redshift_password = os.getenv('REDSHIFT_PASSWORD')
    redshift_endpoint = os.getenv('REDSHIFT_ENDPOINT')
    redshift_db_port = int(os.getenv('REDSHIFT_DB_PORT'), 0)

    engine_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        redshift_user, redshift_password, redshift_endpoint,
        redshift_db_port, redshift_db_name)

    return create_engine(engine_string)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.parse_args()

    lines = sys.stdin.readlines()
    query = ''.join(lines)

    engine = get_engine()

    df = pd.read_sql_query(query, engine)
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == "__main__":
    main(sys.argv[1:])
