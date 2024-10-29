from typing import NamedTuple, List, Dict
from csp import CSP, Constraint
from random import choice
from string import ascii_uppercase


class ComponentLocation(NamedTuple):
    row: []
    column: []


class Component:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.letter = choice(ascii_uppercase)


def generate_board(rows, columns):
    return [["*" for _ in range(columns)] for _ in range(rows)]


def display_board(board):
    for row in board:
        print("".join(row))


def generate_domain(component, board):
    domain = []
    height = len(board)
    width = len(board[0])
    c_width = component.columns
    c_height = component.rows
    for row in range(height):
        for col in range(width):
            if col + c_width <= width and row + c_height <= height:
                domain.append([ComponentLocation([r], [c]) for r in range(row, row + c_height)
                               for c in range(col, col + c_width)])
    return domain


class BoardConstraint(Constraint):
    def __init__(self, components):
        super().__init__(components)
        self.components = components

    def satisfied(self, assignment: Dict[ComponentLocation, ComponentLocation]) -> bool:
        occupied = set()
        for component, locations in assignment.items():
            for loc in locations:
                for row in loc.row:
                    for col in loc.column:
                        if (row, col) in occupied:
                            return False
                        occupied.add((row, col))
        return True


if __name__ == '__main__':
    MAX_BOARD_WIDTH = 10
    MAX_BOARD_HEIGHT = 10

    grid = generate_board(MAX_BOARD_HEIGHT, MAX_BOARD_WIDTH)
    components = [
        Component(2, 3),
        Component(3, 5),
        Component(1, 4),
        Component(2, 4)
    ]
    locations = {}
    for component in components:
        locations[component] = generate_domain(component, grid)
    csp = CSP(components, locations)
    csp.add_constraint(BoardConstraint(components))
    solution = csp.back_tracking_search()
    if solution is None:
        print("No solution found")
    else:
        for component, location in solution.items():
            for locs in location:
                for row in locs[0]:
                    for column in locs[1]:
                        grid[row][column] = component.letter
        display_board(grid)
