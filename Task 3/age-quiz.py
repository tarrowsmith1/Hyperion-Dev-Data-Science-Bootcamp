#request age from user and store as integer variable
age=int(input("How old are you? "))

#if statement for what message for the age
if age>100:
    print("Sorry, you're dead.")
elif age>65:
    print("Enjoy your retirement!")          
elif age>40:
    print("You're over the hill.")
elif (age==21):
    print("Congrats on your 21st!")
elif age<13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")