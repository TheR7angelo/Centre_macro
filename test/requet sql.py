import base64
import os
import sqlite3

def grade(bdd: str, user=os.getlogin()):
    with sqlite3.connect(bdd) as conn:
        cursor = conn.cursor()

        cursor.execute(f"""
                        SELECT ad_grade
                        FROM t_gr
                        WHERE ad_nom = '{user}'
                        """)
        user = cursor.fetchone()
        user = 4 if user is None else user[0]
    return user

def add_app(bdd: str, ap_nom: str, ap_desc: str, in_ver: float, ap_auteur: str, in_maj: str, ap_li_id: str, ap_img: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with open(ap_img, 'rb') as input_file:
            ap_img = base64.b64encode(input_file.read()).decode("utf-8")

        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT at_id
                            FROM t_auteur
                            WHERE at_nom = '{ap_auteur}'
                            """)
            row = cursor.fetchone()
            if row is not None:
                ap_auteur = row[0]
            else:
                print("auteur non enregistrer\nMerci de le rajouter")
                at_mail = input()
                cursor.execute(f"""
                                        INSERT INTO t_auteur(at_nom, at_mail)
                                        VALUES ('{ap_auteur}', '{at_mail}');
                                        """)
                ap_auteur = cursor.lastrowid

            cursor.execute(f"""
                            SELECT ln_id
                            FROM t_lien
                            WHERE ln_lien = '{ap_li_id}'
                            """)
            row = cursor.fetchone()
            if row is not None:
                ap_li_id = row[0]
            else:
                cursor.execute(f"""
                                INSERT INTO t_lien(ln_lien)
                                VALUES ('{ap_li_id}');
                                """)
                ap_li_id = cursor.lastrowid

            cursor.execute(f"""
                            INSERT INTO t_app(ap_nom, ap_desc, ap_auteur, ap_img, ap_li_id)
                            VALUES ('{ap_nom}', '{ap_desc}', {ap_auteur}, '{ap_img}', {ap_li_id});
                            """)

            in_ap_id = cursor.lastrowid

            cursor.execute(f"""
                            INSERT INTO t_ver(in_ap_id, in_ver, in_maj)
                            VALUES ({in_ap_id}, {in_ver}, '{in_maj}');
                            """)
            conn.commit()

        return in_ap_id
    else:
        print("Grade insuficent pour effectuée cette modification")

def add_auteur(bdd: str, at_nom: str, at_mail: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            INSERT INTO t_auteur(at_nom, at_mail)
                            VALUES ('{at_nom}', '{at_mail}');
                            """)
            at_id = cursor.lastrowid
            conn.commit()
        return at_id
    else:
        print("Grade insuficent pour effectuée cette modification")

def add_bug(bdd: str, bu_sender: str, bu_contact: str, bu_ap_id: int, bu_ap_ver: float, bu_desc: str):
    with sqlite3.connect(bdd) as conn:
        cursor = conn.cursor()

        cursor.execute(f"""
                        INSERT INTO t_bug(bu_sender, bu_contact, bu_ap_id, bu_ap_ver, bu_desc)
                        VALUES ('{bu_sender}', '{bu_contact}', {bu_ap_id}, {bu_ap_ver}, '{bu_desc}');
                        """)
        bu_id = cursor.lastrowid
        conn.commit()
    return bu_id

def add_admin(bdd: str, ad_nom: str, ad_grade: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT al_id
                            FROM t_adlist
                            WHERE al_nom = '{ad_grade}'
                            """)
            ad_grade = cursor.fetchone()[0]

            try:
                cursor.execute(f"""
                                INSERT INTO t_gr (ad_nom, ad_grade)
                                VALUES ('{ad_nom}', {ad_grade})
                                """)
            except sqlite3.IntegrityError:
                print(f"{ad_nom} existe déja dans la base")

            conn.commit()
    else:
        print("Grade insuficent pour effectuée cette modification")

def add_lien(bdd: str, ln_lien: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            INSERT INTO t_lien(ln_lien)
                            VALUES ('{ln_lien}');
                            """)
            ln_id = cursor.lastrowid
            conn.commit()
        return ln_id
    else:
        print("Grade insuficent pour effectuée cette modification")

