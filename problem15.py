#string challenges
#problem15 - find a string
#Output the integer number indicating the total number of occurrences of the substring in the original string.
def count_substring(string, sub_string):
    return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)])
print(count_substring(input(),input()))
