#String Challenges
#problem12 - String Split and Join
#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    line_split = line.split(" ")
    line_join = "-".join(line_split)
    print(line_join)
line = split_and_join(input())
