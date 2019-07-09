import tkinter as tk
from enum import Enum
import random
import copy
import time

class Cell(Enum):
    DEAD = 0
    ALIVE = 1

class ConwaysGameOfLife():
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols

        self.board = []
        for i in range(rows):
            self.board.append([])
            for j in range(cols):
                coin_flip = random.randint(0, 1)
                self.board[i].append(Cell.DEAD if coin_flip % 2 == 0 else Cell.ALIVE)

    def north(self, row: int, col: int):
        return (row, col-1)

    def east(self, row: int, col: int):
        return (row+1, col)

    def south(self, row: int, col: int):
        return (row, col+1)

    def west(self, row: int, col: int):
        return (row-1, col)

    def north_east(self, row: int, col: int):
        return (row+1, col-1)

    def south_east(self, row: int, col: int):
        return (row+1, col+1)

    def south_west(self, row: int, col: int):
        return (row-1, col+1)

    def north_west(self, row: int, col: int):
        return (row-1, col-1)

    def number_of_live_neighbors(self, board, row, col):
        live_neighbor_count = 0

        neighbors_to_check = [self.north, self.east, self.south, self.west, self.north_east, self.south_east, self.south_west, self.north_west]

        for neighbor_to_check in neighbors_to_check:
            neighbor = neighbor_to_check(row, col)
            if neighbor[0] >= 0 and neighbor[0] < self.rows and neighbor[1] >= 0 and neighbor[1] < self.cols:
                try:
                    if board[neighbor[0]][neighbor[1]] == Cell.ALIVE:
                        live_neighbor_count += 1
                except IndexError:
                    pass

        return live_neighbor_count

    def is_dead_underpopulation(self, board, row, column):
        """Any live cell with fewer than two live neighbours dies (referred to as underpopulation)."""

        if self.number_of_live_neighbors(board, row, column) < 2:
            return True
        else:
            return False

    def is_dead_overpopulation(self, board, row, column):
        """Any live cell with more than three live neighbours dies (referred to as overpopulation)."""

        if self.number_of_live_neighbors(board, row, column) > 3:
            return True
        else:
            return False

    def is_still_alive_unchanged(self, board, row, column):
        """Any live cell with two or three live neighbours lives, unchanged, to the next generation."""

        if self.number_of_live_neighbors(board, row, column) == 2 or self.number_of_live_neighbors(board, row, column) == 3:
            return True
        else:
            return False

    def is_now_alive(self, board, row, column):
        """Any dead cell with exactly three live neighbours will come to life."""

        if self.number_of_live_neighbors(board, row, column) == 3:
            return True
        else:
            return False

    def update_board(self):
        copy_board = copy.deepcopy(self.board)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == Cell.ALIVE:
                    if self.is_dead_underpopulation(self.board, row, col):
                        copy_board[row][col] = Cell.DEAD
                    elif self.is_dead_overpopulation(self.board, row, col):
                        copy_board[row][col] = Cell.DEAD
                    elif self.is_still_alive_unchanged(self.board, row, col):
                        pass # purposefully do nothing, remaining alive
                elif self.board[row][col] == Cell.DEAD:
                    if self.is_now_alive(self.board, row, col):
                        copy_board[row][col] = Cell.ALIVE

        self.board = copy_board

class Gui():
    def __init__(self, conways_game_of_life: ConwaysGameOfLife):
        self.conways_game_of_life = conways_game_of_life
        self.labels = []

    def refresh(self):
        self.conways_game_of_life.update_board()

        for row in range(self.conways_game_of_life.rows):
            for column in range(self.conways_game_of_life.cols):
                self.labels[row][column].configure(background="Black" if self.conways_game_of_life.board[row][column] == Cell.ALIVE else "White")

        self.root_window.after(150, self.refresh)

    def start(self):
        self.root_window = tk.Tk()
        self.root_window.title("Grehg's Game of Life")

        if len(self.labels) == 0:
            for row in range(self.conways_game_of_life.rows):
                self.labels.append([])
                for column in range(self.conways_game_of_life.cols):
                    label = tk.Label(self.root_window, height=1, width=1, background="Black" if self.conways_game_of_life.board[row][column] == Cell.ALIVE else "White")
                    self.labels[row].append(label)

                    label.grid(row=row, column=column)

        self.refresh()
        self.root_window.mainloop()
conways_game_of_life = ConwaysGameOfLife(rows=30, cols=60)
gui = Gui(conways_game_of_life)
gui.start()
