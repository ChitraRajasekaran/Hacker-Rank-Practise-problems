#basic datatype challenges
#problem7- list comprehensions
#You are given three integers(x,y,z)representing
#the dimensions of a cuboid along with an integer N .
#You have to print a list of all possible coordinates given by on a 3D grid
#where the sum of is not equal to N.

x = int(input())
y = int(input())
z = int(input())
N = int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != N)])