def add_ver(bdd: str, in_ap_id: str, in_ver: float, in_maj: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT ap_id
                            FROM t_app
                            WHERE ap_nom='{in_ap_id}';
                            """)
            ap_id = cursor.fetchone()
            if ap_id is not None:
                ap_id = ap_id[0]
                cursor.execute(f"""
                                INSERT INTO t_ver(in_ap_id, in_ver, in_maj)
                                VALUES ({ap_id}, {in_ver}, '{in_maj}');
                                """)
                conn.commit()
    else:
        print("Grade insuficent pour effectuée cette modification")

def update_ap(bdd: str, ap_nom_old: str, ap_nom: str, ap_desc: str, ap_auteur: str, ap_li_id: str, ap_img: str, user=os.getlogin()):

    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT ap_id
                            FROM t_app
                            WHERE ap_nom='{ap_nom_old}'
                            """)
            ap_id = cursor.fetchone()[0]

            cursor.execute(f"""
                            SELECT at_id
                            FROM t_auteur
                            WHERE at_nom = '{ap_auteur}'
                            """)
            row = cursor.fetchone()
            if row is not None:
                ap_auteur = row[0]
            else:
                print("auteur non enregistrer\nMerci de le rajouter")
                at_mail = input()
                cursor.execute(f"""
                                        INSERT INTO t_auteur(at_nom, at_mail)
                                        VALUES ('{ap_auteur}', '{at_mail}');
                                        """)
                ap_auteur = cursor.lastrowid

            cursor.execute(f"""
                            SELECT ln_id
                            FROM t_lien
                            WHERE ln_lien = '{ap_li_id}'
                            """)
            row = cursor.fetchone()
            if row is not None:
                ap_li_id = row[0]
            else:
                cursor.execute(f"""
                                INSERT INTO t_lien(ln_lien)
                                VALUES ('{ap_li_id}');
                                """)
                ap_li_id = cursor.lastrowid

            cursor.execute(f"""
                            UPDATE t_app
                            SET ap_nom='{ap_nom}', ap_desc='{ap_desc}', ap_auteur='{ap_auteur}', ap_li_id='{ap_li_id}', ap_img='{ap_img}'
                            WHERE ap_id={ap_id}
                            """)
    else:
        print("Grade insuficent pour effectuée cette modification")

