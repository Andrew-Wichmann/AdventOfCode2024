import os
import sys
import typing as T
from copy import deepcopy
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
            puzzle = [l.strip() for l in f.readlines()]
        self.board: T.List[T.List[str]] = []
        for i in range(len(puzzle)):
            self.board.append([0]*len(puzzle[0]))
        for i, row in enumerate(puzzle):
            for j, square in enumerate(row):
                self.board[i][j] = square
                if square == guard:
                    self.guard_position = [j,i]

    def move(self, x, y):
        self.board[self.guard_position[1]][self.guard_position[0]] = visited
        self.guard_position[0] += x
        self.guard_position[1] += y
        if self.board[self.guard_position[1]][self.guard_position[0]] != visited:
            self.visited_count += 1
        self.board[self.guard_position[1]][self.guard_position[0]] = guard

    def __repr__(self):
        repr = ''
        for row in self.board:
            repr += ''.join(row)
            repr += '\n'
        return repr


class Guard():
    def __init__(self, board: Board):
        self.board = board
        self.orientation = Orientation.UP
        self.tail: T.List[T.List[T.List[str]]] = [[]]
        self.cycles = 0

    def walk(self):
        self.tail[0].append(deepcopy(self.board.guard_position))
        if len(self.tail) == 4 and self.board.guard_position in self.tail[3]:
            self.cycles += 1
        if self.orientation == Orientation.UP:
            self.board.move(0,-1)
        elif self.orientation == Orientation.DOWN:
            self.board.move(0,1)
        elif self.orientation == Orientation.RIGHT:
            self.board.move(1,0)
        elif self.orientation == Orientation.LEFT:
            self.board.move(-1,0)

    def turn(self):
        if len(self.tail) == 4:
            self.tail.pop(3)
        if len(self.tail) < 4:
            self.tail.insert(0, [])
        if self.orientation == Orientation.UP:
            self.orientation = Orientation.RIGHT
        elif self.orientation == Orientation.DOWN:
            self.orientation = Orientation.LEFT
        elif self.orientation == Orientation.RIGHT:
            self.orientation = Orientation.DOWN
        elif self.orientation == Orientation.LEFT:
            self.orientation = Orientation.UP

    @property
    def next(self):
        if self.orientation == Orientation.UP and self.board.guard_position[1] == 0:
            return None
        elif self.orientation == Orientation.RIGHT and self.board.guard_position[0] == len(self.board.board[0])-1:
            return None
        elif self.orientation == Orientation.DOWN and self.board.guard_position[1] == len(self.board.board)-1:
            return None
        elif self.orientation == Orientation.LEFT and self.board.guard_position[0] == 0:
            return None

        x,y = self.board.guard_position

        if self.orientation == Orientation.UP:
            return self.board.board[y-1][x]
        elif self.orientation == Orientation.RIGHT:
            return self.board.board[y][x+1]
        elif self.orientation == Orientation.DOWN:
            return self.board.board[y+1][x]
        elif self.orientation == Orientation.LEFT:
            return self.board.board[y][x-1]

    @property
    def position(self):
        self.board.guard_position

board = Board(sys.argv[1])
g = Guard(board)
i = 0
while g.next != None:
    if g.next == obstacle:
        g.turn()
    elif g.next in (empty, visited):
        g.walk()
    i += 1
print(g.cycles)
