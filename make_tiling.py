import random


class Tiling:
    def make(self, nx, ny, list):

        def mark_and_remove(pos, donor):
            if pool.count(pos) > 0:
                pool.remove(pos)
            else:
                print "ya: ", donor, pos
            for key in clusters:
                cluster = clusters[key]
                if cluster.count(pos) > 0:
                    cluster.remove(pos)
            array[pos[0]][pos[1]] = donor

        def add_neighbors(pos, cluster):
            def add(pos, cluster):
                if (pos[1] >= 0 and pos[1] < ny and pos[0] >= 0 and pos[0] < nx) and array[pos[0]][pos[1]] == None:
                    if cluster.count((pos)) < 1:
                        cluster.append(pos)

            add((pos[0] + 1, pos[1]), cluster)
            add((pos[0], pos[1] + 1), cluster)
            add((pos[0] - 1, pos[1]), cluster)
            add((pos[0], pos[1] - 1), cluster)

        random.seed(2)
        clusters = {}
        array = []
        pool = []
        for i in range(0, nx):
            row = []
            for j in range(0, ny):
                row.append(None)
                pool.append((i, j))
            array.append(row)

        for donor in list:
            if not clusters.has_key(donor["flag"]):
                clusters[donor["flag"]] = []
            cluster = clusters[donor["flag"]]
            for i in range(0, int(donor["amount"])/10):
                if len(cluster) > 0:
                    take = cluster[random.randint(0, len(cluster) - 1)]
                else:
                    take = pool[random.randint(0, len(pool) - 1)]
                mark_and_remove(take, donor)
                add_neighbors(take, cluster)

        return array


if __name__ == "__main__":
    tiling = Tiling()
    print tiling.make(10, 10, 3, [0, 1, 2, 2, 1, 0, 0])
