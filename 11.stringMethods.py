print("Hello".upper(),": Makes all letters in upper case")
print("Hello".lower(),": Makes all letters in lower case")
print("Hello".casefold(),": Makes all letters in lower case") #same as lower()
print("hello".capitalize(),": Makes only first letters in upper case")
print("Hello".find('l'),": prints first occuring index of character passed as parameter")
print("Hello".replace("Hello","hi"),": Replaces one string with another")
print("Hello".join("* "),": takes all items in an iterable and joins them into one string.")
print("123".isdigit(),": return true if the string has all digits")
print("Hello".isalpha(),": returns true if the string has alphabets")
print("1K".isalnum(),": returns true if the string has int or alphabets")
print("1232645247848287842".count("2"),": returns no of times 2 is repeated")
print("hello".endswith('o'),": returns true if the string end with passed parameter")
print("Hello".index('e'),": returns index of the passed parameter")