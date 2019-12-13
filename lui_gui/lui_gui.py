from tkinter import *
from gui.guiparts import blank_node_box
from gui.guicommands import generate_graph, run_graph


#local GUI Functions
def clicked(): #TEST CLICK FUNCTION
    entered_text = textentry.get()
    if entered_text:
        print("The value is %s." % str(entered_text))
    else:
        print("Nothing was entered.")

def close_gui(): #exit function
    lui_gui_window.destroy()
    exit()

#declare gui_window
lui_gui_window = Tk()
lui_gui_window.title("LuiGUI - a io powerup")
lui_gui_window.configure(background="grey")
lui_gui_window.geometry("1630x410")

############################################

#properties
graph_name = "New Graph"

#viz settings
node_width = 15 #column width
node_start = 3 #row
node_end = 13 #row
nm_cols = [3,5,9,11]
lng_cols = 7
field_color = "white"

############################################
textentry = Entry(lui_gui_window, width=5, bg="magenta")
############################################
#header
Label(lui_gui_window, text="LuiGUI", fg="black", bg="lightgrey", font="Verdana 14 bold", width=node_width).grid(row=0, column=1, sticky=W)

#blank header
for column_blank in range(0,12,2): # blank header
    Label(lui_gui_window, text="", fg="black", bg="lightgrey", width=4, font="Verdana 14 bold").grid(row=0, column=column_blank, sticky=W)
for column_blank in nm_cols: # blank header
    Label(lui_gui_window, text="", fg="black", bg="lightgrey", width=node_width, font="Verdana 14 bold").grid(row=0, column=column_blank, sticky=W)
Label(lui_gui_window, text="", fg="black", bg="lightgrey", width=20, font="Verdana 14 bold").grid(row=0, column=lng_cols, sticky=W)

# file load label
Label(lui_gui_window, text="        Graph Name:", fg="black", bg="lightgrey", width=node_width, font="Verdana 14 bold").grid(row=0, column=3, sticky=E)

# Label(lui_gui_window, text=("'%s'" % str(graph_name)), fg="black", bg="lightgrey", width=node_width, font="Verdana 14 bold").grid(row=0, column=5, sticky=W)
graph_name_entry = Entry(lui_gui_window, width=node_width, bg="lightgrey", font="Verdana 14 bold")
graph_name_entry.grid(row=0, column=5)
graph_name_entry.insert(END, graph_name)

#arrows
for column_blank in range(2,10,2): # blank header
    Label(lui_gui_window, text=" > ", fg="black", bg="lightgrey", font="Verdana 20 bold").grid(row=8, column=column_blank, sticky=W)

#node 1
node_column = 1
node_width = 15
node_color = "lavender"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="S3Target", fg="black", bg=node_color, font="Verdana 14 bold", width=node_width).grid(row=3, column=node_column, sticky=W)
#Label(lui_gui_window, text=" ", fg="black", bg=node_color, font="Verdana 14 bold", width=node_width).grid(row=4, column=node_column, sticky=W) #blank
node1_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node1_name.grid(row=4, column=node_column)
node1_name.insert(END, ' Node 1 ')
Label(lui_gui_window, text="Boto Credentials:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
Label(lui_gui_window, text="Access ID:", fg="black", bg=node_color, font="Verdana 10 italic", width=node_width).grid(row=6, column=node_column, sticky=W)
node_1_aws_access_id = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold")
node_1_aws_access_id.grid(row=7, column=node_column)
node_1_aws_access_id.insert(END, ' > ')
Label(lui_gui_window, text="Secret Key:", fg="black", bg=node_color, font="Verdana 10 italic", width=node_width).grid(row=8, column=node_column, sticky=W)
node_1_aws_secret_key = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold")
node_1_aws_secret_key.grid(row=9, column=node_column)
node_1_aws_secret_key.insert(END, ' > ')
Label(lui_gui_window, text=" ", fg="black", bg=node_color, font="Verdana 14 bold").grid(row=10, column=node_column, sticky=W) #blank
Label(lui_gui_window, text=" S3 Target Address:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)
node1_target_entry = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold")
node1_target_entry.insert(END, ' s3:// ')
node1_target_entry.grid(row=12, column=node_column) #note: cannot combine these together functionally, or the Entry will return None

#node 2
node_column = 3
node_width = 15
node_color = "lightblue"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="External Task", fg="black", bg=node_color, width=node_width, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node2_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node2_name.grid(row=4, column=node_column)
node2_name.insert(END, ' Node 2 ')
Label(lui_gui_window, text="Params:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
Label(lui_gui_window, text="Output:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)

#node 3
node_column = 5
node_width = 15
node_color = "blue"
fg_color= "white"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="Task", fg=fg_color, bg=node_color, width=node_width, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node3_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, fg=fg_color, font="Verdana 12")
node3_name.grid(row=4, column=node_column)
node3_name.insert(END, ' Node 3 ')
Label(lui_gui_window, text="Params:", fg=fg_color, bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
Label(lui_gui_window, text="Run:", fg=fg_color, bg=node_color, font="Verdana 12", width=node_width).grid(row=7, column=node_column, sticky=W)
node3_run_target = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, fg="white", font="Verdana 8 bold")
node3_run_target.insert(END, ' > ')
node3_run_target.grid(row=8, column=node_column)
Label(lui_gui_window, text="Output Folder:", fg=fg_color, bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)
node3_output_folder = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, fg="white", font="Verdana 8 bold")
node3_output_folder.insert(END, ' ../')
node3_output_folder.grid(row=12, column=node_column)


#node 4
node_column = 7
node_width = 20
node_color = "lightblue"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="External Program Task", width=node_width, fg="black", bg=node_color, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node4_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node4_name.grid(row=4, column=node_column)
node4_name.insert(END, ' Node 4 ')
Label(lui_gui_window, text="Params:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
Label(lui_gui_window, text="CLI Arguments:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=7, column=node_column, sticky=W)
node4_run_target= Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold")
node4_run_target.insert(END, ' > ')
node4_run_target.grid(row=8, column=node_column)
Label(lui_gui_window, text="Output:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)

#node 5
node_column = 9
node_width = 15
node_color = "lavender"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="Local Target", width=node_width, fg="black", bg=node_color, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node5_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node5_name.grid(row=4, column=node_column)
node5_name.insert(END, ' Node 5 ')
Label(lui_gui_window, text="Params:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
Label(lui_gui_window, text="Folder:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=7, column=node_column, sticky=W)
node5_target_output = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold")
node5_target_output.insert(END, '  ../ ')
node5_target_output.grid(row=8, column=node_column)
Label(lui_gui_window, text="Output:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)


# Execution Buttons
but_exit = Button(lui_gui_window, text="> Exit < ", command=close_gui)
but_exit.grid(row=2, column=11, sticky=W)

but_generate = Button(lui_gui_window, text="> Generate Graph! <", font="Verdana 10 bold", command=generate_graph)
but_generate.grid(row=10, column=11, sticky=W)

but_run = Button(lui_gui_window, text="> Run Graph! <", font="Verdana 10 bold", command=run_graph)
but_run.grid(row=12, column=11, sticky=W)

#run interface
mainloop()