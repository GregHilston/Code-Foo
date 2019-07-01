#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


def TableSimulation():
    """
    Display data in a table format
    """
    sg.SetOptions(element_padding=(0,0))

    columm_layout = [[]]

    MAX_ROWS = 20
    MAX_COL = 10
    for i in range(MAX_ROWS):
        inputs = [sg.T('{}'.format(i), size=(4,1), justification='right')] + [sg.Text(size=(10, 1), pad=(1, 1), justification='right', key=(i,j), text=" ", background_color="White") for j in range(MAX_COL)]
        columm_layout.append(inputs)

    layout = [ [sg.T("Conway's Game of Life", font='Any 18')],
               [sg.Column(columm_layout, size=(800,600), scrollable=True)] ]

    window = sg.Window('Table', return_keyboard_events=True).Layout(layout)

    while True:
        event, values = window.Read()

TableSimulation()