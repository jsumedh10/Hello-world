########################################################################
# This program gives the number of occurences of a substring
########################################################################
string = input()
sub = input()
count = 0
for i in range(0,len(string)):
    if string[i:i+len(sub)]==sub:
        count+=1
print(count)
