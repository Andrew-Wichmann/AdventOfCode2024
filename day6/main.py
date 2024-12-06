import sys
import typing as T
from enum import Enum

obstacle = "#"
empty = "."
visited = "$"
guard = "^"

class Orientation(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Board():
    def __init__(self, puzzle_file):
        self.visited_count = 0
        with open(puzzle_file, "r") as f:
            puzzle = f.readlines()
        self.board: T.List[T.List[str]] = [[0]*len(puzzle[0])]*len(puzzle)
        for i, row in enumerate(puzzle):
            self.board.append([])
            for j, square in enumerate(row):
                self.board[i][j] = square
                if square == guard:
                    self.guard_position = [i,j]

    def move(self, x, y):
        self.guard_position[0] += x
        self.guard_position[1] += y
        if self.board[self.guard_position[0]][self.guard_position[1]] != visited:
            self.board[self.guard_position[0]][self.guard_position[1]] = visited
            self.visited_count += 1



class Guard():
    def __init__(self, board: Board):
        self.board = board
        self.orientation = Orientation.UP

    def walk(self):
        if self.orientation == Orientation.UP:
            self.board.move(0,-1)
        elif self.orientation == Orientation.DOWN:
            self.board.move(0,1)
        elif self.orientation == Orientation.RIGHT:
            self.board.move(1,0)
        elif self.orientation == Orientation.LEFT:
            self.board.move(-1,0)

    def turn(self):
        pass

    def next(self):
        pass

    @property
    def position(self):
        self.board.guard_position

board = Board(sys.argv[1])
g = Guard(board)
print(board.guard_position)
g.walk()
print(board.guard_position)
g.orientation = Orientation.DOWN
g.walk()
print(board.guard_position)
g.orientation = Orientation.RIGHT
g.walk()
print(board.guard_position)

#while guard.next != None:
#    if guard.next == obstacle:
#        guard.turn()
#    elif guard.next in (empty, visited):
#        guard.walk()
#
#    if guard.position != visited:
#        board.mark_visited(guard.position)
