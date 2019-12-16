# LuiGUI Project (alpha)

### Building Luigi Pipelines using a Graphic User Interface and Metaprogramming

*Generating Directed Acyclic Graphs using tkinter and CookieCutter*

------

**Final Project for CSCI-E-29 - Advanced Python for Data Science**

**Project Presentation / Concept Deck:**
https://drive.google.com/file/d/1HgUKMXPtUP3CI8sYotqr5AYzqXTCdgud/view

*For information on planned later stages of this project, please see the GUI concept in the link above.*
 
------
**Build Badges**
 
Test | Badge 
--- | --- 
*Travis CI* | [![Build Status](https://travis-ci.com/mjnickerson/csci-e-29-finalproject.svg?token=Sg4NLLafiHfmBCvPrLC5&branch=master)](https://travis-ci.com/mjnickerson/csci-e-29-finalproject)

-----

Concept Wireframe:

![luiGUI Concept](https://raw.githubusercontent.com/mjnickerson/csci-e-29-finalproject/master/data/input/resources/luiGUI_concept.jpg)


Version 1.0.0:

![luiGUI Screenshot](https://raw.githubusercontent.com/mjnickerson/csci-e-29-finalproject/master/data/input/resources/luiGUI_screenshot.jpg)

-----

**Background** -  Directed acyclic graphs (DAG) are best introduced and expressed graphically, yet the construction of a DAG with Luigi is an entirely text (code) based process. Constructing large graphs would be simplified if they could be visualized (how parameters are assigned, and args are passed downstream) and then templated using user inputs. Luigi is ripe for a robust templating system that allows faster declaration of the targets and connecting them via nodes. Luigi has a visualizer, but it only allows the user to see the graph after it is built and running, which limits effective experimentation and error checking. An ideal solution is a Graphic User Interface – a simple drag and drop “node graph” approach or prefabricated fill in visualizers can be useful tools. Cookie cutter is explored to automatically generate a luigi graph using GUI inputs.

  

**Implementation** - this project explores designing a drag and drop GUI for luigi, and implements a prefabricated graphic interface for a graph that simplifies declaring a cookie cutter template for a Luigi pipeline. Cookie cutter is limited by it’s linear declarative structure, as it makes errors in entry easy and limits how many permutations are possible (prohibiting all but simple graph design). A python tkinter interface is generated for a graph that manages the graph configuration (options), build and execution.

 

**Conclusion** - Through exploration, we find that graphic visualizations as part of pipeline graph assembly and design are practical and beneficial, especially for data science team members with weaker coding skills. We find a graphic interfaces paired with cookiecutter or jinja are a doorway to improving cookiecutter’s usefulness. While they remain primarily text based, graph creation that involves some visual diagram component can template the skeleton of a DAG rapidly, and reduce the amount of manual input to deploy a workflow pipeline. We also find by controlling metaprogramming from a GUI, graphs can be as easily discarded as they can be created. Through this, **luigi graphs become a rapid extension to our existing daily data science workflows** - code that exists only for as long as it is are useful, and then disappears. 

-----

**Running luiGUI** -

1) Clone this repository.

2) This project uses **pipenv** as a virtual environment shell. To deploy the venv shell type: 
`$ pipenv install` in the command line within the cloned repository root directory.
    
    *Note:* If there are technical issues locking the file, try `$ pipenv install --ignore-pipfile`.
    If you don't have pipenv installed, try `pip install pipenv`.
    For anaconda/conda users, first try `conda install pipenv`. 

3) To run **Lui_GUI**: `$ pipenv run python lui_gui/lui_gui.py`

4) **Try a demo example** by selecting `> Default Example <` - this demo adds watermarks to existing images; 
    
    The graph will download a watermark image from a cloud server (s3), apply it to sample images (provided under `data/input/images`), and output those images.

5) Enter the name of the new graph in the top bar.

6) Verify/Enter the directory where you want graphs created in the top bar.
    
    By default, new Luigi graphs output to the folder `../graphs`
    You can change this by entering or selecting a different graph path in the interface.

7) Update entry fields for the node blocks, including scripts to run, input and output targets,
as well as optional input parameters.
   
    - If either Task or Local Target Output are left blank, they will output to `../data` by default.
    
    - ExternalProgramTask can be skipped! (along with its Local Target Output) - just leave their fields blank.

8) Select `> Generate Graph <` to assemble the luigi graph with entered parameters. You can see progress of assembly in the command line. Graphs must have unique names, duplicate graphs with same name cannot be built. 

9) Select `> Run Graph <`, to build and execute the generated luigi graph. You can see progress of run in the command line. For the demo example, the output will be in the `data\output` folder. 

10) When done with the graph make sure to `> Delete Graph <` to trash it - no need to keep old graphs lying around!

11) Scripts **must** be located in the folder named `scripts` to be run;
*Future functionality will allow for adaptive naming pathways.*


-----

**Cookie Cutter Repo:**
This project has a public sister repo that holds the cookiecutter code to generate luigi DAG's - 
it can be accessed here: **https://github.com/mjnickerson/cookiecutter-luiGUI**


*Optionally*, if desired it can also be called via cookiecutter on any CLI by
`$ cookiecutter https://github.com/mjnickerson/cookiecutter-luiGUI`

-----
**Install Requirements:**
- Python 3.7 (conda preferred)
- Git
- pipenv

**Virtual Environment Requirements:**
- dev-packages:
    - pytest
    - pytest-cov
- packages:
    - luigi
    - cookiecutter
    - awscli
    - boto3
    - cython
    - atomicwrites
    - pillow
-----
**References:**

*Block Logic*
![Concept Nodeblocks](https://raw.githubusercontent.com/mjnickerson/csci-e-29-finalproject/master/data/input/resources/luiGUI_block_logic.jpg)

-----

[Micah Nickerson](mailto:min021@g.harvard.edu) - [Harvard University Extension](https://www.extension.harvard.edu/academics/graduate-degrees/data-science-degree) - Fall 2019