# Processing Files

# new line character ** \n **
# it is one character in string
greet = 'Hello\nPython'
print(greet)
print(len(greet))

# a file handle open for read can be treated as a sequence of strings
# each line in the file is a string in the sequence
# a sequence is a * ordered set *
# !!! iteration: sentence, will run line by line (# of line times)
firstFile = open('example1.txt')
print(firstFile)  # print out file information instead of contents
for sentence in firstFile:
    print(sentence)

# prompt for file name
fname = input('enter the file name: ')
try:
    myFile = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

# line counter for a file
firstFile = open('example1.txt')
count = 0
for line in firstFile:
    count += 1
print('Line Count:', count)

# File method ** file.read() ** read the whole thing into a string
# read the whole file (new lines and all)
# into a single string
firstFile = open('example1.txt')
print(len(firstFile.read()))

# search through a file using string method .startswith()
# delete the blank line
# Not a very good one
firstFile = open('example1.txt')
for sentence in firstFile:
    if sentence.startswith('Ni'):
        print(sentence, end="")

# a better one!!!
# .rstrip() throw the white space on the right
firstFile = open('example1.txt')
for sentence in firstFile:
    sentence = sentence.rstrip()
    if sentence.startswith('Ni'):
        print(sentence)

# skipping with ** continue **
# same effect as above :)
firstFile = open('example1.txt')
for sentence in firstFile:
    sentence = sentence.rstrip()
    if not sentence.startswith('Ni'):
        continue
    print(sentence)

# using ** in ** to select lines
firstFile = open('example1.txt')
for sentence in firstFile:
    sentence = sentence.rstrip()
    if 'Ni' not in sentence:
        continue
    print(sentence)
