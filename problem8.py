#basic datatype challenges
#problem 8 - find the runner up score
#You are given scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = map(int, input().split())
list = list(arr)
l = [x for x in list if x != max(list)]
print(max(l))
