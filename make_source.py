import cairo


class Source:
    def make(self, nx, ny, tiling, res):
        dx = res[0] / (1.*nx)
        dy = res[1] / (1.*ny)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, res[0] * 2, res[1] * 2)
        source = cairo.ImageSurface.create_from_png("image/bordado.png")
        for i in range(0, nx):
            for j in range(0, ny):
                context = cairo.Context(surface)
                context.rectangle(2 * i * dx, 2 * j * dy, 2 * dx, 2 * dy)
                context.clip()
                context.translate(i * dx + dx / 2, j * dy + dy / 2)
                if tiling[i][j] is None:
                    context.set_source_rgb(191/255., 191/255., 191/255.)
                else:
                    context.set_source_surface(source)
                context.paint()

        #context.set_source_surface(source)
        #context.paint()
        return surface


if __name__ == "__main__":
    source = Source()
    surface = source.make(40, 60)
    surface.write_to_png("image/source_40x60.png")
