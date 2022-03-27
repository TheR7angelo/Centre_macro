import os.path
import sqlite3

from src.config.config import Configue
from src.lib.globals.v_gb import GUID

class Maj:

    def get_maj(self, bdd, nom):
        if os.path.isfile(bdd):
            with sqlite3.connect(bdd) as conn:
                cursor = conn.cursor()

                cursor.execute(f"""
                                SELECT ad_grade
                                FROM t_gr
                                WHERE ad_nom='{GUID}';
                                """)
                grade = cursor.fetchone()

                if grade is None:
                    cursor.execute(f"""
                                    INSERT INTO t_gr (ad_nom, ad_grade)
                                    VALUES ('{GUID}', 4);
                                    """)
                    grade = 4
                else:
                    grade = grade[0]

                cursor.execute(f"""
                        SELECT ver, lien
                        FROM v_centre_logiciel
                        WHERE nom='{nom}';
                        """)
                row = cursor.fetchone()

            return (grade, row[0], row[1]) if row is not None else (grade, 0, None)
        else:
            return 4, 0, None
