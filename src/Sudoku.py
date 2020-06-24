import Level
import MACROS

def find_value(lvl:list): # Backtracking algorithm
    playground = Level.level(lvl)#this is the main class that we will work on since this is a recursive function it will
    #form different classes in each run
    open_arr = playground.get_open() #Gets all the available positions for processing

    if (len(open_arr) == 0): #If no other value is left
        print("\n \t\t\t\t\tNUMBER OF ASIGNMENTS PERFORMED IN TOTAL IS "+ str(MACROS.ASSIGNED_VALUE_NUM)) #This holds how many times the algorithm assigns a value
        return True
    target = open_arr[0]     #gets the first value on the arr in this way the algorithm will go from row to row
    target_x = target[0]+1   # since my format on the matrix doesnt start from 0 , 0 and starts from 1 ,1 it converts it by adding 1
    target_y = target[1]+1

    for val in range(1,10):  #This is a loop for deciding which value we will put into target spot it goes through
                             #1 to 10, and checks if its true

        if playground.allokay(target_x,target_y,val): #MOST IMPORTANT PART
            #This function returns true if the value can be placed at its position.
            #It checks for the row ,column the box and its constraint area, If they all are okay it returns True

            MACROS.ASSIGNED_VALUE_NUM += 1

            playground.set_val(target_x,target_y,val) #since the value is okay the place it puts the val into the arr

            if find_value(playground.get_level()):    #This is the part that makes this function recursive this will
                return True                           #if the functions open_arr is empty then it will return true
                                                      #Therefore all the functions before it will return true as well

            print(str(playground))                    #This is for tracking where the algorithm is

            playground.set_val(target_x,target_y,0)   #if the function came here without getting inside the if then its
                                                      #not the correct value because of the values before so it sets the
                                                      #value back to 0 and re evaluates
    return False #this means no points result True therefore it backtracks to the value before
