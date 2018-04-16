#Problem3 - write a function
#You are given the year, and you have to write a function to check if the year is leap or not.
print("enter the year")
yr = int(input())
def is_leap(year):
    leap = 'FALSE'
    if (year%4 == 0) and (year%400 == 0 or year % 100 != 0):
        leap = 'TRUE'
        return leap
    else:
        return leap
loy = is_leap(yr)
print(loy)
