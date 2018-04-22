#String challenges
#problem13 - Whats your name?
#The first line contains the first name, and the second line contains the last name.
def print_full_name(a, b):
    if len(a)<= 10 and len(b) <= 10:
        print("Hello %s %s! You just delved into python." %(a,b))
print_full_name(input(),input())
