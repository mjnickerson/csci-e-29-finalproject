# LuiGUI Project (alpha)

###Building Luigi Pipelines using a Graphic User Interface and Metaprogramming
*Generating Directed Acyclic Graphs using tkinter and CookieCutter*

------

**Final Project for CSCI-E-29 - Advanced Python for Data Science**

**Project Presentation:**
https://drive.google.com/file/d/1HgUKMXPtUP3CI8sYotqr5AYzqXTCdgud/view
 
------
**Build Badges**
 
Test | Badge 
--- | --- 
*Travis CI* | [![Build Status](https://travis-ci.com/mjnickerson/csci-e-29-finalproject.svg?token=Sg4NLLafiHfmBCvPrLC5&branch=master)](https://travis-ci.com/mjnickerson/csci-e-29-finalproject)

-----

**Background** -  Directed acyclic graphs (DAG) are best introduced and expressed graphically, yet the construction of a DAG with Luigi is an entirely text (code) based process. Constructing large graphs would be simplified if they could be visualized (how parameters are assigned, and args are passed downstream) and then templated using user inputs. Luigi is ripe for a robust templating system that allows faster declaration of the targets and connecting them via nodes. Luigi has a visualizer, but it only allows the user to see the graph after it is built and running, which limits effective experimentation and error checking. An ideal solution is a Graphic User Interface – a simple drag and drop “node graph” approach or prefabricated fill in visualizers can be useful tools. Cookie cutter is explored to automatically generate a luigi graph using GUI inputs.

  

**Implementation** - this project explores designing a drag and drop GUI for luigi, and implements a prefabricated graphic interface for a graph that simplifies declaring a cookie cutter template for a Luigi pipeline. Cookie cutter is limited by it’s linear declarative structure, as it makes errors in entry easy and limits how many permutations are possible (prohibiting all but simple graph design). A python tkinter interface is generated for a graph that manages the graph configuration (options), build and execution.

 

**Conclusion** - Through exploration, we find that graphic visualizations as part of pipeline graph assembly and design are practical and beneficial, especially for data science team members with weaker coding skills. We find a graphic interfaces paired with cookiecutter or jinja are a doorway to improving cookiecutter’s usefulness. While they remain primarily text based, graph creation that involves some visual diagram component can template the skeleton of a DAG rapidly, and reduce the amount of manual input to deploy a workflow pipeline.

-----

**Running** -

1) Clone this repository.

2) This project uses pipenv as a virtual environment.
To deploy the venv shell: `$ pipenv install`
If there are technical issues locking the file, try `$ pipenv install --ignore-pipfile`

3) To run **Lui_GUI**: `$ pipenv run python lui_gui/lui_gui.py`

4) Lui_GUI will use this directory as the root by default;
New Luigi graphs will be output to this directory by default, in the folder `/graphs`
You can change this by entering or selecting a different graph path in the interface.

5) 

6) 

7) Load a demo example by selecting 

8)


**Cookie Cutter Repo:**
This project has a public sister repo that holds the cookiecutter code to generate luigi DAG's - it can be accessed here: https://github.com/mjnickerson/cookiecutter-luiGUI


*Optionally*, if desired it can also be called via cookiecutter on any CLI by `cookiecutter https://github.com/mjnickerson/cookiecutter-luiGUI`


-----
**FAQ** -


-----

[Micah Nickerson](mailto:min021@g.harvard.edu) - [Harvard University Extension](https://www.extension.harvard.edu/academics/graduate-degrees/data-science-degree) - Fall 2019