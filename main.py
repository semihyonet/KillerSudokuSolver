import Level #This has all the Logic and the array of the level
import Sudoku #This has the Algorithm
from MACROS import *  #Includes Macros such as input file location or the size of the sudoku
import time #Its to count the time it takes to find the solution



lvl = Level.levelmaker(INPUT_LEVEL_DIR) #This reaches out to the input file of the level and forms it into a matrix




lev = Level.level(lvl)  #Forms the level class which basically handles all the operations done on -
                        #the matrix of the level gathered from the matrix
a = time.perf_counter() #starts the countdown

Sudoku.find_value(lvl) #Finds the value

b = time.perf_counter() #Ends the timer

Level.level(lvl).output(OUTPUT_SOLUTION_DIR) #Puts the solution to the output file

print(Level.level(lvl)) #Prints the solution for view inside the editor
print("Time passed until a solution was found - ",(b-a)) #Time passed will be printed out