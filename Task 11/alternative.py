#ask user for a string
string = input("Write a sentence: ")
#initalise alternating caps string
alternate_string = ""

#for loop for all letters in the string
for i in range (0,len(string)):
    #if statement where if position of letter is even (starting from 0), turn letter uppercase and add to alternate_string
    if i%2==0:
        alternate_string+=string[i].upper()
    #else statement where if position of letter is not even, , turn letter lowercase and add to alternate_string
    else:
        alternate_string+=string[i].lower()

#print alternating caps string
print(alternate_string)

#initialise variable words of the string split up into seperate words
words = string.split(' ')
#create list to add alternating case words to
alternate_words = []

#for loop for all words in the string
for i in range (0,len(words)):
    #if statement where if position of word is even (starting from 0), turn word lowercase and add to the end of alternate_words list
    if i % 2 == 0:
        alternate_words.append(words[i].lower())
    #else statement where if position of word is not even, turn word uppercase and add to the end of alternate_words list
    else:
        alternate_words.append(words[i].upper())

#print list of alternating case words with a space between the words
print(" ".join(alternate_words))
