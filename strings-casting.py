# Strings and Casting
greetings = 'Hello World!'
single_quotes = 'single quotes \'WOW\''
double_quotes = "double quotes 'WOW'"
print(single_quotes)
print(double_quotes)

# Indexing starts from 0
# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

# String slicing
print(greetings[0:5]) # Prints first 5 characters in greetings
print(greetings[6:11]) # Prints characters 5-11
print(greetings[-1]) # Prints the final character in greetings


# Concatenation and Casting
first_name = "Jordan"
last_name = "Clarke"
age = 24
# Print first name and last name with age converted to string
print(first_name + " " + last_name + ", is " + str(age))
print(first_name, last_name, age)
# F- String is useful for formatting f
print(f"{first_name} {last_name} is {age}")