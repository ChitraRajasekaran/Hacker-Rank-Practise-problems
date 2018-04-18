#Basic datatypes challenges
#problem6 - Tuples
#Given an integer and space-separated integers as input, create a tuple

n = input() # input number
iline = input() #input line
ilist = iline.split() #split the input to create a list
ilist = map(int,ilist) # change the string elements in the list to int
t = tuple(ilist) #converting list to tubple to be hashable
print(hash(t))
