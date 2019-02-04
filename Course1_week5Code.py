# if statement
x = 25
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')
    print('bigger')
    print('bigger')
    print('another bigger')
    print('tab')
print('finish')

# if-else statement
x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

# nested if statement
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than one hundred')
print('All done')

# Multi-way if statement **elif**
x = 9
if x < 2:
    print('Small')
elif x < 6:
    print('Medium')
else:
    print('Large')
print('All done')


# for loop (nested with if statement)
for i in range(5):
    print(i, i)
    if i > 2:
        print('bigger than 2')
    print('Done with i', i)
print('All done')

# try/except structure (element/check traceback)
astr = 'hello bob!'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

# more on try/except structure (where to jump out of try)
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)

# more on try/except structure
rawstr = input('Enter a positive number: ')
try:
    ival = int(rawstr)
except:
    ival = - 1
if ival > 0:
    print('Nice work')
else:
    print('Not a positive number')

# quit() will not execute any following code
# print(1)
# quit()
# print(2)

# while loop with break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

# while loop with continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# nested while loop with break
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

# while loop in string **a** here is a list
# pop() delete element(the last one -1)
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))
print(a)

a = ['foo', 'bar', 'baz']
print(a.pop(1))
print(a[0])

