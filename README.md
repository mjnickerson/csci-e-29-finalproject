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

-----
**FAQ** -

-----

[Micah Nickerson](min021@g.harvard.edu) - [Harvard University Extension](https://www.extension.harvard.edu/academics/graduate-degrees/data-science-degree) - Fall 2019