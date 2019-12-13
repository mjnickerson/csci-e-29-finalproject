from tkinter import *
from lui_gui.guicommands import generate_graph, run_graph


lui_gui_window = Tk()


graph_name = "" #what the entire graph should be called

# NEED TO GIVE A NAME TO EACH LUIGI BLOCK TO ADD IN COOKIE CUTTER!

# THIS IS WHERE CLASSES GET INVOLVED

# NEED A PLACE UNDER S3 TO ENTER CREDENTIALS -or- ENTER A DOT ENV
# CREDENTIALS SHOULD APPEAR AS ************

# COLORS OF REQUIRED LABELS
Label(lui_gui_window, text="LuiGUI", fg="black", bg="lightgrey", font="Verdana 14 bold").pack()

Label(lui_gui_window, text="S3 Target", fg="black", bg="lavender", font="Verdana 14 bold").pack()

Label(lui_gui_window, text="External Task", fg="black", bg="skyblue", font="Verdana 14 bold").pack()

Label(lui_gui_window, text="Task", fg="white", bg="blue", font="Verdana 14 bold").pack()

Label(lui_gui_window, text="External Program Task", fg="black", bg="skyblue", font="Verdana 14 bold").pack()

Label(lui_gui_window, text="Local Target", fg="black", bg="lavender", font="Verdana 14 bold").pack()

Label(lui_gui_window, text="Wrapper Task", fg="black", bg="orange", font="Verdana 14 bold").pack()


but_generate = Button(lui_gui_window, text="Generate Graph!", command=generate_graph)
#but_generate.place(relx=0.5, rely=0.5, anchor=CENTER)
but_generate.pack()

but_run = Button(lui_gui_window, text="Run Graph!", command=run_graph)
#but_run.place(relx=0.5, rely=0.5, anchor=CENTER)
but_run.pack()

mainloop()