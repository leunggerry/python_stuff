fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a amll, sweet fruit grow in bunches",
         "lime": "a sour, green citrus fruit"}

#print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "lovely....mhmm",
       "spinach": "can i have some more"}
#print(veg)


# veg.update(fruit) #no new object is returned
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)