def update_admin(bdd: str, ad_nom: str, ad_grade: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 3:
        if user != ad_nom:
            with sqlite3.connect(bdd) as conn:
                cursor = conn.cursor()

                cursor.execute(f"""
                                SELECT ad_grade
                                FROM t_gr
                                WHERE ad_nom = '{user}'
                                """)
                niveau = cursor.fetchone()[0]

                cursor.execute(f"""
                                SELECT al_id
                                FROM t_adlist
                                WHERE al_nom = '{ad_grade}'
                                """)
                al_id = cursor.fetchone()

                if al_id is not None:
                    al_id = al_id[0]

                    if niveau < al_id or niveau == 1:
                        cursor.execute(f"""
                                        SELECT ad_id
                                        FROM t_gr
                                        WHERE ad_nom = '{ad_nom}'
                                        """)
                        ad_id = cursor.fetchone()
                        if ad_id is None:
                            cursor.execute(f"""
                                            INSERT INTO t_gr (ad_nom, ad_grade)
                                            VALUES ('{ad_nom}', {al_id})
                                            """)
                        else:
                            ad_id = ad_id[0]
                            cursor.execute(f"""
                                            UPDATE t_gr
                                            SET ad_grade = {al_id}
                                            WHERE ad_id={ad_id}
                                            """)
                            conn.commit()
                    else:
                        print("Grade insuficent pour effectuée cette modification")
                else:
                    print("Le grade n'existe pas")
        else:
            print("Impossible de changer son propre grade")
    else:
        print("Grade insuficent pour effectuée cette modification")

def update_auteur(bdd: str, old_at_nom: str, at_nom: str, at_mail, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT at_id
                            FROM t_auteur
                            WHERE at_nom='{old_at_nom}';
                            """)
            old_at_nom = cursor.fetchone()
            if old_at_nom is None:
                cursor.execute(f"""
                                INSERT INTO t_auteur(at_nom, at_mail)
                                VALUES ('{at_nom}', '{at_mail}');
                                """)
            else:
                old_at_nom = old_at_nom[0]
                cursor.execute(f"""
                                UPDATE t_auteur
                                SET at_nom='{at_nom}', at_mail='{at_mail}'
                                WHERE at_id={old_at_nom};
                                """)
                conn.commit()
    else:
        print("Grade insuficent pour effectuée cette modification")

def update_bug(bdd: str, bu_id: int, bu_helper: str, bu_dtCharge: str, bu_etat: str, bu_resolut: str, bu_dtResolut, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 3:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT ad_id
                            FROM t_gr
                            WHERE bu_helper='{bu_helper}';
                            """)
            bu_helper = cursor.fetchone()[0]

            cursor.execute(f"""
                            SELECT bl_id
                            FROM t_buetatlist
                            WHERE bu_etat='{bu_etat}';
                            """)
            bu_etat = cursor.fetchone()[0]

            cursor.execute(f"""
                            UPDATE t_bug
                            SET bu_helper={bu_helper}, bu_dtCharge='{bu_dtCharge}', bu_etat={bu_etat}, bu_resolution='{bu_resolut}', bu_dtResolut='{bu_dtResolut}'
                            WHERE bu_id={bu_id};
                            """)
            conn.commit()
    else:
        print("Grade insuficent pour effectuée cette modification")

def update_lien(bdd: str, old_ln_lien: str, ln_lien, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT ln_id
                            FROM t_lien
                            WHERE ln_lien='{old_ln_lien}'
                            """)
            ln_id = cursor.fetchone()
            if ln_id is None:
                cursor.execute(f"""
                                INSERT INTO t_lien(ln_lien)
                                VALUES ('{ln_lien}');
                                """)
            else:
                ln_id = ln_id[0]
                cursor.execute(f"""
                                UPDATE t_lien
                                SET ln_lien='{ln_lien}'
                                WHERE ln_id={ln_id}
                                """)
            conn.commit()
    else:
        print("Grade insuficent pour effectuée cette modification")

def update_ver(bdd: str, old_ver_ap: str, old_ver: float, in_ver: float, in_maj: str, user=os.getlogin()):
    if grade(bdd=bdd, user=user) <= 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT ap_id
                            FROM t_app
                            WHERE ap_nom='{old_ver_ap}'
                            """)
            ap_id = cursor.fetchone()
            if ap_id is not None:
                cursor.execute(f"""
                                UPDATE t_ver
                                SET in_ver={in_ver}, in_maj='{in_maj}', in_date=CURRENT_DATE
                                WHERE in_ap_id={ap_id} AND in_ver={old_ver};
                                """)
            else:
                print(f"L'application {old_ver_ap} n'existe pas dans la base")
    else:
        print("Grade insuficent pour effectuée cette modification")

def delete_admin(bdd: str, ad_nom: str, user=os.getlogin()):
    niveau = grade(bdd=bdd, user=user)
    niveau_del = grade(bdd=bdd, user=ad_nom)
    if user == ad_nom:
        print("Impossible de se supprimer sois même")
    elif niveau < niveau_del:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            SELECT ad_id
                            FROM t_gr
                            WHERE ad_nom='{ad_nom}';
                            """)
            ad_id = cursor.fetchone()
            if ad_id is not None:
                ad_id = ad_id[0]

                cursor.execute(f"""
                                    DELETE
                                    FROM t_gr
                                    WHERE ad_id={ad_id};
                                    """)
                conn.commit()
    elif niveau_del == 1:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                            SELECT ad_id
                            FROM t_gr
                            WHERE ad_grade=1;
                            """)
            if len(cursor.fetchall()) > 1:
                cursor.execute(f"""
                                SELECT ad_id
                                FROM t_gr
                                WHERE ad_nom='{ad_nom}';
                                """)
                ad_id = cursor.fetchone()
                if ad_id is not None:
                    ad_id = ad_id[0]
                    cursor.execute(f"""
                                        DELETE
                                        FROM t_gr
                                        WHERE ad_id={ad_id};
                                        """)
                    conn.commit()
    else:
        print("Grade insuficent pour effectuée cette modification")

