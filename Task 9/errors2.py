# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error - "" needed for string
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")
#syntax error - f needed
#logical error - wrong variables in wrong part of sentence

print(full_spec) #syntax error - brackets needed
