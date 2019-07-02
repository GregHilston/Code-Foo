import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
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

        if self.number_of_live_neighbors(board, row, column) <= 2:
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
                        pass # purposefully do nothing
                elif self.board[row][col] == Cell.DEAD:
                    if self.is_now_alive(self.board, row, col):
                        copy_board[row][col] = Cell.ALIVE

        self.board = copy_board

class Gui():
    def __init__(self, conways_game_of_life: ConwaysGameOfLife):
        self.conways_game_of_life = conways_game_of_life

    def to_ui(self):
        ui_board = [[]]

        for row in range(self.conways_game_of_life.rows):
            columns = []
            for col in range(self.conways_game_of_life.cols):
                columns.append(
                    sg.Text(
                        size=(10, 1),
                        pad=(1, 1),
                        justification='right',
                        key=(row,col),
                        text=" ",
                        background_color= "White" if self.conways_game_of_life.board[row][col] == Cell.DEAD else "Black"
                    )
                )
            ui_board.append([sg.T('{}'.format(row), size=(4,1), justification='right')] + columns)
        return ui_board

    def start(self):
        sg.SetOptions(element_padding=(0,0))

        while True:
            columm_layout = self.to_ui()

            layout = [ [sg.T("Conway's Game of Life", font='Any 18')],
                    [sg.Column(columm_layout, size=(800,600), scrollable=True)] ]

            window = sg.Window('Table', return_keyboard_events=True).Layout(layout)


            #event, values = window.Read()
            event, values = window.Read(timeout = 1000)

            # window.Close()

            self.conways_game_of_life.update_board()
            time.sleep(1)

conways_game_of_life = ConwaysGameOfLife()
gui = Gui(conways_game_of_life)
gui.start()
