# simple function
# A function takes some input and has output


def thing():
    print('Hello')
    print('Fun')


thing()
print('Zip')
thing()

# max() and min() function (built-in function)
print(max('Hello Python'))
print(min('Hello Python'))
print(max('123.t'))

# function with parameters


def greet(lang):
    if lang == 'es':
        print('haha1')
    elif lang == 'ma':
        print('haha2')
    else:
        print('haha3')


greet('ma')


# function with parameters and return


def say(para1):
    return 'Hello ' + para1


print('Nice ' + say('Mos'))  # output below is the same
print('Nice ', say('Mos'))
print('Nice', 1)

# More function with parameters and return


def mymethod(para2):
    print('Begin')
    for i in range(1, para2 + 1):
        for j in range(i):
            print('*', end='')
        print('')
    print('End!')


mymethod(6)


# there can be multiple parameters in a function


def interesting(para3, para4):
    print(para3, 'yeah')
    for i in range(1, para4 + 1):
        for j in range(i):
            print('*', end='')
        print('')
    print('End!')




# more multiple parameters in a function
# function with return: **fruitful** function
# function without return: **non-fruitful** function


def addtwo(a, b):
    added = a + b
    return added


print(addtwo(3, 5))
print(addtwo('Hello ', 'Python!'))  # cool! parameter can be int and str!


# another example
def stuff():
    print('Hello')
    return


print(stuff())
stuff()
