#################
#program for reversing a string wordwise
#################
import string
inputString=input("enter a string to reverse: ")

#split the string into words and put those words in a list
wordList=inputString.split()

senReverse=" ".join(reversed(wordList))
print(senReverse)        
