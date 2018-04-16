# Problem-2 - Loops
# Read an integer N. For all non-negative integers i< N, print i^2.
# 1<=N<=20

N = int(input())
if N in range(1,21):
    print("entering")
    for i in range(N):
        print(i**2)
else:
    print("not in range")
