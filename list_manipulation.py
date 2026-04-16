## first problem reverse a string
# RULE [START, END, STEP] or [START, END]
 # If you want a slice in regular order, STEP should be positive.
 # If you want a slice in reverse order, STEP should be negative.

#solution 2 :
# range(start, stop, step)
# len(s)-1 → last index
# -1 stop → goes until index 0
# step -1 → move backwards

string = 'whatthefuck'
reversed_string = ""
# print(string [::-1])

#print (len(string) -1)

for i in range(len(string) -1 , -1 , -1):
    reversed_string += string[i]
    print(reversed_string)

