import json
import os
import pyinstaller_versionfile


class Configue:
    def __init__(self):
        if not os.path.isfile("src/config/config.json"):
            self.cfg = {
                "infos": {
                    "nom": "Centre macro",
                    "description": "Centre regroupant plein de macro, et permattant la gestion de leurs mise à jour.",
                    "version": "0.2",
                    "auteur": "ZP6177",
                    "compagnie": "ZP6177"
                },
                "config": {
                    "theme": "gunmetal",
                    "font": "Berlin Sans FB Demi",
                    "widht": 1200,
                    "height": 800,
                    "opacity": 0.96,
                    "cur": "test"
                },
                "var": {
                    "debug": True,
                    "resize": True,
                    "auto_close": True,
                    "toolbox_pin": True
                }
            }
            with open("src/config/config.json", "w", encoding="utf-8") as fichier:
                json.dump(self.cfg, fichier, indent=4)
            self.write_version_file()
        else:
            with open("src/config/config.json", "r", encoding="utf-8") as fichier:
                self.cfg = json.load(fichier)

    def write_version_file(self):
        pyinstaller_versionfile.create_versionfile(
            output_file="src/config/version_file.txt",
            version=self.cfg["infos"]["version"],
            company_name=self.cfg["infos"]["compagnie"],
            file_description=self.cfg["infos"]["description"],
            internal_name=self.cfg["infos"]["nom"],
            legal_copyright="",  # "© My Imaginary Company. All rights reserved.",
            original_filename=f'{self.cfg["infos"]["nom"]}.exe',
            product_name=self.cfg["infos"]["nom"]
        )

    def update(self, section: str, clef: str, valeur):
        """
        :param section: infos || config || variable
        :param clef: nom | description | version | auteur | compagnie || curseur | theme || auto_reload
        :param valeur: string || string || bool
        :return: None
        """
        with open("src/config/config.json", "r+") as output:
            self.cfg[section][clef] = valeur
            output.seek(0)
            json.dump(self.cfg, output, indent=4)
            output.truncate()

        if section == "infos":
            self.write_version_file()