def delete_ver(bdd: str, ap_id: str, in_ver: float, user=os.getlogin()):

    def delete(bdd: str, ap_id: int, in_ver: float):
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                            DELETE
                            FROM t_ver
                            WHERE in_ap_id={ap_id} AND in_ver={in_ver};
                            """)
            conn.commit()

    niveau = grade(bdd=bdd, user=user)
    if niveau == 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                            SELECT at_id
                            FROM t_auteur
                            WHERE at_nom='{user}';
                            """)
            user = cursor.fetchone()
            if user is not None:
                user = user[0]
                cursor.execute(f"""
                                SELECT ap_auteur, ap_id
                                FROM t_app
                                WHERE ap_nom='{ap_id}';
                                """)
                ap_id = cursor.fetchone()
                if ap_id is not None:
                    ap_auteur, ap_id = ap_id[0], ap_id[1]
                else:
                    exit()
            else:
                exit()
        if ap_auteur == user:
            delete(bdd=bdd, ap_id=ap_id, in_ver=in_ver)
        else:
            print("Vous ne pouvez pas supprimer une version d'application qui ne vous appartient pas")
    elif niveau == 1:

        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                            SELECT ap_id
                            FROM t_app
                            WHERE ap_nom='{ap_id}';
                            """)
            ap_id = cursor.fetchone()
            if ap_id is not None:
                ap_id = ap_id[0]
            else:
                exit()
        delete(bdd=bdd, ap_id=ap_id, in_ver=in_ver)
    else:
        print("Grade insuficent pour effectuée cette modification")

def delete_app(bdd: str, ap_id: str, user=os.getlogin()):

    def delete(bdd: str, ap_id: int):
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                            DELETE
                            FROM t_ver
                            WHERE in_ap_id={ap_id};
                            """)

            cursor.execute(f"""
                            DELETE
                            FROM t_app
                            WHERE ap_id={ap_id};
                            """)
            conn.commit()

    niveau = grade(bdd=bdd, user=user)
    if niveau == 2:
        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                            SELECT at_id
                            FROM t_auteur
                            WHERE at_nom='{user}';
                            """)
            user = cursor.fetchone()
            if user is not None:
                user = user[0]
                cursor.execute(f"""
                                SELECT ap_auteur, ap_id
                                FROM t_app
                                WHERE ap_nom='{ap_id}';
                                """)
                ap_id = cursor.fetchone()
                if ap_id is not None:
                    ap_auteur, ap_id = ap_id[0], ap_id[1]
                else:
                    exit()
            else:
                exit()
        if ap_auteur == user:
            delete(bdd=bdd, ap_id=ap_id)
        else:
            print("Vous ne pouvez pas supprimer une version d'application qui ne vous appartient pas")
    elif niveau == 1:

        with sqlite3.connect(bdd) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                            SELECT ap_id
                            FROM t_app
                            WHERE ap_nom='{ap_id}';
                            """)
            ap_id = cursor.fetchone()
            if ap_id is not None:
                ap_id = ap_id[0]
            else:
                exit()
        delete(bdd=bdd, ap_id=ap_id)
    else:
        print("Grade insuficent pour effectuée cette modification")

bdd = r"E:\Logiciels\Adobe\Creative Cloud Files\Programmation\Projets Python\Centre macro.db"

img = r"E:\Logiciels\Adobe\Creative Cloud Files\Programmation\Projets Python\INEO Infracom\APCOM\Ressources\Asset\logo.svg"
ap_li_id = r"T:\- 4 Suivi Appuis\18-Partage\BARRENTO ANTUNES Raphael\6_Programme python\Instalateur"

test = 1
