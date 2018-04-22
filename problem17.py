#string challenge
#problem17- textwarp
#You are given a string and width .Your task is to wrap the string into a paragraph of width .
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)
print(wrap(input(),int(input())))
