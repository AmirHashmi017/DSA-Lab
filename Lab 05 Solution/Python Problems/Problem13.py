def AddRow(grid,row):
    grid.append(row)
    print(f"After adding Row {row} the grid is: {grid}")
def AddColumn(grid,column):
    if(len(grid)==len(column)):
        for i in range(len(grid)):
            grid[i].append(column[i])
        print(f"After adding Column {column} the grid is: {grid}")
    else:
        return "Column can not be added because it's length does'nt match the number of rows"
def DisplayGrid(grid):
    if(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j],end=" ")
            print("")
    else:
        print("Grid is empty")
def SumValues(grid):
    sum=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum+=grid[i][j]
    return sum

#Driver
grid=[[1,2],[3,4]]
AddRow(grid,[5,6])
AddRow(grid,[7,8])
AddColumn(grid,[2,3,4,4])
DisplayGrid(grid)
print(f"Sum of Grid Values: {SumValues(grid)}")