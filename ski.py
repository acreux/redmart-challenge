import itertools


def read_input(file_name):
    with open(file_name, 'r') as f_input:
        # first line
        size_grid = f_input.next().split(" ")
        size_grid = [int(i) for i in size_grid]

        rows_count = size_grid[0]
        ski_map = [r.strip().split(" ") for r in f_input]
        ski_map_flatten = [i for i in itertools.chain(*ski_map)]
        print(len(ski_map_flatten))


class Map(object):

    def __init__(self, ski_map):

        self.ground_map = ski_map
        self.ground_map_flattened = [Point(ind, int(i)) for ind, i in enumerate(itertools.chain(*ski_map))]
        self.row_count = len(self.ground_map)

    def north(self, pos):
        if pos-self.row_count>=0:
            return self.ground_map_flattened[pos-self.row_count]
        return None

    def south(self, pos):
        if pos+self.row_count<self.row_count**2:
            return self.ground_map_flattened[pos+self.row_count]
        return None

    def west(self, pos):
        if pos%self.row_count != 0:
            return self.ground_map_flattened[pos-1]
        return None

    def east(self, pos):
        if pos % self.row_count != self.row_count-1:
            return self.ground_map_flattened[pos+1]
        return None
    
    def get_all_higher_neighbors(self, pos):
        higher_neighbors = []
        pos_elevation = self.ground_map_flattened[pos].elevation
        if north(pos) and north(pos).elevation > value:
            higher_neighbors.append(self.ground_map_flattened[pos])
        if south(pos) and south(pos).elevation > value:
            higher_neighbors.append(self.ground_map_flattened[pos])
        if west(pos) and west(pos).elevation > value:
            higher_neighbors.append(self.ground_map_flattened[pos])
        if east(pos) and east(pos).elevation > value:
            higher_neighbors.append(self.ground_map_flattened[pos])
        return higher_neighbors

    def get_max_score_neighbors(self, pos):
        higher_neighbors = self.get_all_higher_neighbors(pos)
        best_neighbor = max(higher_neighbors, key=lambda x: x.path_length)
        return best_neighbor

    def update_pos(self, pos):
        point = self.ground_map_flattened[pos]
        best_neighbor = self.get_max_score_neighbors(pos)

        point.path_length = best_neighbor.path_length + 1
        point.path_drop = best_neighbor.path_drop + (best_neighbor.elevation - point.elevation)

    def solve(self):
        for i in self.ground_map_flattened:
            update_pos(i)

class Point(object):

    def __init__(self, pos, elevation, path_length=0, path_drop=0):
        self.pos = pos
        self.elevation = elevation
        self.path_length = path_length
        self.path_length = path_length
        self.path_drop = path_drop

    def __str__(self):
        return "\n".join([
            "pos:" + str(self.pos),
            "elevation:" + str(self.elevation),
            "path_length:" + str(self.path_length),
            "path_drop:" + str(self.path_drop)]) + "\n"


# 1 2 3
# 4 5 6
# 7 8 9
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = Map(l)
print(m.north(4))
print(m.south(4))
print(m.west(4))
print(m.east(4))
print(m.north(3))
print(m.south(3))
print(m.west(3))
print(m.east(3))

read_input("map.txt")

