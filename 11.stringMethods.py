print("Hello".upper(),": upper() Makes all letters in upper case")
print("Hello".lower(),": lower() Makes all letters in lower case")
print("Hello".casefold(),": casefold() Makes all letters in lower case") #same as lower()
print("hello".capitalize(),": Makes only first letters in upper case")
print("Hello".find('l'),": find('l') prints first occuring index of character passed as parameter")
print("Hello".replace("Hello","hi"),": replace(Hello,hi) Replaces one string with another")
print("Hello".join("* "),": join('* ') takes all items in an iterable and joins them into one string.")
print("123".isdigit(),": isdigit() return true if the string has all digits")
print("Hello".isalpha(),": isalpha() returns true if the string has alphabets")
print("1k".isalnum(),": isalnum() returns true if the string has int or alphabets")
print("1232645247848287842".count("2"),": count('2') returns no of times 2 is repeated")
print("hello".endswith('o'),": endswith('o') returns true if the string ends with passed parameter")
print("Hello".index('e'),": index('e') returns index of the passed parameter")