#String collections
#prioblem19 - minion gmae
#Your task is to determine the winner of the game and their score.
s = input()
vowels = 'AEIOU'
kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)
print("Kevin", kevsc)
print("Stuart", stusc)
