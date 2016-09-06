import cairo


class Destination:
    def make(self, nx, ny, source1, source2, mask):
        res_x = 768
        res_y = 1024
        dx = 768. / nx
        dy = 1024. / ny
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768 * 4, 1024 * 2)
        context = cairo.Context(surface)
        context.set_source_surface(source1)
        context.mask_surface(mask)
        context.fill()
        context = cairo.Context(surface)
        context.translate(768 * 2, 0)
        context.set_source_surface(source2)
        context.mask_surface(mask)
        context.fill()
        return surface


if __name__ == "__main__":
    source1 = cairo.ImageSurface.create_from_png("image/source_20x30.png")
    source2 = cairo.ImageSurface.create_from_png("image/Flags/flags.png")
    mask = cairo.ImageSurface.create_from_png("image/mask_20x30.png")
    dest = Destination()
    surface = dest.make(20, 30, source1, source2, mask)
    surface.write_to_png("image/template_20x30.png")
