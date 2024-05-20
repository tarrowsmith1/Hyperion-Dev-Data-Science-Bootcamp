#initialise number of rows
rows=9
#for loop in range between 1 and row + 1
for i in range(1,rows+1):
    #if loop for first 5 rows
    if (i<=(rows+1)/2):
        #print asterisks amount of times as the row number
        print("*"*i)
    #else loop for final 4 rows
    else:
        #print asterisks at the number of total rows minus row number minus one
        print("*"*((rows+1)-i))

        