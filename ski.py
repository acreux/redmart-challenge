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


read_input("map.txt")

