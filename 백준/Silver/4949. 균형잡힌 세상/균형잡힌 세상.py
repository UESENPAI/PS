import sys

while True:
    string = list(sys.stdin.readline().rstrip())

    if string[0]==".":
        exit()

    stack = []
    for s in string:
        if s == "(" or s=="[":
            stack.append(s)
        elif s == ")":
            if len(stack) and stack[-1]=="(": #chr(ord(s)+1):
                stack.pop()
            else:
                stack.append(s)
                break;
        elif s == "]":
            if len(stack) and stack[-1]=="[": #chr(ord(s)+2):
                stack.pop()
            else:
                stack.append(s)
                break;
    if len(stack): print("no")
    else: print("yes")
