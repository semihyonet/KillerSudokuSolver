#The constraints are the specific values for areas ,writen on the sudoku sheet



class Constraint:   #The constraints are given on the text file
    def __init__(self,area,total):
        self.area = area
        self.total = total
    def get_area(self):  #This is a list of all the coordinates forming the constraints
        return self.area
    def get_total(self): #The total is what it equals to
        return self.area

    def __str__(self):   #The function for printing the values this is not necesary but it helps to determine if there
                            # are any errors on the text file
        areastr = ""
        for i in range(len(self.area)):
            if i == 0:
                areastr += str(self.area[i][0]) + "," + str(self.area[i][1])
            else:
                areastr += " - " + str(self.area[i][0]) + "," + str(self.area[i][1])


        return ("Areas are: "+ areastr + "\n\tTolal is: "+str(self.total))



"""
Constraint text file consists of
1 or 2 lines of coordinates-  2 lines if it goes on more than 1 dimension
if the line is starting with = its equal to the total of the constraint
"""

def get_constraints(filename):   #This gets the text from input file and converts it into an array of constraint classes,
                                 #This also could be made in a dictonary but folowing the oop makes things easier
    file = open(filename).read().split("\n")


    con_cordinates = []
    constraints = []
    used_cordinates = []

    for i in range(len(file)):


        if "#" in file[i]:
            file[i] = file[i].split("#")
            #Separating the coordinates
            if file[i][0] == file[i][1]: #only one coordinate
                file[i][0] = file[i][0].split(",")
                val1 = int(file[i][0][0])
                val2 = int(file[i][0][1])
                if [val1,val2] in used_cordinates:
                    print("\n\n\t\t\tUSED - ", [val1, val2])
                con_cordinates.append((val1,val2))
                used_cordinates.append((val1, val2))
            else:
                cor1 = file[i][0].split(",")
                cor2 = file[i][1].split(",")
                if cor1[0] == cor2[0]:
                    for i2 in range(int(cor1[1]),int(cor2[1])+1):
                        if [int(cor1[0]),i2] in used_cordinates:
                            print("\n\n\t\t\tUSED - ",[int(cor1[1]), i2])
                        con_cordinates.append((int(cor1[0]),i2))
                        used_cordinates.append((int(cor1[0]), i2))
                elif cor1[1] == cor2[1]:
                    for i3 in range(int(cor1[0]),int(cor2[0])+1):
                        if [i3,int(cor1[1])] in used_cordinates:
                            print("\n\n\t\t\tUSED - ",[i3,int(cor1[1])])
                        con_cordinates.append((i3,int(cor1[1])))
                        used_cordinates.append((i3, int(cor1[1])))



        if "=" in file[i]:

            file[i] =file[i].strip("=")
            constraints.append(Constraint(con_cordinates,int(file[i])))
            con_cordinates = []
    return constraints