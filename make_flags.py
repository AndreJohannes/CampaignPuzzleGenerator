import cairo
import make_tiling
import random
import get_flag

class Source:
    def make(self, nx, ny, tiling, res):
        dx = res[0] / (1.0*nx)
        dy = res[1] / (1.0*ny)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, res[0] * 2, res[1] * 2)
        flag = get_flag.Flag()
        #source = cairo.ImageSurface.create_from_png("image/bordado.png")
        for i in range(0, nx):
            for j in range(0, ny):
                context = cairo.Context(surface)
                context.rectangle(2 * i * dx, 2 * j * dy, 2 * dx, 2 * dy)
                if(tiling[i][j] is None):
                    source = cairo.ImageSurface(cairo.FORMAT_ARGB32, 20, 20)
                    context2 = cairo.Context(source)
                    context2.set_source_rgb(191 / 255., 191 / 255., 191 / 255.)
                    context2.paint()
                else:
                    source = flag.get_image(tiling[i][j]["flag"])



                pattern = cairo.SurfacePattern(source)
                pattern.set_extend(cairo.EXTEND_REPEAT)
                context.translate(dx*i, dy*j)
                #context.scale(dx/source.get_width(), dy/source.get_height())
                context.set_source(pattern)
                context.fill()

        return surface


if __name__ == "__main__":
    source = Source()
    tiling = make_tiling.Tiling()
    list = []
    for i in range(0, 400):
        list.append(random.randint(0, 4))
    surface = source.make(20, 30, tiling.make(20,30, 5, list))
    surface.write_to_png("image/source_flags_20x30.png")