fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a amll, sweet fruit grow in bunches",
         "lime": "a sour, green citrus fruit"}

#print(fruit)
#print(fruit["apple"])

#can ADD to dictionary
#fruit["pear"] = "an odd shape apple"
#print(fruit)

#values cannot be added but rather replaced
#fruit ["pear"] = "great with tequila"
#print(fruit)

#REMOVE entries in the dictionary, always specify the key
#del fruit["lemon"]
#print(fruit)

#CLEAR the entire dictionary
#fruit.clear()
#print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we dont have a " + dict_key)
    #alternatively
    # description = fruit.get(dict_key, "we dont have a " + dict_key)
    # print(description)

# for snack in fruit:
#     print(fruit[snack])
#dicitionaries can comeout to be in different order all the time
# all keys are hashed
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 40)


# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# using valuse is less efficient
# for val in fruit.values():
#     print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# #tomato is updated behind the scenes
# print(fruit_keys)

print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

#Regular dictionary
print(dict(f_tuple))
