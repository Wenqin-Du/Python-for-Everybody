# Dictionary like bags. No order. For Lists
# like HashMap in Java
# common use: Building a histogram counting the occurrences of various strings in a file
# We label the contents in ** dict() ** the label called key
# when print out, the elements will be in {key:value - pairs}
purse = dict()
purse['a'] = 12
purse['b'] = 3
purse['c'] = 75
print(purse)
print(purse['b'])
purse['b'] = purse['a'] + 1
print(purse)

# can make an empty dictionary using empty curly braces
purs = {}
print(purs)
pus = {'h1': 2, 'h2': 3}
print(pus)

# it's an error to reference a key which is not in the dictionary
# can use ** in ** to see if a key is in a dictionary
print('d' in purse)

# Example: Counting names
counts = dict()
names = ['dwq', 'dwq', 'ly', 'dwq', 'ly']
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
print(counts)

# Dict method ** .get(key, default value) **
# return the value of key, if key does not exist, return default value
x = counts.get('ly', 0)
y = counts.get('lm', 0)
print(x, y)

# a quicker way to solve the example above
counts = dict()
names = ['dwq', 'dwq', 'ly', 'dwq', 'ly']
for name in names:
    # combine if&else in one line
    counts[name] = counts.get(name, 0) + 1
print(counts)

# for loop for dict()
# for loop iterate through the KEY
for key in counts:
    print(key, counts[key])

# get a ** List ** of keys, values and items(both) from a dictionary
print(list(counts))
print(counts.keys())  # same as above
print(counts.values())
print(counts.items())  # return list of tuples

# counting pattern
counts = dict()
line = input('print a line and I will count the words')
wordsList = line.split()
print('Your Words List: ', wordsList)
for word in wordsList:
    counts[word] = counts.get(word, 0) + 1
print('Counts: ', counts)

# Two Iteration Variables - Cool!!!
for k, v in counts.items():
    print(k, v)

# A Good Task
# counts the variable whose occur time is  the most
name = input('Enter File name: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None
for k, v in counts.items():
    if bigCount is None or v > bigCount:
        bigWord = k
        bigCount = v

print(bigWord, bigCount)

# better (when two or more words have the same count)
for k, v in counts.items():
    if v == bigCount:
        print(k, v)

# count the number of characters in a string
a = 'aabbbcdd'
counts = dict()
for i in range(len(a)):
    counts[a[i]] = counts.get(a[i], 0) + 1
print(counts)
for key in counts:
    print(key, counts[key])
