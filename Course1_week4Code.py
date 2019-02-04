# simple print out
ddd = 1 + 4
print(ddd)
eee = 'hello ' + 'python'
print(eee)

type(ddd)
type(eee)

# comma in print!! is space!  cool!
print('hello', 'mos', 'Q')

# simple calculation (different from Java!)
print(int(99 / 100))
print(99 / 100)

# use int() and float() to convert between strings and numbers
# get a error if the string does not contain numeric characters
word1 = '123'
type(word1)
number1 = int(word1)
print(number1 + 1)
print(float(number1) + 1)

# construct python to pause and read data from the user using input() function
# input() function returns a **string**
scanner = input('who are you')
print('Welcome ' + scanner)

# more on input (ex: convert elevator floor)
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)
