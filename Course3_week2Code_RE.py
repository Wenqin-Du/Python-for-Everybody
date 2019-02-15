# Regular Expression
import re

# ex1 Using re.search() like find()
handle = open('example1.txt')
for line in handle:
    line = line.rstrip()
    if line.find('Nice') >= 0:
        print(line.find('Nice'))
        print(line)

# Same result using re.search()
hand = open('example1.txt')
for line in hand:
    line = line.rstrip()
    if re.search('Nice', line):
        print(line)

# ex2 Using re.search() like startswith()
handle = open('example1.txt')
for line in handle:
    line = line.rstrip()
    if line.startswith('Nice'):
        print(line)

# Same result using re.search()
hand = open('example1.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^Nice', line):
        print(line)

# Python Regular Expression Quick Guide
# https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

# **re.search()** returns a T/F depending on whether the string matches the regular expression
# **re.findall** match strings to be extracted, return a List of the matches of the regular expression

x1 = 'haha 12 jdjd 889 ddfkf 1 dsd 0 999'
y0 = re.findall('[0-8]+', x1)
y1 = re.findall('[0-9]+', x1)
print(y0)
print(y1)

x2 = 'X-Sieve: CMU CC Sieve 2.3'
y2 = re.findall('^X-\S+:', x2)
y3 = re.findall('[ABCDE]', x2)
y4 = re.findall('[ABCDE]+', x2)
print(y2)
print(y3)
print(y4)

# Warning: Greedy Matching: re.findall() returns the list of the longest matching (alap the string)
# if non-greedy, use '+?' and '*?'

x3 = 'From: Using the  : character'
y5 = re.findall('^F.+:', x3)  # greedy
y6 = re.findall('^F.+?:', x3)   # non-greedy
print(y5)
print(y6)

x4 = 'From wenqin.Du@colostate.za Sat Jan 5 2019'
y7 = re.findall('\S@\S', x4)  # non-greedy
y8 = re.findall('\S+@\S+', x4)  # greedy
print(y7)
print(y8)

# adjust how re.findall() works by using parentheses
# just return the part of string in the form within the parentheses

y9 = re.findall('^From (\S+@\S+)', x4)  # careful about the whitspace!
y10 = re.findall('^From(\S+@\S+)', x4) 
print(y9)
print(y10)  # will return an empty list

y11 = re.findall('@([^ ]*)', x4)  # From @ and match non-blank character and match many of them
print(y11)

# use \$ to represent real dollar sign
# just print out the number of the money
x5 = 'i have $12.56 for you'
y12 = re.findall('\$([0-9.]+)', x5)
print(y12)
