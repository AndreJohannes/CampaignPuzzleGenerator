#!/usr/bin/python

import cairo
import numpy as np
import random
from gi.repository import Gtk
import json
import models


class Tiles:
    def __init__(self, grid):
        self.nx = grid.nx
        self.ny = grid.ny
        self.grid = grid.grid
        self.list = []
        self.pool = None
        self.field = self._make_field()
        for i in range(0, self.nx * self.ny):
            self._make_list()

    def get_path(self, i, j):
        path = list(self.grid[i][j]["r"])
        path.extend(self.grid[i + 1][j]["d"])
        path.extend(reversed(self.grid[i][j + 1]["r"]))
        path.extend(reversed(self.grid[i][j]["d"]))
        return path

    def _make_field(self):
        field = []
        for i in range(0, self.nx):
            strip = []
            for j in range(0, self.ny):
                strip.append("e")
            field.append(strip)
        return field

    def _make_list(self):
        if self.pool == None:
            self.pool = [(0, 0)]
            self.field[0][0] = "l"
        take = self.pool[random.randint(0, len(self.pool) - 1)]
        self.list.append(take)
        self.pool.remove(take)
        self._set_field(take[0], take[1], self.field)

    def _set_field(self, i, j, grid):
        if grid[i][j] == "l":
            grid[i][j] = "f"
            self._add_list(i - 1, j, grid)
            self._add_list(i + 1, j, grid)
            self._add_list(i, j - 1, grid)
            self._add_list(i, j + 1, grid)

    def _add_list(self, i, j, grid):
        if self.pool == None:
            self.pool = []
        if (i < 0 or i >= self.nx or j < 0 or j >= self.ny):
            return
        if grid[i][j] == "e":
            grid[i][j] = "l"
            self.pool.append((i, j))


class Grid:
    def __init__(self, res=(768, 1024)):
        self.nx = 20 #40
        self.ny = 20 #60
        grid = []
        for i in range(0, self.nx + 1):
            strip = []
            for j in range(0, self.ny + 1):
                p1 = (1. * i * res[0] / self.nx, 1. * j * res[1] / self.ny)
                p2 = (1. * (i + 1) * res[0] / self.nx, 1. * j * res[1] / self.ny)
                p3 = (1. * i * res[0] / self.nx, 1. * (j + 1) * res[1] / self.ny)
                strip.append({"r": [p1, p2] if j == 0 or j == self.ny else self._get_seq(p1, p2),
                              "d": [p1, p3] if i == 0 or i == self.nx else self._get_seq(p1, p3)})
            grid.append(strip)
        self.grid = grid

    def get_grid(self):
        return self.grid

    def _get_seq(self, p1, p2):
        X, Y = models.gp_puzzle_nub(steps=50)
        xy = np.array([X, (1 if random.random() < 0.5 else -1) * Y])

        a = np.array(p1)
        b = np.array(p2)

        r = np.linalg.norm(b - a)
        cosT, sinT = (b - a) / r
        R = np.array([[cosT, -sinT],
                      [sinT, cosT]])

        xy = a + r * np.dot(R, xy).T
        X = xy[:, 0]
        Y = xy[:, 1]
        return xy


class Example(Gtk.Window):
    def __init__(self):
        super(Example, self).__init__()
        self.image = cairo.ImageSurface.create_from_png("./image/bordado.png")
        self.tiles = Tiles(Grid())
        self.index = 0
        self.init_ui()
        with open('keys.json', 'w') as outfile:
            json.dump(self.tiles.list, outfile)

    def init_ui(self):
        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Complex shapes")
        self.resize(768, 1024)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_draw(self, wid, cr):
        self._draw(cr, self.index)

    def _draw(self, cr, index):
        cr.set_source_surface(self.image)
        cr.set_line_width(1.)
        for i in range(0, index):
            pos = self.tiles.list[i]
            self._add_path(self.tiles.get_path(pos[0], pos[1]), cr)
        cr.clip()
        cr.paint()
        # cr.get_target().write_to_png("./frames/frame{}.png".format(self.index))

    def _add_path(self, path, cr):
        first = True
        for point in path:
            if first:
                first = False
                cr.move_to(point[0], point[1])
            else:
                cr.line_to(point[0], point[1])

    def on_key_press_event(self, widget, event):
        print event.keyval
        if event.keyval == 65364:
            self.index += 1
        if event.keyval == 65362:
            self.index -= 1
            self.index = 0 if self.index < 0 else self.index
        if event.keyval == 115:
            self._save()
        if event.keyval == 103:
            self._save_grid()
        print "index: {}".format(self.index)
        widget.queue_draw()

    def _save(self):
        for i in range(0, self.tiles.nx * self.tiles.ny):
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768, 1024)
            context = cairo.Context(surface)
            context.rectangle(0, 0, 768, 1024)
            context.set_source_rgb(1, 1, 1)
            context.fill()
            context = cairo.Context(surface)
            self._draw(context, i)
            print "save: {}".format(i)
            surface.write_to_png("./frames/frame{}.png".format(i))

    def _save_grid(self):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 768, 1024)
            #context.set_source_rgb(1, 1, 1)
            #context.fill()
        context = cairo.Context(surface)
        context.set_line_width(1.)
        for i in range(0, self.tiles.nx*self.tiles.ny):
            pos = self.tiles.list[i]
            self._add_path(self.tiles.get_path(pos[0], pos[1]), context)
        context.stroke()
        print "save grid: {}".format(i)
        surface.write_to_png("./image/grid.png")

def main():
    random.seed(1)
    app = Example()
    app.connect('key_press_event', app.on_key_press_event)
    Gtk.main()


if __name__ == "__main__":
    main()
