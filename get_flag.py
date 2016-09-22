import cairo
from enum import Enum


class Flag:
    class Flags(Enum):
        no_country = 0
        germany = 1
        austria = 2
        brazil = 3
        america = 4
        canada = 5
        britain = 6
        mexico = 7
        spain = 8
        australia = 9
        newzealand = 10
        argentina = 11
        honduras = 12
        kazakhstan = 13
        russia = 14
        sweden = 15
        norway = 16
        japan = 17
        korea = 18
        china = 19
        switzerland = 20
        netherlands = 21
        france = 22
        bulgaria = 23
        malaysia = 24

    flags = {
        Flags.no_country: {"name": "unknown", "file": "white.png"},
        Flags.germany: {"name": "germany", "file": "germany.png"},
        Flags.austria: {"name": "austria", "file": "austria.png"},
        Flags.brazil: {"name": "brazil", "file": "brazil.png"},
        Flags.america: {"name": "usa", "file": "america.png"},
        Flags.canada: {"name": "canada", "file": "canada.png"},
        Flags.britain: {"name": "britain", "file": "britain.png"},
        Flags.mexico: {"name": "mexico", "file": "mexico.png"},
        Flags.spain: {"name": "spain", "file": "spain.png"},
        Flags.australia: {"name": "australia", "file": "australia.png"},
        Flags.newzealand: {"name": "new zealand", "file": "newzeland.png"},
        Flags.argentina: {"name": "argentina", "file": "argentina.png"},
        Flags.honduras: {"name": "honduras", "file": "honduras.png"},
        Flags.kazakhstan: {"name": "kazahkstan", "file": "kazahkstan.png"},
        Flags.russia: {"name": "russia", "file": "russia.png"},
        Flags.sweden: {"name": "sweden", "file": "sweden.png"},
        Flags.norway: {"name": "norway", "file": "norway.png"},
        Flags.japan: {"name": "japan", "file": "japan.png"},
        Flags.korea: {"name": "korea", "file": "korea.png"},
        Flags.china: {"name": "china", "file": "china.png"},
        Flags.switzerland: {"name": "switzerland", "file": "switzerland.png"},
        Flags.netherlands: {"name": "netherlands", "file": "netherlands.png"},
        Flags.france: {"name": "france", "file": "france.png"},
        Flags.bulgaria: {"name": "bulgaria", "file": "bulgaria.png"},
        Flags.malaysia: {"name": "malaysia", "file": "malaysia.png"}
    }

    def get_flag(self, name):
        for flag in self.flags:
            if self.flags[flag]["name"] == name.lower():
                return flag
        return self.Flags.no_country

    def get_image(self, flag):
        file = "./image/Flags/{}".format(self.flags[flag]["file"])
        return cairo.ImageSurface.create_from_png(file)
