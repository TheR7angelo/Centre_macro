import os
import sqlite3
import datetime

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

    def make_bakup(self, bdd):
        date = datetime.datetime.now().strftime("%d_%m_%Y %H_%M_%S")
        dossier, fichier = os.path.split(bdd)

        dst = f"{dossier}/backup_{fichier.split('.')[0]}"
        os.makedirs(dst, exist_ok=True)
        bdd_backup = f"{dst}/{fichier.split('.')[0]}_{date}.db"

        try:
            # existing DB
            sqliteCon = sqlite3.connect(bdd)
            # copy into this DB
            backupCon = sqlite3.connect(bdd_backup)
            with backupCon:
                sqliteCon.backup(backupCon, pages=3, progress=self.progress)
            print("backup successful")
        except sqlite3.Error as error:
            print("Error while taking backup: ", error)
        finally:
            if backupCon:
                backupCon.close()
                sqliteCon.close()

    def progress(self, status, remaining, total):
        print(f'Copied {total - remaining} of {total} pages...')


