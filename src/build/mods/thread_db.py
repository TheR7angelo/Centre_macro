import threading
import re

import sqlite3
import psycopg2
import psycopg2.extras

from deepdiff import DeepDiff
from collections import defaultdict

def sqlite3_change(bdd: str, table="All", old_db={}):

    def dict_factory(cursor, row):
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

    with sqlite3.connect(bdd) as conn:
        conn.row_factory = dict_factory
        cursor = conn.cursor()

        if table == "All":
            cursor.execute("""SELECT name
                           FROM sqlite_master
                           WHERE type='table';""")
            tables = cursor.fetchall()
        else:
            tables = [table]

        data = {}
        for table in tables:
            cursor.execute(f"""
                            SELECT *
                            FROM {table["name"]};
                            """)
            data[table["name"]] = cursor.fetchall()

        resultat = differentiel(old=old_db, new=data)

    return data, resultat if resultat != {} else None

def postgres_change(database: str, user: str, password: str, host: str, port=5432, table_schema=None, table_name=None, old_db={}):
    """
    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)
    """
    with psycopg2.connect(database=database, user=user, password=password,
                          host=host, port=port) as conn:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        if table_schema is not None and table_name is not None:
            tables = [{
                "table_schema": table_schema,
                "table_name": table_name
            }]
        elif table_schema is not None:
            cursor.execute(f"SELECT * FROM information_schema.tables WHERE table_schema='{table_schema}'")
            tables = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM information_schema.tables WHERE table_schema not in ('information_schema', 'pg_catalog')")
            tables = cursor.fetchall()

        data = defaultdict(lambda: defaultdict(lambda: None))
        for table in tables:
            cursor.execute(f"""
                            SELECT *
                            FROM {table["table_schema"]}."{table["table_name"]}";
                            """)
            data[table["table_schema"]][table["table_name"]] = cursor.fetchall()

        resultat = differentiel(old=old_db, new=data)

    return data, resultat if resultat != {} else None

def differentiel(old, new):
    diff = DeepDiff(old, new).to_dict()
    resultat = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

    try:
        for key in diff:
            match key:
                case "iterable_item_added":
                    for index, sub_key in enumerate(diff[key]):
                        result = [item for item in re.findall(r"(?:(?<=\[').*?(?=\']))|(?:(?<=\]\[).*?(?=\]\[))", sub_key)]
                        resultat[result[4]]["ADD"][index] = {
                            "row": int(result[1])+1,
                            "value": diff[key][sub_key]
                        }

                case "iterable_item_removed":
                    for index, sub_key in enumerate(diff[key]):
                        result = [item for item in re.findall(r"(?:(?<=\[').*?(?=\']))|(?:(?<=\]\[).*?(?=\]\[))", sub_key)]
                        resultat[result[0]]["REMOVE"][index] = {
                            "row": int(result[1])+1,
                            "value": diff[key][sub_key]
                        }
                case "values_changed":
                    for index, sub_key in enumerate(diff[key]):
                        result = [item for item in re.findall(r"(?:(?<=\[').*?(?=\']))|(?:(?<=\]\[).*?(?=\]\[))", sub_key)]
                        resultat[result[0]]["SET"][index] = {
                            "row": int(result[1])+1,
                            "column": result[2],
                            "value": {
                                "old": diff[key][sub_key]["old_value"],
                                "new": diff[key][sub_key]["new_value"]
                            }
                        }

    except Exception as error:
        print(error)

    return resultat if resultat != {} else None
