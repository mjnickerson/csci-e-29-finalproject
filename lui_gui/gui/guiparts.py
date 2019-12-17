from tkinter import *
from tkinter import messagebox
from random import *


def blank_node_box(window, box_start, box_end, node_col, node_wid, nod_color):
    for row_blank in range(box_start, (box_end+1), 1):  # blank header
        Label(window, text=" ", fg="black", bg=node_col, width=node_wid, font="Verdana 14 bold").grid(
            row=row_blank, column=nod_color, sticky=W)  # blank

def blank_ground(window, gnd_color, start_gnd, end_gnd, buffer_width, nm_cols, nm_width, lng_cols, lng_width, but_width):
    for row_blank in range(start_gnd, (end_gnd + 1), 1):  # blankrows at bottom
        for column in range (0,(10+1),2): # for buffer columns/seperators
                Label(window, text=" ", fg="black", bg=gnd_color, width=buffer_width, font="Verdana 14 bold").grid(
                row=row_blank, column=column, sticky=W)  # blank
        for column in nm_cols: #for narrow columns
            Label(window, text=" ", fg="black", bg=gnd_color, width=nm_width, font="Verdana 14 bold").grid(
            row=row_blank, column=column, sticky=W)  # blank
        Label(window, text=" ", fg="black", bg=gnd_color, width=lng_width, font="Verdana 14 bold").grid(
        row=row_blank, column=lng_cols, sticky=W)  # blank
        Label(window, text=" ", fg="black", bg=gnd_color, width=but_width, font="Verdana 14 bold").grid(
        row=row_blank, column=13, sticky=W)  # blank


class credits_window:
    """
    Project Credits Window
    With Demo to Test GUI Functions
    """
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.textcolor = "white"
        self.background = "black"

        self.master_window = Toplevel(self.parent_window)
        self.master_window.title("Pack it up, pack it in, let me begin")
        self.master_window.configure(background="black")
        self.master_window.geometry("435x435")

        self.label1 = Label(self.master_window, text="So get out your seat and jump around!", fg=self.textcolor, bg=self.background).pack()
        self.mainlabel = Label(self.master_window, text="LuiGUI", fg=self.textcolor, bg=self.background, font="Times 80 bold")
        self.mainlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.sublabel = Label(self.master_window, text="a demo graphic user interface to generate luigi graphs using metaprogramming", fg=self.textcolor, bg=self.background)
        self.sublabel.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.versionlab = Label(self.master_window, text="Version 1.0.0 ALPHA", fg=self.textcolor, bg=self.background)
        self.versionlab.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.label2 = Label(self.master_window, text="PROJECT CREDITS:", fg=self.textcolor, bg=self.background)
        self.label2.place(relx=0.03, rely=0.90, anchor=W)
        self.label3 = Label(self.master_window, text="ADV. PYTHON - CSCI-E-29 FINAL PROJECT - FALL 2019 - MICAH NICKERSON", fg=self.textcolor, bg=self.background)
        self.label3.place(relx=0.5, rely=0.95, anchor=CENTER)

        self.b = Button(self.master_window, text="Jump Around!", command=self.jump)
        self.b.place(relx=0.4, rely=0.10, anchor=CENTER)
        self.btoo = Button(self.master_window, text="Get Down!", command=self.get_down)
        self.btoo.place(relx=0.6, rely=0.10, anchor=CENTER)

    def get_down(self):
        print("\nJump Up,\nJump Up,\nand Get Down!\n")
        self.btoo.place(relx=0.6, rely=0.85, anchor=CENTER)

    def jump(self):
        print("")
        print("Jump!")
        self.mainlabelweak = Label(self.master_window, text="LuiGUI", fg="dark slate grey", bg=self.background, font="Times 80 bold")
        self.mainlabelweak.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label2.destroy()
        self.mainlabel.destroy()
        self.sublabel.destroy()
        self.versionlab.destroy()
        self.label3.destroy()
        self.b.place(relx=random(), rely=random())


def warning_graph_exists():
    print("\nGraph Already Exists!")
    messagebox.showinfo("Warning!", "Cannot create Graph - that folder already exists!")


def warning_no_folder():
    print("\nThat folder does not exist!")
    messagebox.showinfo("Warning!", "Cannot destroy Graph - that folder does not exist!")

def warning_no_graph():
    print("\nCannot Run: Graph does not exist")
    messagebox.showinfo("Warning!", "Cannot Run Graph - it does not exist!")

def warning_task_missing():
    print("\nCannot Run: Task is missing main script")
    messagebox.showinfo("Warning!", "Cannot Run Graph - TASK is missing a script!\n\nExternalProgramTask can be left blank, but Task MUST have a script to execute.")

def warning_node_name_missing():
    print("\nCannot Run: Node Name is Empty")
    messagebox.showinfo("Warning!", "Cannot Run Graph - a Required Node Name is Empty!")

def warning_output_target_missing():
    print("\nCannot Run: Required Target is not Specified")
    messagebox.showinfo("Warning!", "Cannot Run Graph - Required Target is NOT specified!")