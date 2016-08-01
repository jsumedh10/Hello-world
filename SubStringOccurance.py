###############################################################################
# This program gives if the required substring is present in the input string
###############################################################################
string = input()
sub = input()
count = 0
for i in range(0,len(string)):
    if string[i:i+len(sub)]==sub:
        count+=1
print(count)
