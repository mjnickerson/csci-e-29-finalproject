import os
from tkinter import *


"""
This py file is a library of Graphic Interface commands that run LuiGUI.
"""

def test_script(): #TEST BUTTON FUNCTION
    print("Testing this script")
    for i in range(1,20,1):
        print(i," Mississippi")


def test_clicked(): #TEST CLICK FUNCTION
    """
    This is a test function, that will be abandoned.
    """
    entered_text = textentry.get()
    if entered_text:
        print("\nThe value is %s." % str(entered_text))
    else:
        print("\nNothing was entered.")


def update_field(fieldname,newmessage):
    fieldname.delete(0, END) #clear existing root declaration
    fieldname.insert(END, str(newmessage)) #add new text


def graph_path(path_entry, name_entry):
    """
    :param path_entry: Entry field, for root path, holding a value to get()
    :param name_entry: Entry field, for graph directory name, holding a value to get()
    :return: a string of the complete graph directory path
    """
    check_dir = os.path.join(path_entry.get(),(name_entry.get().replace(" ", "_"))) #collapse name with no spaces
    return check_dir


