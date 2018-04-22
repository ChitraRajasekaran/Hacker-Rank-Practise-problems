#String challenges
#problem11- SWAP case
#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
    print(''.join([i.lower() if i.isupper() else i.upper() for i in s]))
s = swap_case(input())
