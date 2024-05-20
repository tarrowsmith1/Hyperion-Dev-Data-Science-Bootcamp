#initialise variables for sum and the amount of numbers collected
sum=0
count=0
#ask user for number
number = int(input("Pick a number: "))
#while loop for when number is not -1
while number!=-1:
    #add number chosen to sum and add one to count
    sum+=number
    count+=1
    #ask for number from user again
    number = int(input("Pick a number: "))
#calculate and display average of numbers entered excluding -1
print(f"The average is {sum/count}")
