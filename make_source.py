import cairo


class Source:
    def make(self, nx, ny):
        res_x = 768
        res_y = 1024
        dx = 768. / nx
        dy = 1024. / ny
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768 * 2, 1024 * 2)
        source = cairo.ImageSurface.create_from_png("image/bordado.png")
        for i in range(0, nx):
            for j in range(0, ny):
                context = cairo.Context(surface)
                context.rectangle(2 * i * dx, 2 * j * dy, 2 * dx, 2 * dy)
                context.clip()
                context.translate(i * dx + dx / 2, j * dy + dy / 2)
                context.set_source_surface(source)
                context.paint()

        #context.set_source_surface(source)
        #context.paint()
        return surface


if __name__ == "__main__":
    source = Source()
    surface = source.make(20, 30)
    surface.write_to_png("image/source_20x30.png")
