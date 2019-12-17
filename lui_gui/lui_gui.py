import os
import shutil
import pathlib
from datetime import date
from cookiecutter.main import cookiecutter
from tkinter import *
from tkinter import dnd, messagebox, simpledialog, filedialog, colorchooser
from gui.guiparts import blank_node_box, blank_ground, credits_window, warning_graph_exists, warning_no_folder, warning_no_graph, warning_task_missing, warning_node_name_missing, warning_output_target_missing
from gui.guicommands import update_field, graph_path
from src.tools import get_file_path


######################

#local GUI Functions

def close_gui(): #exit function
    lui_gui_window.destroy()
    exit()

def new_winF(): # new window definition
    credits_window(lui_gui_window)

def example_gui():
    """
    For TA Review purposes, fills values into a demonstration format
    :return: updates all the fields to defaults for easy running
    """
    update_field(graph_name_entry, 'Watermark Example')
    update_field(graph_root_entry, os.path.join(os.getcwd(),'graphs'))
    update_field(node1_name, 'Cloud Data')
    update_field(node_1_aws_access_id, '')
    update_field(node_1_aws_secret_key, '')
    update_field(node1_target_entry, 's3://lui-gui-demo-data/images/luigi_trans.png')
    update_field(node2_name, 'S3 Download')
    update_field(node3_name, 'Watermark Atomic Download')
    update_field(node3_input_params, ' >')
    update_field(node3_run_target, os.path.join(os.getcwd(),'scripts','s3_atomic_download.py'))
    update_field(node3_output_folder, os.path.join(os.getcwd(),'data','input','watermark'))
    update_field(node4_name, 'Add Watermark Top Left')
    update_field(node4_input_params, os.path.join(os.getcwd(),'data','input','images','hackathon.jpg'))
    update_field(node4_run_target, 'scripts/watermark.py')
    update_field(node5_name, 'Save Local')
    update_field(node5_target_output, os.path.join(os.getcwd(),'data','output'))

def no_fields_empty():
    """
    Verifies if fields entered are empty, and a create/delete can proceed
    :return: True if they are not empty, False if either are empty
    """
    if not graph_root_entry.get(): #if this field is blank
        messagebox.showinfo("Warning!", "Warning! Graph path is incomplete!")
        return False #cannot proceed
    elif not graph_name_entry.get(): #if this field is blank
        messagebox.showinfo("Warning!", "Warning! Graph name is incomplete!")
        return False #cannot proceed
    else:
        return True

def try_delete():
    """
    Point of no return - checks with user if they want to delete this path
    :return: delete_graph() , deletes ALL folders and files within, and downstream, of that path
    """
    if no_fields_empty():
        confirm_delete = messagebox.askyesno("Warning!","Are you sure you want to delete this Graph?")
        if confirm_delete:
            delete_graph()

