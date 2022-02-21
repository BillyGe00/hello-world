
print('Hello world!')

# storing categories as a list
food = ['snacks', 'fruits', 'meat', 'vegetables']

# storing items in sets
snacks = ('chips', 'chocolate', 'cookies')
fruits = ('apples', 'bananas', 'oranges', 'watermelons', 'strawberries', 'lemons', 'peaches')
meat = ('beef', 'pork', 'chicken')
vegetables = ('broccoli', 'carrots', 'potatoes', 'asparagus', 'eggplant')

# create an empty list that stores sets from above
s = []
s.append(snacks)
s.append(fruits)
s.append(meat)
s.append(vegetables)

# create an empty dictionary
dic = {}

# pair categories and items and store each pair in the dictionary
for x in range(4):
    dic[food[x]] = s[x]

# print the dictionary
for x in dic:
    print(x + ": " + str(dic[x]))
