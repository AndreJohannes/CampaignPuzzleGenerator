import cairo

from tools.tiles import Tiles, Grid


class Puzzle:
    def __init__(self):
        nx = 20
        ny = 30
        self.tiles = Tiles(Grid(nx, ny))
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768 * 2, 1024 * 2)
        context = cairo.Context(surface)
        context.set_source_rgb(1, 1, 1)
        dx = 768 / nx
        dy = 1024 / ny
        for i in range(0, nx):
            for j in range(0, ny):
                self._add_path([[path[0] + i * dx+dx/2, path[1] + j * dy+dy/2] for path in self.tiles.get_path(i, j)], context)
        context.clip()
        context.paint()
        surface.write_to_png("image/template.png")

    def _add_path(self, path, cr):
        first = True
        for point in path:
            if first:
                first = False
                cr.move_to(point[0], point[1])
            else:
                cr.line_to(point[0], point[1])


if __name__ == "__main__":
    Puzzle()