def set_root():
    graph_directory = filedialog.askdirectory(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select the graph root directory folder:")
    print(graph_directory) #diagnostics
    update_field(graph_root_entry, graph_directory)

def set_temp_directory():
    temp_directory = filedialog.askdirectory(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select a folder to download to:")
    print(temp_directory) #diagnostics
    update_field(node3_output_folder, temp_directory)

def set_output_directory():
    out_directory = filedialog.askdirectory(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select a folder to output to:")
    print(out_directory) #diagnostics
    update_field(node5_target_output, out_directory)

def set_node_3_run_target():
    set_3_script = filedialog.askopenfilename(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select script to run:",
                                 filetypes=allowed_filetypes)
    print(set_3_script) #diagnostics
    update_field(node3_run_target, set_3_script)

def set_node3_input_params():
    set_3_params = filedialog.askopenfilename(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select input parameters or folder:",
                                 filetypes=allowed_filetypes)
    print(set_3_params) #diagnostics
    update_field(node3_input_params, set_3_params)

def set_node_4_run_target():
    set_4_script = filedialog.askopenfilename(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select script to run:",
                                 filetypes=allowed_filetypes)
    print(set_4_script) #diagnostics
    update_field(node4_run_target, set_4_script)

def set_node_4_input_params():
    set_4_params = filedialog.askopenfilename(parent=lui_gui_window,
                                 initialdir=os.getcwd(),
                                 title="Select input parameters or folder:",
                                 filetypes=allowed_filetypes)
    print(set_4_params) #diagnostics
    update_field(node4_input_params, set_4_params)

######################
# PLACEHOLDER FOR THREE KEY FUNCTIONS:

def generate_graph():
    """
    This function:
    1) Collect GUI inputs, format them into strings
    2) Run logic checks to verify user inputs are stable / make stable graph
    3) Assembles cc_kwargs from collected GUI inputs
    :return cc_kwargs: key word arguments dictionary of cookie_cutter json fields
    :return: call_cookiecutter()
    """
    verbose = False #diagnostics flag, for checking kwargs

    #set environmental variables
    if node_1_aws_access_id.get():
        os.environ['node_1_aws_access_id'] = node_1_aws_access_id.get()
    if node_1_aws_secret_key.get():
        os.environ['node_1_aws_secret_key'] = node_1_aws_secret_key.get()

    #GET GENERATOR PARAMETERS
    graph_root_gen = graph_root_entry.get()
    graph_name_gen = graph_name_entry.get().lower().replace(" ", "_")
    node1_name_gen = node1_name.get().replace(" ", "_")
    node1_target_gen = node1_target_entry.get()
    node1_target_filename = os.path.basename(node1_target_gen) #get target file name
    node2_name_gen = node2_name.get().replace(" ", "_")
    node3_name_gen = node3_name.get().replace(" ", "_")
    node3_run_gen = get_file_path(os.path.basename(node3_run_target.get().replace(" ", "_")), True) #get just module name (ditch path and extensions)
    node3_output_folder_gen = node3_output_folder.get()
    node4_name_gen = node4_name.get().replace(" ", "_")
    node4_input_params_gen = node4_input_params.get()
    node4_run_gen = node4_run_target.get()
    node5_name_gen = node5_name.get().replace(" ", "_")
    node5_target_output_gen = node5_target_output.get()

    #CHECK FOR LOGIC FAILURES THAT WILL BREAK THE GRAPH
    if not node3_run_gen: #if Task script is blank
        warning_task_missing() #show warning
        return #break generate
    if not node1_name_gen: #if node name is blank
        warning_node_name_missing() #complain
        return #break
    if not node2_name_gen:
        warning_node_name_missing()
        return
    if not node3_name_gen:
        warning_node_name_missing()
        return
    if not node4_name_gen: #if node 4 name is blank
        if (node4_input_params_gen + node4_run_gen): #but the other fields have text, assume that node 4 should run
            warning_node_name_missing() #complain about it
            return #break generate

    # INTERPRETATION OF USER ENTRY PRIOR TO GENERATON - CONFIGURATION OF MISSING VALUES
    #missing required targets
    if not node3_output_folder_gen: #if no node_3 target is given
        node3_output_folder_gen = (os.path.join(os.getcwd(),"data"))
    if not node5_target_output_gen: #if no node_3 target is given
        node5_target_output_gen = (os.path.join(os.getcwd(),"data"))

    # if nodes 4 are blank - assume user wants to skip ExternalProgramTask its LocalTarget
    check_nodes_4_5 = node4_name_gen + node4_input_params_gen + node4_run_gen #concatenated string
    if not check_nodes_4_5: #if all node 4 fields are blank
        active_nodes = "123" #dont include 4,5
    else:
        active_nodes = "12345" #else include all

    #diagnostics print
    if verbose:
        print(graph_name_gen)
        print(graph_root_gen)
        print(active_nodes)
        print(node1_name_gen)
        print(node1_target_gen)
        print(node1_target_filename)
        print(node2_name_gen)
        print(node3_name_gen)
        print(node3_run_gen)
        print(node3_output_folder_gen)
        print(node4_name_gen)
        print(node4_input_params_gen)
        print(node4_run_gen)
        print(node5_name_gen)
        print(node5_target_output_gen)

    # ENTER GENERATOR PHASE - PREP KWARGS FOR COOKIECUTTER
    # kwargs dictionary for cookiecutter to override default parameters
    cc_kwargs = {"graph_name": graph_name_gen,
        "graph_folder": graph_name_gen,
        "dag_name": graph_name_gen + "_graph",
        "dag_short_description": "AutoGenerated Graph " + graph_name_gen + " from luiGUI",
        "active_nodes": active_nodes,
        "node_1": node1_name_gen,
        "node_2": node2_name_gen,
        "node_3": node3_name_gen,
        "node_4": node4_name_gen,
        "node_5": node5_name_gen,
        "node3_run_target": node3_run_gen,
        "node4_run_target": node4_run_gen,
        "node1_target_entry": node1_target_gen,
        "node1_target_filename": node1_target_filename,
        "node3_output_folder": node3_output_folder_gen,
        "node4_input_params": node4_input_params_gen,
        "node5_target_output": node5_target_output_gen,
        "release_date": date.today().strftime("%d/%m/%Y"),
        "version": "1.0.0",
        "node_1_aws_access_id": os.environ.get('node_1_aws_access_id'),
        "node_1_aws_secret_key": os.environ.get('node_1_aws_secret_key')}

    #verify graph does not exist
    check_dir = graph_path(graph_root_entry, graph_name_entry)
    if no_fields_empty(): #if the path is complete
        if os.path.exists(check_dir): #dir exists
            if not os.listdir(check_dir):  #dir is empty
                call_cookiecutter(check_dir, graph_root_gen, cc_kwargs, True) #includes flag that empty directory exists
            else: #if the directory is not empyy
                warning_graph_exists()
        else: #directory does not exist
            call_cookiecutter(check_dir, graph_root_gen, cc_kwargs, False) #includes flag that directory does not exist

def call_cookiecutter(full_path, root_path, cc_kwargs_dict, dir_exists=False):
    """
    Calls cookiecutter build from a dictionary of user inputs
    :param full_path: full install path, for diagnostics
    :param root_path: root path for cookiecutter, to install into
    :param cc_kwargs_dict: dictionary of user inputs from GUI
    :param dir_exists: boolean flag if the dictionary exists (to install within an existing dictionary)
    :return: calls cookiecutter function
    """
    if dir_exists: # if empty directory exists
        root_path = full_path #install inside the existing folder
    print("\nGENERATING Luigi graph...")
    print("\nInstalling into: ", full_path)
    # call cookiecutter
    cookiecutter('https://github.com/mjnickerson/cookiecutter-luiGUI', no_input=True, extra_context=cc_kwargs_dict, output_dir=root_path)
    # end
    print("\nDone!")

def run_graph():
    check_dir = graph_path(graph_root_entry, graph_name_entry)
    if no_fields_empty(): #if the path is complete
        if os.path.exists(check_dir): #and dir exists
            print("\nBUILDING Luigi graph...")
            # check execution process
            print("\nRUNNING Luigi graph...\n")
            run_command = ('pipenv run python "' + os.path.join(check_dir,graph_name_entry.get().lower().replace(" ", "_") + '_graph"'))
            print(run_command)
            os.system(run_command) # run graph on the command line
        else:
            warning_no_graph() #warn the user it can't run, no graph

def delete_graph():
    check_dir = graph_path(graph_root_entry, graph_name_entry)
    if os.path.exists(check_dir): #if user says yes
        print("\nBye Bye Graph - deleting graph %s" % check_dir)
        #######################
        #### DANGER ZONE: #####
        # Here lies the ability to delete important stuff without mercy!
            # The user must not be able to specify folders outside of their root!
        shutil.rmtree(check_dir)  # delete the graph files
        #######################
       #######################
    else:
        warning_no_folder()

############################################

#properties
graph_name = "New_Graph" #default
graph_directory = os.path.join(os.getcwd(),"graphs") #default

#viz settings
node_width = 15 #column width
node_start = 3 #row
node_end = 13 #row
nm_cols = [1,3,5,9,11]
lng_cols = 7
lng_width = 20
but_width = 19
buffer_width = 4
start_gnd =  12 #row to start ground
end_gnd = 14 #row to start ground


#SET color schema
"""
This allows for different possible color configurations
"""
color_schema = 2

#color schema configurations
if color_schema == 2: #supermario theme
    background_color = "#5b99fe"
    field_color = "white"
    header_color = "#89e100"
    ground_color = "#d74701"
    arrow_color = "#ff9d3a"
    arrow_text_color = "#de4c01"
    but_color = "#f8be03"
    but_text_color = "black"
    exit_but_color = "#ffffff"
    exit_but_text_color = "#5b99fe"
## ADD YOUR OWN COLOR SCHEMA HERE ###
else: #default theme
    background_color = "grey"
    field_color = "white"
    header_color = "lightgrey"
    ground_color = "grey"
    arrow_color = "lightgrey"
    arrow_text_color = "black"
    but_color = "lightgrey"
    but_text_color = "black"
    exit_but_color = "lightgrey"
    exit_but_text_color = "black"

#filetypes
allowed_filetypes = [('python files', '.py'),('all files', '.*')]

############################################

#declare gui_window
lui_gui_window = Tk()
lui_gui_window.title("LuiGUI - a luigi powerup") #bar name
lui_gui_window.iconbitmap(r'data/input/resources/luiGUI.ico') #bar icon
lui_gui_window.configure(background=background_color) #main background color
lui_gui_window.geometry("1620x410")

############################################

#header
Label(lui_gui_window, text="LuiGUI", fg="black", bg=header_color, font="Verdana 14 bold", width=node_width).grid(row=0, column=1, sticky=W)

#blank header
for column_blank in range(0,12,2): # blank header
    Label(lui_gui_window, text="", fg="black", bg=header_color, width=buffer_width, font="Verdana 14 bold").grid(row=0, column=column_blank, sticky=W)
for column_blank in nm_cols: # blank header
    Label(lui_gui_window, text="", fg="black", bg=header_color, width=node_width, font="Verdana 14 bold").grid(row=0, column=column_blank, sticky=W)
Label(lui_gui_window, text="", fg="black", bg=header_color, width=lng_width, font="Verdana 14 bold").grid(row=0, column=lng_cols, sticky=W)

# file load label
Label(lui_gui_window, text="        Graph Name:", fg="black", bg=header_color, width=node_width, font="Verdana 14 bold").grid(row=0, column=3, sticky=E)
graph_name_entry = Entry(lui_gui_window, width=14, bg=header_color, font="Verdana 14 bold")
graph_name_entry.grid(row=0, column=5)
graph_name_entry.insert(END, graph_name)

#root directory label
Label(lui_gui_window, text="  Graph Location:", fg="black", bg=header_color, width=node_width, font="Verdana 14 bold").grid(row=0, column=7, sticky=E)
graph_root_entry = Entry(lui_gui_window, width=14, bg=header_color, font="Verdana 14 bold")
graph_root_entry.grid(row=0, column=9)
graph_root_entry.insert(END, graph_directory)
root_but = Button(lui_gui_window, text="Open", fg="black", bg=header_color, font="Verdana 10", command=set_root)
root_but.grid(row=0, column=10, sticky=W)

#arrows
for column_blank in range(2,10,2): # blank header
    Label(lui_gui_window, text=" > ", fg=arrow_text_color, bg=arrow_color, font="Verdana 20 bold").grid(row=8, column=column_blank, sticky=W)

#blank ground at bottom
blank_ground(lui_gui_window, ground_color, start_gnd, end_gnd, buffer_width, nm_cols, node_width, lng_cols, lng_width, but_width)

############################################

#node 1
node_column = 1
node_color = "lavender"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="S3Target", fg="black", bg=node_color, font="Verdana 14 bold", width=node_width).grid(row=3, column=node_column, sticky=W)
node1_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node1_name.grid(row=4, column=node_column)
node1_name.insert(END, ' Node 1 Name')
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

############################################

#node 2
node_column = 3
node_color = "lightblue"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="External Task", fg="black", bg=node_color, width=node_width, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node2_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node2_name.grid(row=4, column=node_column)
node2_name.insert(END, ' Node 2 Name')
Label(lui_gui_window, text="Parameters:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W) #NOT IMPLEMENTED IN THIS VERSION
node2_params_entry = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold") #NOT IMPLEMENTED IN THIS VERSION
node2_params_entry.grid(row=6, column=node_column) #NOT IMPLEMENTED IN THIS VERSION
node2_params_entry.insert(END, '')
Label(lui_gui_window, text="Output:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)
Label(lui_gui_window, text="                -->", fg="black", bg=node_color, font="Verdana 12 bold", width=node_width).grid(row=12, column=node_column, sticky=W)
############################################

#node 3
node_column = 5
node_color = "blue"
fg_color= "white"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank

Label(lui_gui_window, text="Task", fg=fg_color, bg=node_color, width=node_width, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node3_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, fg=fg_color, font="Verdana 12")
node3_name.grid(row=4, column=node_column)
node3_name.insert(END, ' Node 3 Name')

Label(lui_gui_window, text="Parameters:", fg=fg_color, bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
node3_input_params= Entry(lui_gui_window, width=round(node_width*1.5), fg=fg_color, bg=node_color, font="Verdana 8 bold")
node3_input_params.insert(END, ' > ')
node3_input_params.grid(row=6, column=node_column)
node3_input_params_but = Button(lui_gui_window, text="^", fg=fg_color, bg=node_color, font="Verdana 8 bold", command=set_node3_input_params)
node3_input_params_but.grid(row=6, column=node_column, sticky=E)

Label(lui_gui_window, text="Run:", fg=fg_color, bg=node_color, font="Verdana 12", width=node_width).grid(row=7, column=node_column, sticky=W)
node3_run_target = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, fg="white", font="Verdana 8 bold")
node3_run_target.insert(END, ' > ')
node3_run_target.grid(row=8, column=node_column)
node_3_run_but = Button(lui_gui_window, text="^", fg=fg_color, bg=node_color, font="Verdana 8 bold", command=set_node_3_run_target)
node_3_run_but.grid(row=8, column=node_column, sticky=E)

Label(lui_gui_window, text="Output Folder:", fg=fg_color, bg=node_color, font="Verdana 12", width=node_width).grid(row=11, column=node_column, sticky=W)
node3_output_folder = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, fg="white", font="Verdana 8 bold")
node3_output_folder.insert(END, ' ../')
node3_output_folder.grid(row=12, column=node_column)
node_3_output_but = Button(lui_gui_window, text="^", fg=fg_color, bg=node_color, font="Verdana 8 bold", command=set_temp_directory)
node_3_output_but.grid(row=12, column=node_column, sticky=E)

############################################

#node 4
node_column = 7
node_4_width = lng_width
node_color = "lightblue"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_4_width, node_column) #blank
Label(lui_gui_window, text="External Program Task", width=node_4_width, fg="black", bg=node_color, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node4_name = Entry(lui_gui_window, width=round(node_4_width), bg=node_color, font="Verdana 12")
node4_name.grid(row=4, column=node_column)
node4_name.insert(END, ' Node 4 Name')
Label(lui_gui_window, text="Parameters / Inputs:", fg="black", bg=node_color, font="Verdana 12", width=node_4_width).grid(row=5, column=node_column, sticky=W)
node4_input_params= Entry(lui_gui_window, width=round(node_4_width*1.5), bg=node_color, font="Verdana 8 bold")
node4_input_params.insert(END, ' > ')
node4_input_params.grid(row=6, column=node_column)
node4_input_params_but = Button(lui_gui_window, text="^", fg="black", bg=node_color, font="Verdana 8 bold", command=set_node_4_input_params)
node4_input_params_but.grid(row=6, column=node_column, sticky=E)
Label(lui_gui_window, text="CLI Script / Arguments:", fg="black", bg=node_color, font="Verdana 12", width=node_4_width).grid(row=7, column=node_column, sticky=W)
node4_run_target= Entry(lui_gui_window, width=round(node_4_width*1.5), bg=node_color, font="Verdana 8 bold")
node4_run_target.insert(END, ' > ')
node4_run_target.grid(row=8, column=node_column)
node4_target_output_but = Button(lui_gui_window, text="^", fg="black", bg=node_color, font="Verdana 8 bold", command=set_node_4_run_target)
node4_target_output_but.grid(row=8, column=node_column, sticky=E)
Label(lui_gui_window, text="Output:", fg="black", bg=node_color, font="Verdana 12", width=node_4_width).grid(row=11, column=node_column, sticky=W)
Label(lui_gui_window, text="                -->", fg="black", bg=node_color, font="Verdana 12 bold", width=node_4_width).grid(row=12, column=node_column, sticky=W)
############################################

#node 5
node_column = 9
node_color = "lavender"
blank_node_box(lui_gui_window, node_start, node_end, node_color, node_width, node_column) #blank
Label(lui_gui_window, text="Local Target", width=node_width, fg="black", bg=node_color, font="Verdana 14 bold").grid(row=3, column=node_column, sticky=W)
node5_name = Entry(lui_gui_window, width=round(node_width), bg=node_color, font="Verdana 12")
node5_name.grid(row=4, column=node_column)
node5_name.insert(END, ' Node 5 Name')
Label(lui_gui_window, text="Parameters:", fg="black", bg=node_color, font="Verdana 12", width=node_width).grid(row=5, column=node_column, sticky=W)
node5_params_entry = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold") #NOT IMPLEMENTED IN THIS VERSION
node5_params_entry.grid(row=6, column=node_column) #NOT IMPLEMENTED IN THIS VERSION
node5_params_entry.insert(END, '') #NOT IMPLEMENTED IN THIS VERSION
Label(lui_gui_window, text="Output:", fg="black", bg=node_color, font="Verdana 12 bold", width=node_width).grid(row=7, column=node_column, sticky=W)
node5_target_output = Entry(lui_gui_window, width=round(node_width*1.5), bg=node_color, font="Verdana 8 bold")
node5_target_output.insert(END, '  ../ ')
node5_target_output.grid(row=8, column=node_column)
node_5_output_but = Button(lui_gui_window, text="^", fg="black", bg=node_color, font="Verdana 8 bold", command=set_output_directory)
node_5_output_but.grid(row=8, column=node_column, sticky=E)

############################################

test_but = Button(lui_gui_window, text="LuiGUI", fg="black", bg=header_color, font="Verdana 14 bold", height=1, borderwidth=0, width=node_width, command=new_winF)
test_but.grid(row=0, column=1, sticky=W)

but_exit = Button(lui_gui_window, text="> Exit < ", font="Verdana 10 bold", fg=exit_but_text_color, bg=exit_but_color, width=but_width, command=close_gui)
but_exit.grid(row=2, column=11, sticky=W)

but_del = Button(lui_gui_window, text="> Delete Graph <", fg="red", bg=but_color, font="Verdana 10 bold", width=but_width, command=try_delete)
but_del.grid(row=4, column=11, sticky=W)

but_example = Button(lui_gui_window, text="> Default Example <", fg=but_text_color, bg=but_color, font="Verdana 10", width=21, command=example_gui)
but_example.grid(row=6, column=11, sticky=W)

but_generate = Button(lui_gui_window, text="> Generate Graph! <", fg=but_text_color, bg=but_color, font="Verdana 10 bold", width=but_width, command=generate_graph)
but_generate.grid(row=9, column=11, sticky=W)

but_run = Button(lui_gui_window, text="> Run Graph! <", fg=but_text_color, font="Verdana 10 bold", bg=but_color, width=but_width, command=run_graph)
but_run.grid(row=11, column=11, sticky=W)

############################################

#run interface
mainloop()