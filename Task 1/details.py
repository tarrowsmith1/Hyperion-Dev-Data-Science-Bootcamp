#request input from user and store into variable called "name"
#request input from user and store into variable called "age"
#request input from user and store into variable called "house_num"
#request input from user and store into variable called "street_name"
#print sentence with variables inside it using f-string

name = input("What is your name? ")
age= input("What is your age? ")
house_num = input("What is your house number? ")
street_name = input("What is your street name? ")

print(f"This is {name}. He is {age} years old and lives at house number {house_num} on {street_name}.")