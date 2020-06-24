# Killer Sudoku Solver

This is a Sudoku Solving Python application. This application solves basic Sudoku's but it was built to solve Killer Sudoku's, which is a harder version with more rules and constraints when compared with sudoku which is already a very difficult game.

# How to Run
This application needs to be initiated from the main.py file. Before running this file, change the file.txt with the sudoku you want to solve. Since this app is meant for Killer Sudoku type of Sudoku you also need to configure the constraints you want to put within the application.

"Constraints.txt" has a specific format for it to work. It's a very easy to use format thus wont create any problems. You need to define the areas as lines. For example to create a "L" shaped constraint you need to say the following: 
- 1,1#1,3
- 2,3#2,3
- =20
This will make a L shape with the following 2 dimensional Cordinates: 1,1  1,2  1,3  2,3 . The Lines should be 1 dimensional and only one dimension should change from the initial coordinate. This coordinate specifiers can be only 1 line or 2 lines then the total points needed for the application should come, just like #20 shown in the previous example. This means that the numbers assigned to the coordinates 1,1 1,2 1,3 2,3 should have a total of 20 points when combined. 

If you want to change the size you should change it from MACROS.py with the SIZE variable. It is configured to be a 9x9 matrix but can be changed to any size. But I suggest that you dont change it to any number that doesnt have a root value. It may produce unwanted errors and it is unpredictable. 

# How does the Algorithm Work

Backtracking algorithm works recursively. Its first action is initializing the value algorithm searches. It is the open spots on the sudoku.It initializes an array holding the coordinates of the values which are equal to 0 and the algorithm will select the first element from these coordinates to assign a value
The algorithm ends in 2 conditions ;
1. There are no open spots in the algorithm
2. The value cant be reached and all possible values reachable from the coordinates the
algorithm got stuck has been tried and it couldn’t find a solution in that scenario.
After that it goes into a for loop which will try all the values the selected coordinate can have , in each iteration of the loop it calls the all_okay() function from the level class. This function has an important role in this algorithm since it checks if the value on the specified coordinates is valid regarding
A. The coordinate hasn’t been given any value and is equal to 0(This is important since there are values pre determined in the sudoku grid)
B. Each number from 1-9 is only used once in its column
C. Each number from 1-9 is only used once in its row
D. Each number from 1-9 is only used once in its 3x3 section
E. All coordinates add up to a specific value that the Sudoku has given. I called this
specific values Constraints in the code I wrote.
If all the values return True then the algorithm initialize the value to the coordinates and calls itself recursively. It passes down the modified matrix as an argument since it will try to go and determine the next open value.
If it fails and returns False as the value it backtracks once and try’s all the values left in the for loop it was iterating. If it fails to find it, it goes back one more and more and more... Backtracking might be on the last point and it might delete all the values it found and come back to the first coordinate since its only logic is determining if the point in the specified coordinates is valid or not.


# Conclusion 
When the app concludes it will present the result matrix as well as how long it took to produce this result. Since the app is using the backtracking algorithm it may take a while to conclude.
