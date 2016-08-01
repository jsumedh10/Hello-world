#################
#program for reversing a string wordwise
#################

inputString=input("enter a string: ")

print(max(inputString.split(), key=len))
