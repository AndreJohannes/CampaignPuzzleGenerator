import cairo


class Source:
    def __init__(self):
        nx = 20
        ny = 30
        res_x = 768
        res_y = 1024
        dx = 768 / nx
        dy = 1024 / ny
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768 * 2, 1024 * 2)
        source = cairo.ImageSurface.create_from_png("image/bordado.png")
        for i in range(0, nx):
            for j in range(0, ny):
                context = cairo.Context(surface)
                context.rectangle(2 * i * dx, 2 * j * dy, 2 * dx, 2 * dy)
                context.clip()
                context.translate(i * dx+dx/2, j * dy+dy/2)
                context.set_source_surface(source)
                context.paint()

        context.set_source_surface(source)

        context.paint()
        surface.write_to_png("image/source.png")


if __name__ == "__main__":
    Source()
