# A = "()[]{}()[]{}"
# print(A)
def solution(A):
    stack = []
    for i in A:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
            # print("this is stack", stack)
        elif i == ")":
            stack.pop()
        elif i == "]":
            stack.pop()
        elif i == "}":
            stack.pop()

    print("this is end_stack", stack)
    if not stack:
        return print("true")
    else:
        print("falsee!")


print(solution("()[]{{()[]{}"))


