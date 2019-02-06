# List
# a list element can be any python object - even another list
# a list can be empty
print([1, 2, 3])
print(['red', 'yellow', 'blue'])
print(['pink', 1, 2.5, [6, 8], 'cool!'])

# List index
myList = ['pink', 1, 2.5, [6, 8], 'cool!']
print(myList[4])

# Lists are mutable
# but strings are not
myList[2] = 25
print(myList)

myString = 'hello'
print(myString[2])
# myString[2] = 's'  # traceback error

# List function ** len() ** similar to String
# other simple functions: max() min() sum()
print(len(myList))

# Function ** range() **
# return s a list
a = range(4)
print(len(a))
# a[1:3] from index 1 to 2
# a[1:]
print(a)
print(range(2, 6))

# to know more list methods
# x = list()
# type(x)
# dir(x)

# List method ** append() **
# Building a List from scratch
stuff = list()
stuff.append('hello')
stuff.append(99)
stuff.append('hello')
print(stuff)

# List method ** remove() **
# remove the 1st target item (just one)
stuff.remove('hello')
print(stuff)

# List operators ** in ** and ** not in **
# return True or False
myList = ['pink', 1, 2.5, [6, 8], 'cool!']
print(1 in myList)
print('pink' not in myList)

# List method ** .sort() **
# does NOT return value, make change on the original list
numbers = [1, 4, 344, 66, 9, 22]
numbers.sort()
print(numbers)

# string method ** .split() **
# return a list, separate by white space
# change every word in string into list
abc = 'have       a nice day'
print(abc.split())
print(len(abc))
print(len(abc.split()))
print(abc.split()[2])
for w in abc.split():
    print(w)

# parameter of .split(): delimiter !!!
print(abc.split(' '))
cba = 'nice, to, meet, you'
print(cba.split())
print(cba.split(','))
print(cba.split(', '))

# The double split pattern
line = 'my e-mail address is hsoaj@lovely sdi'
a = line.split()
b = a[4].split('@')
print(b[1])

# combine lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# bounds:
# && in python3: and
# || in python3: or
