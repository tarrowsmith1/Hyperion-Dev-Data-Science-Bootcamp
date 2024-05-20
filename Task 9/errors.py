# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #syntax error - no brackets on print statement
print("\n") #syntax error - no brackets on print statement

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"
#syntax error - one = sign needed rather than two
age = int(age_Str[0:2])
#syntax error - cannot convert age_Str into integer so retrieve 24 from string
print("I'm " + str(age) + " years old.")
#not an error that will prevent program from running but more spaces for readability


# Variables declaring additional years and printing the total years of age
years_from_now = 3 #syntax error - unneeded indentation, " should be removed so variable is integer
total_years = age + years_from_now

print("The total number of years: " + str(total_years)) #syntax error- no brackets on print statement, total_years instead of answer_years, no "" needed on total_years, space needed for readability

#Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 #syntax error - misspelling of total_years
print ("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old")
#syntax error - brackets around print statement, concatenate total months to display
#logical error - total months is 3 years from now not 3 years and 6 months so add 6
#HINT, 330 months is the correct answer
