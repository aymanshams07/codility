A = "()[]{}()[]{}"
print(A)
stack = []
for i in A:
    if i == "(" or i == "[" or i == "{":
        stack.append(i)
        print("this is stack", stack)
    elif i == ")":
        stack.pop()
    elif i == "]":
        stack.pop()
    elif i == "}":
        stack.pop()
        