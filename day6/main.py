import sys
import typing as T
from enum import Enum

obstacle = "#"
empty = "."
visited = "$"
guard = "^"

class Orientation(Enum):
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"

class Board():
    def __init__(self, puzzle_file):
        with open(puzzle_file, "r") as f:
            puzzle = f.readlines()
        self.board: T.List[T.List[str]] = [[0]*len(puzzle[0])]*len(puzzle)
        for i, row in enumerate(puzzle):
            self.board.append([])
            for j, square in enumerate(row):
                self.board[i][j] = square
                if square == guard:
                    self.guard_position = (i,j)

class Guard():
    def __init__(self, board: Board):
        self.board = board
        self.orientation = Orientation.UP

    def walk(self):
        self.board

    def turn(self):
        pass

    def next(self):
        pass

    @property
    def position(self):
        self.board.guard_position

board = Board(sys.argv[1])
print(board.guard_position)
g = Guard()
g.walk()

#while guard.next != None:
#    if guard.next == obstacle:
#        guard.turn()
#    elif guard.next in (empty, visited):
#        guard.walk()
#
#    if guard.position != visited:
#        board.mark_visited(guard.position)
