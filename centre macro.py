import base64
import os
import re
import shutil
import sqlite3
import sys
import time
from pprint import pprint

from PySide6 import QtCore, QtWidgets, QtGui

from src import *
from src.gui import *
from src.lib.globals.v_gb import GUID


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    cfg = Configue().cfg
    bdd = r"T:\- 4 Suivi Appuis\18-Partage\BARRENTO ANTUNES Raphael\6_Programme python\Centre macro.db"

    if not os.path.exists(bdd):
        bdd = r"E:\Logiciels\Adobe\Creative Cloud Files\Programmation\Projets Python\Centre macro.db"

    import_ico_app = None
    grade = 4
    regex_mail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
        # size_grip
        self.size_grip = QtWidgets.QSizeGrip(self)
        # tray
        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"), self)
        self.tray.activated.connect(self.trayActivate)
        self.timer_double_click = QtCore.QTimer(self)
        self.timer_double_click.setSingleShot(True)
        self.timer_double_click.timeout.connect(self.traySingleClick)
        # tray_menu
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### VARIABLES DE BASES ###
        self.win_state = QtCore.Qt.WindowNoState

        # backup = Maj().make_bakup(bdd=self.bdd)
        maj = Maj().get_maj(bdd=self.bdd, nom=self.cfg['infos']['nom'])
        self.grade = maj[0]

        ### FONCTIONS AU LANCEMENT ###
        self.INIT(
            [self.IN_BASE, "Configuration des éléments principaux"],
            [self.IN_SETUP_UI, "Setup de l'interface graphique"],
            [self.IN_CLASSE, "Initialisation des Widgets"],
            [self.IN_WG, "Configuration de base des Widgets"],
            [self.IN_CONNECTIONS, "Ajout des connexions"],
            [self.IN_ACT, "Fonctions de base"],
            [self.IN_WG_BASE, "Etat de base des Widgets"],
            [self.IN_TRAY, "Finalisation de la configuration"]
        )

        splash_screen.close()

        if maj[1] > float(self.cfg["infos"]["version"]):
            rep = ResponseBox().INFO(title="Mise à jour disponible",
                                     msg=f"""
                                        Une mise à jour est disponible.
                                        Version: {maj[1]}
                                        Voulez-vous la télécharger ?"
                                        """,
                                     txt_ok="Oui",
                                     txt_cancel="Non")
            if rep:
                try:
                    os.startfile(maj[2])
                except FileNotFoundError:
                    ResponseBox().ALERTE(title="Erreur",
                                         msg="Une erreur est survenue.\nMerci de réessayer ultérieurement.")

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseDoubleClickEvent = self.evt.mouseDoubleClickEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent
        self.mouseReleaseEvent = self.evt.mouseReleaseEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre principal ###
        self.setWindowTitle(Configue().cfg["infos"]["nom"])
        self.setWindowIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.setWindowOpacity(Configue().cfg["config"]["opacity"])
        self.setGraphicsEffect(Shadow().ombre_portee(self))

        self.e_resize_screen()

    def IN_SETUP_UI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### Ui principal ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)

    def IN_CLASSE(self):

        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Base(self.fr_body).tr()
        Frame.Menu(self.fr_menu_bottom).bottom()
        ### /QFrame ###

        Label.Base(self.lb_mt_ico).ico_main()
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_mb_version).tr()

        ### QTreeWidget ###
        ListWidget.Test(self.list_menu).th()
        ### /QTreeWidget ###

        PushButton.menu_top(self.pb_mt_option).option()
        PushButton.menu_top(self.pb_mt_reduire).reduire()
        PushButton.menu_top(self.pb_mt_agrandir).agrandir()
        PushButton.menu_top(self.pb_mt_quitter).quitter()

        # ## QRadioButton ###
        TrayIcon.Main(self.tray_menu)

        ######################################################################################################

        ### Changer de version
        Label.Base(self.lb_changeVer_titre).th()
        TextEdit.Base(self.text_desc, self.text_chang, self.text_old_chang, self.text_new_chang).th()
        LineEdit.Base(self.line_ap_ver).th()
        Label.Base(self.lb_list_app, self.lb_old_ver, self.lb_change_old_ver, self.lb_correct_old,
                   self.lb_new_ver, self.lb_change_new_ver, self.lb_correct_new).th()
        SpinBox.PlusMinus(self.num_old_ver, self.num_new_ver).th()
        PushButton.Base(self.pb_ap_selector_ver).th()
        PushButton.Base(self.pb_new_ver_val).th2()
        ### /Changer de version

        ### Ajout application
        Label.Base(self.lb_addApp_titre).th()
        ComboBox.Base(self.cb_auteur, self.cb_stock, self.cb_list_app_ver).th()
        LineEdit.Base(self.line_ap, self.line_ap_nom).th()
        Label.Base(self.lb_nom_ap, self.lb_ver_ap, self.lb_auteur_ap,
                   self.lb_stock, self.lb_desc_ap, self.lb_chang_ap).th()
        SpinBox.PlusMinus(self.num_ver).th()
        PushButton.Base(self.pb_ico, self.pb_ap_selector).th()
        PushButton.Base(self.pb_new_ap_val).th2()
        ### /Ajout application

        ### Ajout auteur
        Label.Base(self.lb_auteur_titre).th()
        LineEdit.Base(self.ln_auteur_name_add, self.ln_auteur_alias_add, self.ln_auteur_mail_add).th()
        Label.Base(self.lb_auteur_name_add, self.lb_auteur_alias_add, self.lb_auteur_mail_add).th()
        PushButton.Base(self.pb_auteur_add_valide).th2()
        ### /Ajoput auteur

        ### Page logiciel
        ScrollArea.Base(self.scrollArea).th()
        Label.Base(self.lb_logiciel_titre).th()

        ### Adding application ###
        for wid in [self.num_ver, self.num_old_ver, self.num_new_ver]:
            wid.setLocale(QtCore.QLocale("English"))

        with sqlite3.connect(self.bdd) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                            SELECT at_nom
                            FROM t_auteur
                            """)
            rows = cursor.fetchall()
            for item in rows:

                self.cb_auteur.addItem(item[0])

            cursor.execute("""
                            SELECT ln_lien
                            FROM t_lien
                            """)
            rows = cursor.fetchall()
            for item in rows:
                self.cb_stock.addItem(item[0])

            cursor.execute("""
                            SELECT *
                            FROM v_centre_logiciel
                            """)
            rows = cursor.fetchall()
            col = [item[0] for item in cursor.description]

        x_frame, y_frame = 0, 0
        for row in rows:
            dictio = dict(zip(col, row))

            if self.grade == 1 or (self.grade == 2 and GUID == dictio["auteur"]):
                self.cb_list_app_ver.addItem(dictio["nom"])

            app_id = f"{dictio['id']}"

            self.frame = Button_frame(self.scrollArea)
            self.frame.setContentsMargins(2, 2, 2, 2)

            self.frame.setObjectName(f"fr_ct_{dictio['id']}")
            self.frame.setMaximumHeight(232)
            # Frame.button(self.frame).th()

            self.frame.clicked.connect(lambda text=app_id: self.install_app(text))

            self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)

            img = QtGui.QPixmap()
            img.loadFromData(base64.b64decode(dictio["image"]))

            self.lb_app = QtWidgets.QLabel(self.frame)
            self.lb_app.setObjectName(f"lb_ct_{dictio['id']}")
            self.lb_app.setPixmap(img)
            self.lb_app.setMaximumSize(128, 128)
            self.lb_app.setScaledContents(True)

            # self.verticalLayout.addWidget(self.btn)
            self.verticalLayout.addWidget(self.lb_app, 0, Align().center_horizontal())

            self.titre = QtWidgets.QLabel("Titre :")
            self.titre_value = QtWidgets.QLabel(dictio["nom"])
            self.titre.setObjectName(f"lb_ct_tt_{dictio['id']}")
            self.titre_value.setObjectName(f"fr_ct_tv_{dictio['id']}")

            self.version = QtWidgets.QLabel("Version :")
            self.version_value = QtWidgets.QLabel(str(dictio["ver"]))
            self.version.setObjectName(f"lb_ct_vs_{dictio['id']}")
            self.version_value.setObjectName(f"fr_ct_vv_{dictio['id']}")

            self.auteur = QtWidgets.QLabel("Auteur :")
            self.auteur_value = QtWidgets.QLabel(dictio["auteur"])
            self.auteur.setObjectName(f"lb_ct_at_{dictio['id']}")
            self.auteur_value.setObjectName(f"fr_ct_av_{dictio['id']}")

            self.description = QtWidgets.QLabel("Description :")
            self.description_value = QtWidgets.QLabel(dictio["description"])
            self.description.setObjectName(f"lb_ct_dt_{dictio['id']}")
            self.auteur_value.setObjectName(f"fr_ct_dv_{dictio['id']}")
            self.description_value.setWordWrap(True)

            Label.Base(self.titre, self.titre_value,
                       self.version, self.version_value,
                       self.auteur, self.auteur_value,
                       self.description, self.description_value).app_menu()

            self.formLayout = QtWidgets.QFormLayout(self.frame)
            tmp = [[self.titre, self.titre_value], [self.version, self.version_value], [self.auteur, self.auteur_value], [self.description, self.description_value]]
            for x in range(len(tmp)):
                for i, role in enumerate([QtWidgets.QFormLayout.LabelRole, QtWidgets.QFormLayout.FieldRole]):
                    self.formLayout.setWidget(x, role, tmp[x][i])

            self.verticalLayout.addLayout(self.formLayout)

            self.gridLayout.addWidget(self.frame, x_frame, y_frame)
            y_frame = y_frame+1
            if y_frame == 3:
                y_frame = 0
                x_frame += 1

        ### /Page logiciel

    def IN_WG(self):

        ### Base ###
        self.setCursor(Functions().SET_CURSOR(Cur().Arrow()))

        ### Nom de l'app ###
        self.lb_mt_nom.setText(self.cfg["infos"]["nom"])

        ### Widget blanc pour centrer le nom de l'app ###
        dim = Dim().h9() * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim * 3, height=dim)

        ### Version de l'app ###
        self.lb_mb_version.setText(f" Version : {self.cfg['infos']['version']}")

        ### Centrage des titre ###
        for widget in [self.lb_logiciel_titre, self.lb_addApp_titre, self.lb_changeVer_titre, self.lb_auteur_titre]:
            widget.setAlignment(Align().center_horizontal())

        ### size_grip ###
        if self.cfg["var"]["resize"]:
            self.size_grip.setCursor(Functions().SET_CURSOR(Cur().fleche_nwse()))
            self.size_grip.setStyleSheet(
                f"""
                QSizeGrip {{
                image: url({Img().resize()}th3.svg);
                width: {Dim().h10()}px;
                height: {Dim().h10()}px;
                }}
                """
            )
            self.hlay_menu_bottom.addWidget(self.size_grip)


        self.lb_icon_new.setPixmap(QtGui.QPixmap(f"{Img().img_vide()}bn1.svg"))
        self.lb_icon_new.setScaledContents(True)

        ########################################################!!!! Il faut des icones pour chaque bouton

        if self.grade == 1:
            menu = ["Application", "Helper", "Editeur", "Admin"]
        elif self.grade == 2:
            menu = ["Application", "Helper", "Editeur"]
        elif self.grade == 3:
            menu = ["Application", "Helper"]
        else:
            menu = ["Application"]

        self.list_menu.addItems(menu)
        self.list_menu.setCurrentRow(0)

        for wid in [self.cb_auteur, self.cb_stock, self.cb_list_app_ver]:
            liste = sorted([wid.itemText(i) for i in range(wid.count())])
            wid.clear()
            for item in liste:
                wid.addItem(item)
            wid.setCurrentIndex(-1)

        self.lb_app_ver_add.setScaledContents(True)

    def IN_CONNECTIONS(self):

        ### Menu_top ###
        self.pb_mt_option.clicked.connect(lambda: OptionBox(fen_main=fen).MAIN())
        self.pb_mt_reduire.clicked.connect(lambda: self.evt.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.evt.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.evt.e_cacher())

        ### Menu application
        self.list_menu.itemClicked.connect(self.change_mode)

        ### Menu Editeur
        self.pb_addApp_edit.clicked.connect(lambda: self.change_menu("ajout_app"))
        self.pb_addVer_edit.clicked.connect(lambda: self.change_menu("change_ver"))

        ### Menu Admin
        self.pb_addApp_admin.clicked.connect(lambda: self.change_menu("ajout_app"))
        self.pb_addVer_admin.clicked.connect(lambda: self.change_menu("change_ver"))
        self.pb_addAuteur_admin.clicked.connect(lambda: self.change_menu("ajout_auteur"))

        ### Menu crée appli
        self.lb_icon_new.new_ico.connect(self.import_app_img)
        self.lb_icon_new.clicked.connect(self.import_app_img_file)
        self.pb_ico.clicked.connect(self.import_app_img_file)
        self.pb_ap_selector.clicked.connect(lambda: self.import_app_file(self.pb_ap_selector.objectName()))
        self.pb_new_ap_val.clicked.connect(self.import_app)

        ### Menu ajouté version
        self.cb_list_app_ver.currentTextChanged.connect(lambda: self.add_ver_new(self.cb_list_app_ver.currentText()))
        self.pb_ap_selector_ver.clicked.connect(lambda: self.import_app_file(self.pb_ap_selector_ver.objectName()))
        self.pb_new_ver_val.clicked.connect(self.add_ver)

        ### Menu ajouté auteur
        self.pb_auteur_add_valide.clicked.connect(self.add_auteur)

    def IN_ACT(self):

        self.threadpool = QtCore.QThreadPool()

    def IN_WG_BASE(self):
        for wid in [self.num_old_ver, self.text_old_chang]:
            wid.setEnabled(False)

    def IN_TRAY(self):
        ### Actions ###
        Functions.ADD_QACTION(
            self,
            tray=self.tray_menu,
            ico=Img().quitter(),
            ico_rgb="bn2",
            txt="Quitter",
            shortcut_txt="Shift+Esc",
            status_tip="Quitter",
            fct=self.e_quitter_tray,
            sht_1=Keys().shift(),
            sht_2=Keys().escape()
        )

        # self.tray_menu.addSeparator()

        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()

    def INIT(self, *args):
        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue(splash_screen.pg_chargement.value() + 100 / len(args))
            fct[0]()

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(2)

    def add_auteur(self):

        def isValid(email):
            return bool(re.fullmatch(self.regex_mail, email))

        gid = self.ln_auteur_name_add.text()
        alias = self.ln_auteur_alias_add.text()
        mail = self.ln_auteur_mail_add.text()

        erreur = []
        if gid == "":
            erreur.append("le GID ne peut pas étre vide")
        if not isValid(mail):
            erreur.append("adresse mail incorect")

        if len(erreur) == 0:
            with sqlite3.connect(self.bdd) as conn:
                cursor = conn.cursor()

                cursor.execute(f"""
                                SELECT at_nom
                                FROM t_auteur
                                WHERE at_nom='{gid}';
                                """)
                row = cursor.fetchone()
                if row is None:
                    cursor.execute(f"""
                                    INSERT INTO t_auteur(at_nom, at_mail)
                                    VALUES ('{gid}', '{mail}');
                                    """)

                    cursor.execute(f"""
                                    SELECT ad_id, ad_grade
                                    FROM t_gr
                                    WHERE ad_nom='{gid}';
                                    """)
                    row = cursor.fetchone()
                    if row is None:
                        cursor.execute(f"""
                                        INSERT INTO t_gr(ad_nom, ad_grade)
                                        VALUES ('{gid}', 2);
                                        """)
                    else:
                        if row[1] > 2:
                            cursor.execute(f"""
                                            UPDATE t_gr
                                            SET ad_grade=2
                                            WHERE ad_nom='{gid}';
                                            """)
                    conn.commit()
                    MsgBox().INFO(msg=f"Auteur \"{gid}\" ajouté dans la base")
                else:
                    MsgBox().INFO(msg=f"Auteur \"{gid}\" est déja present dans la base")
        else:
            MsgBox().ALERTE(msg=f"""
            Une erreur à étais détecter :\n
            {", ".join(erreur)}\n
            Merci de corriger.""")


    def add_ver(self):
        app = self.line_ap_ver.text()
        ap_id = self.cb_list_app_ver.currentText()
        in_ver = self.num_new_ver.value()
        in_maj = self.text_new_chang.toPlainText()

        erreur = []
        if app == "":
            erreur.append("chemin de l'application")
        if ap_id == "":
            erreur.append("nom de l'application")
        if in_ver == 0:
            erreur.append("version")
        if in_maj == "":
            erreur.append("correctif")

        if not erreur:
            msg = ResponseBox().INFO(title="Validation",
                               msg="Voulez-vous vraiment mettre à jour la version de l'application ?")
            if msg:
                with sqlite3.connect(self.bdd) as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"""
                                    SELECT ap_id
                                    FROM t_app
                                    WHERE ap_nom='{ap_id}';
                                    """)
                    ap_id = cursor.fetchone()
                    ap_id = ap_id[0]
                    cursor.execute(f"""
                                    INSERT INTO t_ver(in_ap_id, in_ver, in_maj)
                                    VALUES ({ap_id}, {in_ver}, "{in_maj}");
                                    """)
                    conn.commit()
                    cursor.execute(f"""
                                    SELECT lien
                                    FROM v_centre_logiciel
                                    WHERE id={ap_id};
                                    """)
                    lien = cursor.fetchone()
                    lien = lien[0]
                    dossier, _ = os.path.split(lien)
                    os.makedirs(dossier, exist_ok=True)
                    shutil.copy(src=app, dst=lien)
        else:
            erreur = ", ".join(erreur)
            MsgBox().ALERTE(msg=f"Des erreurs ont étais détecter :\n{erreur}\nMerci de les corrigers")

    def add_ver_new(self, item):
        with sqlite3.connect(self.bdd) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                            SELECT ver, correctif, image
                            FROM v_centre_logiciel
                            WHERE nom='{item}'
                            """)
            row = cursor.fetchone()
            col = [item[0] for item in cursor.description]

            dictio = dict(zip(col, row))

            img = QtGui.QPixmap()
            img.loadFromData(base64.b64decode(dictio["image"]))
            self.lb_app_ver_add.setPixmap(img)

            self.num_old_ver.setValue(dictio["ver"])
            min = dictio["ver"] + 0.1
            self.num_new_ver.setMinimum(min)
            self.num_new_ver.setValue(min)

            self.text_old_chang.setText(dictio["correctif"])

    def import_app(self):
        ico = self.import_ico_app
        app = self.line_ap.text()
        ap_nom = self.line_ap_nom.text()
        ap_li_id = self.cb_stock.currentText()
        in_ver = self.num_ver.value()
        ap_auteur = self.cb_auteur.currentText()
        ap_desc = self.text_desc.toPlainText()
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

        if len(erreur) == 0:
            if self.grade <= 2:
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

                    cursor.execute(f"""
                                    SELECT lien
                                    FROM v_logiciel
                                    WHERE id={in_ap_id} AND nom='{ap_nom}';
                                    """)
                    lien = cursor.fetchone()
                    lien = lien[0]
                    os.makedirs(os.path.dirname(lien), exist_ok=True)
                    shutil.copy(app, lien)
            else:
                print("Grade insuficent pour effectuée cette modification")
        else:
            erreur = ", ".join(erreur)
            MsgBox().ALERTE(msg=f"Des erreurs ont étais détecter :\n{erreur}\nMerci de les corrigers")

    def import_app_file(self, wid):
        dictio = {
            "pb_ap_selector": self.line_ap,
            "pb_ap_selector_ver": self.line_ap_ver
        }

        app = QtWidgets.QFileDialog.getOpenFileName(self, "Merci de chosir une application", "",
                                                    "Application (*.exe *.msi);;Archive(*.zip *.rar);;Excel (*.xlsx *.xls *.xlsm)")

        if app[0] != "":
            dictio[wid].setText(app[0])
            #wid.setText(app[0])

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
        print(e)

    def change_menu(self, menu):
        menu = getattr(self, f"page_{menu}")
        self.stackedWidget.setCurrentWidget(menu)

    def change_mode(self, item):
        item = item.text()

        dictionaire = {
            "Application": "page_logiciel",
            "Helper": "page_helper",
            "Editeur": "page_editeur",
            "Admin": "page_admin"

        }

        page = getattr(self, dictionaire[item])
        self.stackedWidget.setCurrentWidget(page)

    def install_app(self, id_app):
        with sqlite3.connect(self.bdd) as conn:
            cursor = conn.cursor()

            cursor.execute(f"""
                    SELECT nom, lien
                    FROM v_centre_logiciel
                    WHERE id={int(id_app)};
                    """)
            row = cursor.fetchone()

        install = ResponseBox().INFO(title=f"Instalation de {row[0]}",
                                     msg=f"Voulez-vous installer {row[0]}",
                                     txt_ok="Oui",
                                     txt_cancel="Non",
                                     )
        if install:
            try:
                os.makedirs("installateur", exist_ok=True)
                #prog = shutil.copy(src=row[1], dst=fr"installateur/{row[0]}.msi")
                #prog = os.path.abspath(prog)
                # os.startfile(prog)
                os.startfile(row[1])
            except Exception as e:
                print(e)
                ResponseBox().ALERTE(title="Erreur",
                                     msg="Une erreur est survenue.\nMerci de réessayer ultérieurement.",
                                     txt_ok="D'accord",
                                     txt_cancel="D'accord")

    def e_resize_screen(self):

        if self.cfg["var"]["resize"]:
            self.setMinimumWidth(self.cfg["config"]["widht"])
            self.setMinimumHeight(self.cfg["config"]["height"])
        else:
            self.setFixedWidth(self.cfg["config"]["widht"])
            self.setFixedHeight(self.cfg["config"]["height"])

    def traySingleClick(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        widget = toolBox.geometry()

        toolBox.open()
        toolBox.show()
        toolBox.activateWindow()

        toolBox.move(screen.width() - widget.width(), screen.height() - widget.height())

    def trayDoubleClick(self):
        self.timer_double_click.stop()
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

    def trayActivate(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.timer_double_click.start(app.doubleClickInterval())

        elif reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.trayDoubleClick()

    def e_quitter(self):
        """Permet de quitter l'application"""
        if not Configue().cfg["var"]["auto_close"]:
            self.hide()
        elif ResponseBox().QUITTER():
            app.quit()

    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        if ResponseBox().QUITTER():
            app.quit()

    def closeEvent(self, event):
        event.accept()
        app.quit()

if __name__ == "__main__":
    Functions().GEN_SVG()

    app = QtWidgets.QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.open()
    toolBox = ToolBoxUi()
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
