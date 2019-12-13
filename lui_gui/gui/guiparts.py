from tkinter import *

def blank_node_box(window, box_start, box_end, node_col, node_wid, nod_color):
    for row_blank in range(box_start, (box_end+1), 1):  # blank header
        Label(window, text=" ", fg="black", bg=node_col, width=node_wid, font="Verdana 14 bold").grid(
            row=row_blank, column=nod_color, sticky=W)  # blank