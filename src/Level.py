import Constraints
from MACROS import *

def levelmaker(text:str):                 #This function takes the text file directory it was given and puts it into a
                                          #NxN array
    level = open(text,"r").read()
    level = level.split("\n")             #Splits rows
    for y in range(len(level)):
        level[y] = level[y].split(" ")   #Splits Columns
        for x in range(len(level[y])):
            level[y][x] = int(level[y][x])
    return level


class level:
    def __init__(self ,lvltext:list):

        self.lvltext = lvltext             #gets the level text


    def __str__(self):                     #This is for printing the array easily
        text =""
        for y in self.lvltext:
            for val in y:
                text +=str(val) +"\t"
            text+="\n"
        return text

    def output(self,file_dir):             #only called when the solution is found it writes the sol into a .txt file
        output_file = open(file_dir,"w")
        output_file.write(str(self))
        output_file.close()

    def get_level(self):                  #gets the level for the recursive part of the function since it passes down arr
        return self.lvltext

    def get_val(self,x,y):                #Gets the value of the coordinates
        return self.lvltext[y-1][x-1]

    def is_open(self,x,y):                #if the val is = 0, it returns true
        if self.get_val(x,y) == 0:
            return True
        else:
            return False

    def get_open(self):                   #gets the all the coordinates which have the value of 0
        open_list = []
        for y in range(SIZE):
            for x in range(SIZE):
                if self.lvltext[y][x] == 0:
                    open_list.append((x,y))
        return open_list

    def row_available(self,x,val):        #checks for the row if the number was used or not before
        for y in range(1,10):
            var = self.lvltext[y-1][x-1]
            if var == val:
                return False
        return True

    def col_available(self,y,val):       #checks for the column if the number was used or not before
        for x in range(1,10):
            var = self.lvltext[y-1][x-1]
            if var == val:
                return False
        return True

    def sectiondetermine(self,x,y):     #this determines which 3x3 matrix the coordinates are on on and returns it into
                                        #the box_available function
        xsection = int((x-1)/3)+1
        ysection = int((y-1)/3)+1
        return [xsection,ysection]

    def box_available(self,x,y,val):    # checks if the value is previously used on its 3x3 matrix
        sect = self.sectiondetermine(x,y)
        for y in range(1,10):
            for x in range(1,10):
                if sect == self.sectiondetermine(x,y):
                    if self.get_val(x,y) == val:
                        return False
        return True

    def constraint_okay(self,x,y,val):  #the constraints are the coordinate specific values for the sudoku it gets the
                                                                    #value it spossed to be equal when all the values
                                                                    #on the coor are added
        arr =Constraints.get_constraints(INPUT_CONSTRAINTS_DIR)

        for con in arr:     # searchs for the x ,y cor to find the if the values are equal to the value or not

            if (x,y) in con.get_area():

                total =0
                for i in con.get_area(): #this gives all the values of the coordinates on the same constraint
                    total +=self.get_val(i[0],i[1])
                if (total+val) <= con.total:#NOTE: This function looks if the total value is passed
                    # not if its exactly = total so it returns true if its not more than the total
                    return True
        else:
            return False


    def set_val(self,x,y,val):
        self.lvltext[y-1][x-1] = val

    def allokay(self,x,y,val): #This is the most important function on this class. It checks the row ,column , 3x3 matrix and constraints if its all True it returns True
        return self.is_open(x,y) and self.row_available(x,val) and self.col_available(y,val) and  self.constraint_okay(x,y,val) and self.box_available(x,y,val)

