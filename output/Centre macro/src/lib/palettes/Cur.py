import json
import os

from PySide6 import QtGui

from src.config.config import Configue


class Cur:
    cfg = Configue().cfg

    with open(f"src/assets/cursor/{cfg['config']['cur']}/_data.json", "r",
              encoding="utf-8") as fichier:
        cur = json.load(fichier)

    _souris = cur["_souris"]
    _centre = cur["_centre"]
    _crayon = cur["_crayon"]
    _fleche_top = cur["_fleche_top"]

    def CUR(self, img, xy):
        cur = f"src/assets/cursor/{self.cfg['config']['cur']}/{img}"

        return next(
            (
                [f"{cur}{ext}", xy[0], xy[1]]
                for ext in [".cur", ".ani"]
                if os.path.exists(f"{cur}{ext}")
            ),
            [None, 0, 0],
        )

    def agrandir(self): return self.CUR(img="agrandir", xy=self._souris)

    def DragCopy(self): return self.CUR(img="DragCopy", xy=self._souris)

    def crayon(self): return self.CUR(img="crayon", xy=self._crayon)

    def Cross(self): return self.CUR(img="Cross", xy=self._centre)

    def fleche_nesw(self): return self.CUR(img="fleche_nesw", xy=self._centre)

    def fleche_ns(self): return self.CUR(img="fleche_ns", xy=self._centre)

    def fleche_nwse(self): return self.CUR(img="fleche_nwse", xy=self._centre)

    def fleche_top(self): return self.CUR(img="fleche_top", xy=self._fleche_top)

    def fleche_tout(self): return self.CUR(img="fleche_tout", xy=self._centre)

    def fleche_we(self): return self.CUR(img="fleche_we", xy=self._centre)

    def ibeam(self): return self.CUR(img="ibeam", xy=self._centre)

    def infos(self): return self.CUR(img="infos", xy=self._souris)

    def main(self): return self.CUR(img="main", xy=self._souris)

    def non(self): return self.CUR(img="non", xy=self._centre)

    def retour(self): return self.CUR(img="retour", xy=self._souris)

    def Arrow(self): return self.CUR(img="Arrow", xy=self._souris)

    def souris_main(self): return self.CUR(img="souris_main", xy=self._souris)

    def souris_non(self): return self.CUR(img="souris_non", xy=self._souris)

    def Forbidden(self): return self.CUR(img="Forbidden", xy=self._centre)
