import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
from enum import Enum
import random

class Cell(Enum):
    DEAD = 0
    ALIVE = 1

class Table():
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols

        self.board = []
        for i in range(rows):
            self.board.append([])
            for j in range(cols):
                coin_flip = random.randint(0, 1)
                print(coin_flip)
                self.board[i].append(Cell.DEAD if coin_flip % 2 == 0 else Cell.ALIVE)

class Simulator():
    def __init__(self, table: Table):
        self.table = table

    def domain_model_to_ui(self):
        ui_board = [[]]

        for row in range(self.table.rows):
            columns = []
            for col in range(self.table.cols):
                columns.append(
                    sg.Text(
                        size=(10, 1),
                        pad=(1, 1),
                        justification='right',
                        key=(row,col),
                        text=" ",
                        background_color= "Black" if self.table.board[row][col] == Cell.DEAD else "White"
                    )
                )
            ui_board.append([sg.T('{}'.format(row), size=(4,1), justification='right')] + columns)
        return ui_board

    def start(self):
        sg.SetOptions(element_padding=(0,0))

        columm_layout = self.domain_model_to_ui()

        layout = [ [sg.T("Conway's Game of Life", font='Any 18')],
                [sg.Column(columm_layout, size=(800,600), scrollable=True)] ]

        window = sg.Window('Table', return_keyboard_events=True).Layout(layout)

        while True:
            event, values = window.Read()

table = Table()
simulator = Simulator(table)
simulator.start()