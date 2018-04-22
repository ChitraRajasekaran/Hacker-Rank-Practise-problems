#String challenges
#problem14 - Mutations
#Read a given string, change the character at a given index and then print the modified string.
def mutate_string(s):
    i,c = input().split()
    print(s[:int(i)]+ c + s[int(i)+1:])
s = mutate_string(input())


"""Alternative code
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    return ''.join(l)
"""
