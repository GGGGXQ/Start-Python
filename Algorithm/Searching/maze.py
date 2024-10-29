from enum import Enum
from typing import NamedTuple
import random
from math import sqrt
from generic_search import dfs, node_to_path, bfs, astar


class Cell(str, Enum):
    EMPTY = ""
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        self._rows = rows
        self._columns = columns
        self.start_position = start
        self.goal_position = goal
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fil(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fil(self, rows, columns, sparseness):
        for row in range(rows):
            for col in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED

    def goal_test(self, ml):
        return ml == self.goal_position

    def mark(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start_position.row][self.start_position.column] = Cell.START
        self._grid[self.goal_position.row][self.goal_position.column] = Cell.GOAL

    def clear(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start_position.row][self.start_position.column] = Cell.START
        self._grid[self.goal_position.row][self.goal_position.column] = Cell.GOAL

    def successors(self, ml):
        location = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            location.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            location.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            location.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            location.append(MazeLocation(ml.row, ml.column - 1))
        return location

    def __str__(self) -> str:
        output = ""
        for row in self._grid:
            output = "".join([c.value for c in row]) + "\n"
        return output


def euclidean_distance(goal):
    def calculate_distance(ml):
        x_dist = ml.column - goal.column
        y_dist = ml.row - goal.row
        return sqrt(x_dist**2 + y_dist**2)
    return calculate_distance


def manhattan_distance(goal):
    def calculate_distance(ml):
        x_dist = ml.column - goal.column
        y_dist = ml.row - goal.row
        return x_dist + y_dist
    return calculate_distance


if __name__ == "__main__":
    maze = Maze()
    print(maze)
    solution1 = dfs(maze.start_position, maze.goal_test, maze.successors)
    if solution1 is None:
        print("No solution found using depth-first search")
    else:
        path1 = node_to_path(solution1)
        maze.mark(path1)  
        print(maze)
        maze.clear(path1)

    solution2 = bfs(maze.start_position, maze.goal_test, maze.successors)
    if solution2 is None:
        print("No solution found using breadth first search")
    else:
        path2 = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)

    distance = manhattan_distance(maze.goal_position)
    solution3 = astar(maze.start_position, maze.goal_test, maze.successors, distance)
    if solution3 is None:
        print("No solution found using a* search")
    else:
        path3 = node_to_path(solution3)
        maze.mark(path3)
        print(maze)
        maze.clear(path3)
