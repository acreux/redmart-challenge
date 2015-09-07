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
        self.ground_map_flattened = [i for i in itertools.chain(*ski_map)]
        self.row_count = len(self.ground_map)

    def north(self, pos):
        if pos-self.row_count>=0:
            return self.ground_map_flattened[pos-self.row_count]
        return None

    def south(self, pos):
        if pos+self.row_count<1000**2:
            return self.ground_map_flattened[pos+self.row_count]
        return None

    def west(self, pos):
        if pos%self.row_count != 0:
            return self.ground_map_flattened[pos-1]
        return None

    def east(self, pos):
        if pos % self.row_count != 999:
            return self.ground_map_flattened[pos+1]
        return None



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

