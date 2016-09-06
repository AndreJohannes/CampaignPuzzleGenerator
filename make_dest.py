import cairo


class Destination:
    def __init__(self):
        nx = 20
        ny = 30
        res_x = 768
        res_y = 1024
        dx = 768 / nx
        dy = 1024 / ny
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768 * 4, 1024 * 2)
        source = cairo.ImageSurface.create_from_png("image/source.png")
        mask = cairo.ImageSurface.create_from_png("image/template.png")
        context = cairo.Context(surface)
        context.set_source_surface(source)
        context.mask_surface(mask)
        context.fill()
        source = cairo.ImageSurface.create_from_png("image/Flags/flags.png")
        context = cairo.Context(surface)
        context.translate(768*2,0)
        context.set_source_surface(source)
        context.mask_surface(mask)
        context.fill()

        surface.write_to_png("image/destination.png")


if __name__ == "__main__":
    Destination()