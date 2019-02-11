# Tuple - limited version of lists ** use () **
# tuples are sort of a more efficient version of lists that you can't modify

# something same with list
x = ('a', 'b', 'c')
print(x[2])
y = (1, 9, 2)
print(max(y))

for iter in x:
    print(iter)

# lists are mutable
# strings and tuples are immutable
# more information:
l = list()
dir(l)
t = tuple()
dir(t)

# can put tuple on the left-hand-side of an assignment statement
(x, y, z) = ('Mos', 'q', 100)
print(y)

# dict.items() returns a list of tuples

# tuples are comparable (pair by pair)
(1, 2, 3) < (5, 0, 0)
('J', 'z') < ('a', 'A')

# tuple function: ** sorted() **
# can be sort (start from the first element)
# sort by key
d = {'a': 10, 'c': 5, 'b': 0}  # dictionary
d.items()  # tuple
print(sorted(d.items()))

for k, v in sorted(d.items()):
    print(k, v)

# tuple sort by values
# construct a list which inverse v and k
d = {'a': 10, 'c': 5, 'b': 0}
temp = list()
for k, v in d.items():
    temp.append((v, k))
print(temp)
temp = sorted(temp, reverse=True)  # Or default: from small to large
print(temp)

# even one line!
# List comprehension creates a dynamic list.
# here we make a list of reversed tuples and then sort it
print(sorted([(v, k) for k, v in d.items()], reverse=True))
