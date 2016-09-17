import cairo


class Template:
    def make(self, nx, ny, source1, source2, mask, res):
        dx = res[0] / (1.*nx)
        dy = res[1] / (1.*ny)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, res[0] * 4, res[1] * 2)
        context = cairo.Context(surface)
        context.set_source_surface(source1)
        context.mask_surface(mask)
        context.fill()
        context = cairo.Context(surface)
        context.translate(res[0] * 2, 0)
        context.set_source_surface(source2)
        context.mask_surface(mask)
        context.fill()
        return surface


if __name__ == "__main__":
    source1 = cairo.ImageSurface.create_from_png("image/source_20x30.png")
    source2 = cairo.ImageSurface.create_from_png("image/source_flags_20x30.png")
    mask = cairo.ImageSurface.create_from_png("image/mask_20x30.png")
    dest = Template()
    surface = dest.make(20, 30, source1, source2, mask)
    surface.write_to_png("image/template_20x30.png")
