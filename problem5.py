"""
#problem5 - Basic data types challenges
#Lists

    insert i e: Insert integer at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
"""
print("input n the number of commands that we will enter")
n = int(input())
l = []
for _ in range(n):
    print("input s")
    s = input().split()
    print("value stored in s is", s)
    cmd = s[0]
    print("value stored in cmd is",cmd)
    args = s[1:]
    print("value stored in args is",args)
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        print(cmd)
        print("entering eval")
        eval("l." + cmd)
    else:
        print("printing l")
        print(l)
