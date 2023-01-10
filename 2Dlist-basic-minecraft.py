# A python program to learn the 2D list by making a smaller version of minesweep game.

#Following is the example grid that contains hyphens and hash. We have to replace hyphens with the numbers. The number will denote the surroundin hashes
grid = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["#", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "#"],
         ["-", "-", "-", "#", "-"] ]

#Another example grid
grid2 = [ ["#", "-", "#", "-"],
         ["#", "#", "#", "-"],
         ["-", "-", "-", "#"],
         ["#", "#", "#", "-"]
          ]

'''
    Program Logic - 
    We will apply 2 for loops to explore the 2D list.
    For each cell that is containing '-', count how many surrounding '#' are there.
    So, for each cell the program should look into 8 directions as :
        Up, Up-right, Right, Right-down, Down, Down-left, Left, Left-up
    Replace '-' with the count for that cell.    
'''

print("Original Grid")
for row_idx, row in enumerate(grid, start=0):
       for col_idx, col in enumerate(row, start=0):
              digit = 0
              print(grid[row_idx][col_idx], end=" ")
              if grid[row_idx][col_idx] == "-":
                     # Up direction
                     if (row_idx - 1) >= 0 and grid[row_idx - 1][col_idx] == "#":
                          digit = digit + 1
                     # Up-right direction
                     if (row_idx - 1) >= 0 and (col_idx + 1) < len(row) and grid[row_idx - 1][col_idx + 1] == "#":
                          digit = digit + 1
                     # Right direction
                     if (col_idx + 1) < len(row) and grid[row_idx][col_idx + 1] == "#":
                          digit = digit + 1
                     # Right-down direction
                     if (row_idx + 1) < len(grid) and (col_idx + 1) < len(row) and grid[row_idx + 1][col_idx + 1] == "#":
                          digit = digit + 1
                     # Down direction
                     if (row_idx+1) < len(grid) and grid[row_idx+1][col_idx] == "#":
                            digit = digit + 1
                     # Down-left direction
                     if (row_idx + 1) < len(grid) and (col_idx-1) >= 0 and grid[row_idx + 1][col_idx - 1] == "#":
                        digit = digit + 1
                     #Left direction
                     if (col_idx-1) >= 0 and grid[row_idx][col_idx-1] == "#":
                            digit = digit + 1
                     #Left-up direction
                     if (col_idx - 1) >= 0 and (row_idx-1) >= 0 and grid[row_idx-1][col_idx - 1] == "#":
                        digit = digit + 1

                     grid[row_idx][col_idx] = str(digit)

       print("")

print("\nNew minesweep found Grid")
#Display the modified list
for row in grid:
    for col in row:
        print(col + " ", end="")
    print()
