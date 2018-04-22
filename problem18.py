#string challenges
#problem18 - capitalize
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
string = input()
print(' '.join(i.capitalize() for i in string.split(' ')))
