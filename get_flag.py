from enum import Enum
import cairo


class Flag:

    flags = Enum("FLAGS", "no_country america germany australia china")


    def get_flag(self, name):
        if(name.lower()=="usa"):
            return self.flags.america
        if (name.lower()=="germany"):
            return self.flags.germany
        if(name.lower()=="australia"):
            return self.flags.australia
        if(name.lower()=="china"):
            return self.flags.china
        return self.flags.no_country

    def get_image(self, flag):
        if(flag==self.flags.america):
            return cairo.ImageSurface.create_from_png("image/Flags/america.png")
        if (flag == self.flags.germany):
            return cairo.ImageSurface.create_from_png("image/Flags/germany.png")
        if (flag == self.flags.australia):
            return cairo.ImageSurface.create_from_png("image/Flags/australia.png")
        if (flag == self.flags.china):
            return cairo.ImageSurface.create_from_png("image/Flags/china.png")
        if (flag == self.flags.no_country):
            return cairo.ImageSurface.create_from_png("image/Flags/america.png")
        return cairo.ImageSurface.create_from_png("image/Flags/america.png")