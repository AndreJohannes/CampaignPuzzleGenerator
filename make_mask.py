import cairo

from tools.tiles import Tiles, Grid


class Mask:
    def make(self, nx, ny, res = (768, 1024)):
        self.tiles = Tiles(Grid(nx, ny, res))
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 2 * res[0], 2 * res[1])
        context = cairo.Context(surface)
        context.set_source_rgb(1, 1, 1)
        dx = res[0] / (1.*nx+0.0)
        dy = res[1] / (1.*ny+0.0)
        print dx, dy
        for i in range(0, nx):
            for j in range(0, ny):
                self._add_path(
                    [[path[0] + i * dx + dx / 2, path[1] + j * dy + dy / 2] for path in self.tiles.get_path(i, j)],
                    context)
        context.clip()
        context.paint()
        return surface

    def _add_path(self, path, cr):
        first = True
        for point in path:
            if first:
                first = False
                cr.move_to(point[0], point[1])
            else:
                cr.line_to(point[0], point[1])


if __name__ == "__main__":
    mask = Mask()
    nx = 30
    ny = 40
    surface = mask.make(nx, ny, (733, 915))
    surface.write_to_png("./image/mask_{}x{}.png".format(nx,ny))
