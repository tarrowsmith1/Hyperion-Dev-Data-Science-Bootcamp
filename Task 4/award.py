#ask user for times for triathlon
swimming = int(input("Enter the swimming time in minutes: "))
cycling = int(input("Enter the cycling time in minutes: "))
running = int(input("Enter the running time in minutes: "))

#store total time for triathlon and display time to user
totaltime=swimming+cycling+running
print(f"You completed the triathlon in {totaltime} minutes!")

#if statement for time up to 100 minutes   
if totaltime<=100:
    print("You achieved Provincial Colours")
#else if statement for time between 101 and 105
elif totaltime>100 and totaltime<=105:
    print("You achieved Provincial Half Colours")
#else if statement for time between 106 and 110
elif totaltime>105 and totaltime<=110:
    print("You achieved Provincial Scroll")
#else statement for not qualifying time
else:
    print("Sorry, you did not achieve an award.")