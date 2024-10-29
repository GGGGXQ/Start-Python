from typing import NamedTuple, List
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint


Grid = [[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows, columns):
    return [[choice(ascii_uppercase) for _ in range(columns)] for _ in range(rows)]


def display_grid(grid):
    for row in grid:
        print("".join(row))


def generate_domain(word, grid):
    domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)
    for row in range(height):
        for col in range(width):
            columns = range(col, col + length + 1)
            rows = range(row, row + length + 1)
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            if row + length <= height:
                domain.append([GridLocation(r, col) for r in rows])
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain


class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words):
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment):
        all_locations = [locs for values in assignment.values() for locs in values]
        location_count = {}
        for loc in all_locations:
            location_count[loc] = location_count.get(loc, 0) + 1
        return all(count <= 1 for loc, count in location_count.items())


if __name__ == "__main__":
    grid = generate_grid(9, 9)
    words = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution = csp.back_tracking_search()
    if solution is None:
        print("No solution found")
    else:
            for word, grid_locations in solution.items():
                if choice([True, False]):
                    grid_locations.reverse()
                for index, letter in enumerate(word):
                    (row, col) = (grid_locations[index].row, grid_locations[index].column)
                    grid[row][col] = letter
            display_grid(grid)
