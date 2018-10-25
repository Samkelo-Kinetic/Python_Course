#Reading Files
#Libraries
from sys import argv
#Argument variables 
script, filename = argv
#openning the text file
txt = open(filename)
#Writing the textual content within the text file
print "Here's your file %r:" % filename
#printing the textual content to the screen
print txt.read()
#Requires a user to re-enter the file name
print "Type the filename again:"
#Showing the file to the screen using the raw _input()
file_again = raw_input("> ")
#Opening the file 
txt_again = open(file_again)
#Printing the textual content to the screen
print txt_again.read()