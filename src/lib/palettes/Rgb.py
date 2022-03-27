import json
from src.config.config import Configue


class Rgb:

    def get_rgb(self, val):
        with open(fr"src/theme/{Configue().cfg['config']['theme']}.json", "r") as fichier:
            js = json.load(fichier)
            return tuple(js[val])
    def rgb_to_hex(self, rgb):
        return "#" + "%02x%02x%02x" % rgb

    def th1(self): return self.get_rgb("th1") + (255,)
    def th2(self): return self.get_rgb("th2") + (255,)
    def th3(self): return self.get_rgb("th3") + (255,)
    def bn1(self): return self.get_rgb("bn1") + (255,)
    def bn2(self): return self.get_rgb("bn2") + (255,)
    def tr(self): return 0, 0, 0, 0

    def hx_th1(self): return self.rgb_to_hex(self.get_rgb("th1"))
    def hx_th2(self): return self.rgb_to_hex(self.get_rgb("th2"))
    def hx_th3(self): return self.rgb_to_hex(self.get_rgb("th3"))
    def hx_bn1(self): return self.rgb_to_hex(self.get_rgb("bn1"))
    def hx_bn2(self): return self.rgb_to_hex(self.get_rgb("bn2"))
