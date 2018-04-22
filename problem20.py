#string challange
#problem20 - merge the tools
#Any repeat occurrence of a character is removed from the string
s=input()
k=int(input())
n=len(s)

for i in range(0, n, k):
    slice_string = s[i : i+k]
    final_string =[]
    for y in slice_string:
        if y not in final_string:
            final_string.append(y)
    print(''.join(final_string))
