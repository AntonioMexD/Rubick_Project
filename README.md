# Rubick_Project
Mini Project Cubo Rubik

Technical Report - Rubik's Cube Solver
1. Author

Author: Antonio Medina Padilla
2. Project Description

This project is a Rubik's Cube solver implemented in Python. It utilizes a depth-first search approach to find a solution to the Rubik's Cube from any initial state.

3. Programming Environment Requirements

Python 3.x
Standard Python libraries

4. User Manual

4.1 Encoding Format to Load Cube State from Text File
The text file cube_state.txt should follow the following format:

makefile
up:
<color1> <color2> <color3>
<color4> <color5> <color6>
<color7> <color8> <color9>
front:
<color1> <color2> <color3>
<color4> <color5> <color6>
<color7> <color8> <color9>
left:
<color1> <color2> <color3>
<color4> <color5> <color6>
<color7> <color8> <color9>
right:
<color1> <color2> <color3>
<color4> <color5> <color6>
<color7> <color8> <color9>
down:
<color1> <color2> <color3>
<color4> <color5> <color6>
<color7> <color8> <color9>
back:
<color1> <color2> <color3>
<color4> <color5> <color6>
<color7> <color8> <color9>

Where color represents the color of each cell in a row of a face of the cube.

4.2 Instructions to Execute the Program
Download the source code from the repository.
Ensure you have Python 3.x installed on your system.
Open a terminal and navigate to the directory where the code is located.
Run the program using the following command:
python main2.py
Follow the instructions provided in the console.

5. Design and Implementation

5.1 Problem Model
The problem involves finding a sequence of moves that restores a Rubik's Cube to its original state, where each face of the cube has a single color.

5.2 Algorithm(s), Techniques, Selected Heuristics
A depth-first search (DFS) approach is used to explore the state space of the Rubik's Cube. A heuristic function is implemented to detect repeated states and avoid infinite loops.

5.3 Linguistic Models Used
No linguistic models were used in this project.

6. Future Work

6.1 Incomplete Tasks and/or Ideas for Project Continuation
Implement more advanced search algorithms, such as breadth-first search or A* search.
Improve the efficiency of the solver for larger cubes.
Develop a graphical user interface (GUI) for a better user experience.
