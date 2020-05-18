# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

vowels = set(["a", "e", "i", "o", "u", "y"]) #could use frozenset

# constanants = set(["b", "c", "d", "f", "g",
#                    "h", "j", "k", "l", "m",
#                    "n", "p", "q", "r", "s",
#                    "t", "v", "w", "x", "z"])
user_input = input("Enter a string: ")

finalSet = set(user_input).difference(vowels)
print(finalSet)

finalSet = sorted(finalSet)
print(finalSet)
