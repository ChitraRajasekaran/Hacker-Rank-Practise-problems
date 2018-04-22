#string challenges
#problem16 - string validators
#Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
s = input()
for f in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
	print(any(getattr(c, f)() for c in s))
