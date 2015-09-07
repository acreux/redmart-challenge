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
        for direction in [self.north, self.south, self.west, self.east]:
            if direction(pos) and direction(pos).elevation > pos_elevation:
                higher_neighbors.append(direction(pos))
        return higher_neighbors

    def get_max_score_neighbors(self, pos):
        higher_neighbors = self.get_all_higher_neighbors(pos)
        for i in higher_neighbors:
            print("i")
            print(i)
        if higher_neighbors:
            # We take the longest path
            # If equal, we take the longest drop (current drop + elevation)
            best_neighbor = max(higher_neighbors, key=lambda x: (x.path_length, x.path_drop+x.elevation))
            print(pos)
            print(best_neighbor)
            return best_neighbor
        else:
            return None

    def update_pos(self, pos):
        best_neighbor = self.get_max_score_neighbors(pos)
        if not best_neighbor:   # Highest point among its neighbour
            return False

        point = self.ground_map_flattened[pos]

        point.path_length = best_neighbor.path_length + 1
        point.path_drop = best_neighbor.path_drop + (best_neighbor.elevation - point.elevation)
        return True

    def solve(self):
        finished = False
        for i in range(10):
        # while(not finished):
            finished = True
            for ind, _ in enumerate(self.ground_map_flattened):
                self.update_pos(ind)

    def __str__(self):
        return "\n".join(i.__str__() for i in self.ground_map_flattened)

class Point(object):

    def __init__(self, pos, elevation, path_length=1, path_drop=0):
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


# 4 8 7 3
# 2 5 9 3
# 6 3 2 5
# 4 4 1 6
l = [[4,8,7,3], [2,5,9,3], [6,3,2,5], [4,4,1,6]]
m = Map(l)
# print(m.north(4))
# print(m.south(4))
# print(m.west(4))
# print(m.east(4))
# print(m.north(3))
# print(m.south(3))
# print(m.west(3))
# print(m.east(3))


m.solve()
print "solved"
print(m)


read_input("map.txt")

