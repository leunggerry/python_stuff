# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.
string = "1234567890"

myIterator = iter(string)
# print(myIterator)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
#
# print(next(myIterator))

#implicitly defined as an iterator
# for char in string:
#     print char
#
# #explicity dfined as an iterator
# for char in iter(string):
#     print char

for i in range(len(string)):
    print(next(myIterator))
