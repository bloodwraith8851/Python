# string creation

# strings are pieces of text like you name a sentence or even emojis
# we can use strings to store text data
# we can use "" , '' or """ """ to create strings

name = 'RAKESH'  # string variable
name2 = "RAKESH"  # another way to create a string variable
name3 = """RAKESH"""  # yet another way to create a string variable
name1 = '  RAKESH  '  # string with leading and trailing spaces
# indexing and slicing

# indexing is a way to access individual characters in a string
# each character in a string has a unique index, starting from 0 for the first character
# for example, in the string "hello", the characters are indexed as follows:

word= "hello"
#      01234

print(word[4])

# slicing is a way to access a range of characters in a string
# we can use the colon (:) operator to specify a range of indices

print(word[1:4])  # Output: ello
print(name[1:6])

# we can also use negative indices to access characters from the end of the string

#common strings methods
# len() - returns the length of the string
# upper() - converts all characters to uppercase
# lower() - converts all characters to lowercase
# strip() - removes leading and trailing whitespace
# replace(old, new) - replaces occurrences of 'old' with 'new'
# we can use these methods to manipulate strings in various ways

#example
print(name.upper())
print(len(name))
print(name.lower())
print(name1.strip())
print(name.replace("RAKESH", "Nidhi"))

#string formatting
# we can use f-strings to format strings in python
#example
age = 15
name4 = "Nidhi"
print(f"my name is {name4} and my age is {age}")
#or
print("my name is {} and my age is {}".format(name4,age))

#example

robot = "bot"
print(f"{robot} wants a vacation. Too much coding!")

#practice questions
#1 write ur name in uppercase and lowercase using upper() and lower() methods
#2 first 3 letter of your name using slicing
#3 length of your name using len() function
#4 replace your name with another name using replace() method
#5 format a string with your name and age using f-strings