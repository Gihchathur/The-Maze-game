import time
import csv
import os

filename = input("Enter File Name: ")
                 
#initialize a matrix
maze =[]
#get reading from csv file
with open(filename + '.csv')as myFile:
    reader=csv.reader(myFile)
    for row in reader:
        maze.append(row)

#number of rows in the maze
SIZE = len(maze)
#number of columns in the maze
SIZE1 = len(maze[0])

#solution is stored in the matrix
solution = [[0]*SIZE1 for _ in range(SIZE)]

#support matrix for the path finding
mat= [[0]*SIZE1 for _ in range(SIZE)]

#start position
startx=0
starty=0

#end position
destx=0
desty=0

def algorithm(row, column):
    #maze is solved if the current position of Robot is the destination
    if (row==destx) and (column==desty):
        solution[row][column] = 1;
        return True;
    
    #checking whether unvisited cells are safe to visit
    if row>=0 and column>=0 and row<SIZE and column<SIZE1 and (solution[row][column] == 0 and maze[row][column] == 0 or maze[row][column]=='S'):
        #if the next cell is not a brick robot visits it
        mat[row][column] = "R"
        
        for i in mat:
            print (*i)
            
        #delay for 1 second
        time.sleep(1)
        #print the path of the current robot
        print("\n")
        print("Robot is travelling\n")
        
        mat[row][column]='.'
        solution[row][column] = 1
        
        #first the robot will try to go down
        if algorithm(row+1, column):
            return True
        #going right
        if algorithm(row, column+1):
            
            return True
        #going up
        if algorithm(row-1, column):
            
            return True
        #going left
        if algorithm(row, column-1):
            
            return True
        #backtracking
        solution[row][column] = 0;
        mat[row][column] = "R"
        for i in mat:
            print (*i)
        time.sleep(1)
        mat[row][column]="."
        print("Robot is travelling\n")
        return False;
    return 0;


for i in range (0,SIZE):
    for j in range (0,SIZE1):
        if(maze[i][j]=='S'):      #get the source
            startx=i
            starty=j
        elif(maze[i][j]=='D'):    #get the destination
            destx=i
            desty=j
        elif(maze[i][j]=='0'):
            maze[i][j]=1
        elif(maze[i][j]=='1'):
            maze[i][j]=0
        


if(algorithm(startx,starty)):
    for i in range (0,SIZE):
      for j in range (0,SIZE1):
         if(solution[i][j]==1):
            solution[i][j]='+'

    for i in solution:    #print final path
        print (*i)
else:
    print ("No solution")
