board=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,9],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#used to print the board in a more user friendly method
def print_board(bo):
    for i in range(len(bo)):
        #prints a separating line after every 3 rows
        if i%3==0 and i!=0:
            print("- - - - - - - - - - -")

        for j in range(len(bo)):
            #prints a separating line after every 3 columns
            if j%3==0 and j!=0:
                print("| ",end="")

            #if the iteration reaches the last element in a row,it prints the next values on a new line 
            if j==8:
                print(bo[i][j])

            #if the iteration is any other element in the row, it prints the next value right after it
            else:
                print(str(bo[i][j])+" ",end="")

def empty_index(bo):
    #checks if index has value 0 stored in it
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j]==0:
                return (i,j)
            
#ind refers to the index of the empty space. it is stored in a tuple
#num refers to numbers ranging from 1 to 9 which will be put into the empty indexs
def valid_checker(bo, num, ind):
    #this function assumes the sudoku board can be any size besides the regular 9x9

    #checking the rows
    for i in range(len(bo[0])):
        if bo[ind[0]][i]==num:
            return False
    
    #checking the columns
    for i in range(len(bo[0])):
        if bo[i][ind[0]]==num:
            return False
        
    #checking the individual boxes
    #the values that will be stored in box_x and box_y are either 0,1,2
    box_x=ind[0]//3
    box_y=ind[1]//3

    for i in range(box_x)




