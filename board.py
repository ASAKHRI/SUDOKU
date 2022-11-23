def print_board(bo):
  for i in range(len(bo)): # for loop iterating through each row.  'i' is the row, and 'j' is each value in each row. 
    if i % 3 == 0 and i != 0: print("- - - - - - - - - - - -")
    
    for j in range(len(bo[0])): #iterating through each column of each row.
      if j % 3 == 0 and j != 0: print(" | ", end="")
        
      if j == 8: print(bo[i][j])
      else: print(bo[i][j], end=" ")
print_board(bo)

