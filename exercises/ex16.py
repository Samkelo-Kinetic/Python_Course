#Reading and Writing Files
#Importing libraries to the script
from sys import argv

script, filename = argv
#Printing a string as a sentence to the screen prompting file naming to the user
print "We're going to erase %r." % filename
#Printing a string as a sentence to the screen prompting a user for input
print "If you don't want that, hit CTRL-C (^C)"
#Printing a string as a sentence to the screen prompting user for RETURN button.
print "If you do want that, hit RETURN."
#Perfoming the raw input by means of opening the text file
raw_input("?")
#Printing strings as sentence to the screen
print "Opening the file..."
#Opening the file name created in the preceeding stepsyyh
target = open(filename, 'w')
#Printing the string sentence in the screen
print "Truncating the file. Goodbye!"
#Empties the file. Watch out if you care about the file
target.truncate()
#Printing to the string sentence to the screen
print "Now I'm going to ask you for three lines."
#Printing line sentences 
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")
#Printing to the string to the screen
print "I'm going to write these to the file"
#Printing sentence on line 1 followed by an escape sequence which enters a new line
target.write(line1)
#Escape sequence: new line
target.write("\n")
#Printing sentence on line 1 followed by an escape sequence which enters a new line
target.write(line2)
#Escape sequence: new line
target.write("\n")
#Printing sentence on line 1 followed by an escape sequence which enters a new line
target.write(line3)
#Escape sequence: new line
target.write("\n")
#
print "And finally, we close it."
target.close()