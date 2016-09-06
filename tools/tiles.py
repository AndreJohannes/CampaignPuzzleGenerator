import random
import numpy as np
from tools import models

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
        path = list([(x[0]+0.5, x[1]+0.5) for x in self.grid[i][j]["r"]])
        path.extend(self.grid[i + 1][j]["d"])
        path.extend(reversed(self.grid[i][j + 1]["r"]))
        path.extend([(x[0]+0.5, x[1]+0.5) for x in reversed(self.grid[i][j]["d"])])
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
    def __init__(self, nx, ny, res=(768, 1024)):
        self.nx = nx
        self.ny = ny
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