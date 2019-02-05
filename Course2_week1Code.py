# index in String
fruit = 'strawberry'
letter = fruit[0]
word = fruit[0: 3]  # up to but NOT including index 3
print(letter)
print(word)

print(fruit[: 3])
print(fruit[3:])
print(fruit[:])  # do not need to


# length of String using function ** len() **
print(len(fruit))

# Looping through Strings
fruit = 'strawberry'
for letter in fruit:
    print(letter)

# another approach (allow adding 2 every time)
fruit = 'strawberry'
index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1  # can be index += 2

# counting words in a string
fruit = 'strawberry'
total = 0
for letter in fruit:
    if letter == 'r':
        total += 1
print(total)

# String concatenation
a = 'Hello'
b = 'Python'
print(a + ' ' + b)
print(a, b)

# keyword ** in **
# can also test weather a string is in another string
# return a boolean
fruit = 'strawberry'
if 'a' in fruit:
    print('a yes')
if 'c' in fruit:
    print('c yes')

# you can compare string with < and > and ==
if 's' > 'S':
    print('s > S')

if 'b' > 'A':
    print('b > A')

if 'chunk' > 'Gu':
    print('chunk > Gu')

# String Library:
# .lower() .upper()
# show more in console
stuff = 'Hello Python'
type(stuff)
dir(stuff)

# String method ** find() **
# finds the first occurrence of a substring print out the index
# if not exist, return -1
fruit = 'strawberry'
print(fruit.find('tr'))
print(fruit.find('ljcrf'))

# String method ** replace() **
# search and replace
fruit = 'strawberry'
newFruit = fruit.replace('rr', 'o')
print(newFruit)
ß
fruit = ' strawberry'
newFruit = fruit.replace(' ', 'Mine')
print(newFruit)

# String method ** lstrip(), rstrip(), strip() **
# remove left, right, both sides whitespace
greet = '   Hello    Python    '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# Prefixes (in console)
line = 'Please have a nice day'
line.startswith('Please')
line.startswith('P')
line.startswith('p')

# Parsing and Extracting
data = 'hh kjddd.sdsd@goog.hh jskjf ijfi'
index = data.find('@')
aim = data.find(' ', index)  # search from index
print(data[index + 1: aim])

# Exercise 6.5
str = 'hahahaha: 0.86'
ipos = str.find(':')
print(float(str[ipos + 2:]))
