import cairo


class Destination:
    def make(self, nx, ny, template):
        res_x = 768
        res_y = 1024
        dx = 768. / nx
        dy = 1024. / ny
        surface1 = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768, 1024)
        surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768, 1024)
        for i in range(0, nx):
            for j in range(0, ny):
                context = cairo.Context(surface1)
                context.rectangle(i * dx - dx / 2, j * dy - dy / 2, 2 * dx, 2 * dy)
                context.clip()
                context.translate(-i * dx - dx / 2, -j * dy - dy / 2)
                context.set_source_surface(template)
                context.paint()
                context = cairo.Context(surface2)
                context.rectangle(i * dx - dx / 2, j * dy - dy / 2, 2 * dx, 2 * dy)
                context.clip()
                context.translate(-i * dx - dx / 2-2*768, -j * dy - dy / 2)
                context.set_source_surface(template)
                context.paint()
        return surface1, surface2


if __name__ == "__main__":
    template = cairo.ImageSurface.create_from_png("image/template_20x30.png")
    dest = Destination()
    surface1, surface2 = dest.make(20, 30, template)
    surface1.write_to_png("image/puzzle_20x30.png")
    surface2.write_to_png("image/flags_20x30.png")