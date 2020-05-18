# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther"])
# print(wild_animals)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# print(farm_animals)
# print(wild_animals)

################
# even = set(range(0,40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = {4, 6, 9, 16, 25}
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# #UNION method
# print(even.union(squares))
# print(len(even.union(squares)))
# ############
# #INTERSECTION method
# print("=" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

#########
# differences
# even = set(range(0,40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# even = set(range(0,40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# print("symmetric even minus squares")
# print(even.symmetric_difference(squares))
#
# print("squares even minus symmetric")
# print(squares.symmetric_difference(even))
# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # no error
#
# print(squares)
# if 8 in squares:
#     squares.remove(8)


###sub/supersets

# even = set(range(0,40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# if (squares.issubset(even)):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

#immutable sets
even = frozenset(range(0, 100, 2))
print(even)
