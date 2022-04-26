import base64
import os
import shutil
import sqlite3

from PySide6 import QtWidgets, QtGui

from src.lib.palettes.Img import Img
from src.gui.dlg.MsgBox.MsgBox import MsgBox


def import_app(self):
    ico = self.import_ico_app
    app = self.line_ap.text()
    ap_nom = self.line_ap_nom.text()
    ap_li_id = self.cb_stock.currentText()
    in_ver = self.num_ver.value()
    ap_auteur = self.cb_auteur.currentText()
    ap_desc = self.text_desc.toPlainText().replace('"', '""')
    in_maj = self.text_chang.toPlainText()

    erreur = []
    if ico is None:
        erreur.append("icone")
    if app == "":
        erreur.append("chemin de l'application")
    if ap_nom == "":
        erreur.append("nom de l'application")
    if in_ver == 0:
        erreur.append("version")
    if ap_auteur == "":
        erreur.append("auteur")
    if ap_li_id == "":
        erreur.append("stokage")
    if ap_desc == "":
        erreur.append("description")
    if in_maj == "":
        erreur.append("correctif")

    if erreur:
        erreur = ", ".join(erreur)
        MsgBox().ALERTE(msg=f"Des erreurs ont étais détecter :\n{erreur}\nMerci de les corrigers")

    elif self.grade <= 2:
        with open(ico, 'rb') as input_file:
            ap_img = base64.b64encode(input_file.read()).decode("utf-8")

        with sqlite3.connect(self.bdd) as conn:
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
            if row is None:
                cursor.execute(f"""
                                INSERT INTO t_lien(ln_lien)
                                VALUES ('{ap_li_id}');
                                """)
                ap_li_id = cursor.lastrowid

            else:
                ap_li_id = row[0]
            cursor.execute(f"""
                            INSERT INTO t_app(ap_nom, ap_desc, ap_at_id, ap_img, ap_ln_id)
                            VALUES ('{ap_nom}', '{ap_desc}', {ap_auteur}, '{ap_img}', {ap_li_id});
                            """)

            in_ap_id = cursor.lastrowid

            cursor.execute(f"""
                            INSERT INTO t_ver(in_ap_id, in_ver, in_maj)
                            VALUES ({in_ap_id}, {in_ver}, '{in_maj}');
                            """)
            conn.commit()

            cursor.execute(f"""
                            SELECT lien
                            FROM v_logiciel
                            WHERE id={in_ap_id} AND nom='{ap_nom}';
                            """)
            lien = cursor.fetchone()
            lien = lien[0]
            os.makedirs(os.path.dirname(lien), exist_ok=True)
            shutil.copy(app, lien)

            self.affichage_macro(reset=True)

            MsgBox().INFO(msg="Application ajouté")
    else:
        print("Grade insuficent pour effectuée cette modification")


def import_app_file(self, wid):
    dictio = {
        "pb_ap_selector": self.line_ap,
        "pb_ap_selector_ver": self.line_ap_ver
    }

    app = QtWidgets.QFileDialog.getOpenFileName(self, "Merci de chosir une application", "",
                                                "Application (*.exe *.msi);;Archive(*.zip *.rar);;Excel (*.xlsx *.xls *.xlsm)")

    if app[0] != "":
        dictio[wid].setText(app[0])


def import_app_img_file(self):
    img = QtWidgets.QFileDialog.getOpenFileName(self, "Merci de chosir une image", "",
                                                "Image (*.svg *.png *.jpg *.jpeg)")
    if img[0] != "":
        self.import_ico_app = img[0]
        self.lb_icon_new.setPixmap(QtGui.QPixmap(img[0]))


def import_app_img(self, e):
    if e is not None:
        self.import_ico_app = e
    else:
        self.lb_icon_new.setPixmap(QtGui.QPixmap(f"{Img().img_vide()}bn1.svg"))
