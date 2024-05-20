#request input from user
str_manip = input("Write a sentence: ")

#print length of sentence
print(len(str_manip))
#print out manipulated sentences
print(str_manip.replace(str_manip[-1],"@"))
print(str_manip[:-4:-1])
print(str_manip[:3] + str_manip[-2:])
