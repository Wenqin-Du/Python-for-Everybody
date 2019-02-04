# while loop


def example(number):
    n = number
    while n > 0:
        print(n)
        n -= 1
    print('Happy ending')
    print(n)  # when while loop ends, the result


example(5)

# breaking out of a while loop: break
while True:
    line = input('Please type in a line')
    if line == 'done':
        break
    print(line)
print('Done!')

# skip a specific iteration: continue
while True:
    line = input('Please type in a line')
    if line == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# simple for loop
for i in [5, 100, 3, 2, 1]:
    print(i)
print('Done!!')

# more interesting for loop
# friends: list of string
# name: iteration variable (for each of the value in the list)
add = input('Who t bless')
friends = [add, 'liu', 'jiang', 'wei']
for name in friends:
    print('Happy new year', name + '!')
print('Done!')

# for loop from week 6


def interesting(para3, para4):
    print(para3, 'yeah')
    for i in range(1, para4 + 1):
        for j in range(i):
            print('*', end='')
        print('')
    print('End!')


interesting('Start', 5)
interesting(123, 5)  # can be number!!!

# for loop - looping through a set
print('begin')
for thing in [2, 4, 5, 6, 75, 90]:
    print(thing)

# for loop - finding the average in a loop
count = 0
total = 0
for thing in [2, 4, 5, 6, 75, 90]:
    count += 1
    total += thing
print(total / count)

# for loop - filtering in a loop
for thing in [2, 4, 5, 6, 75, 90]:
    if thing > 20:
        print(thing)

# keyword *** None ***
# *** the "is" and "is not" logical operators *** "is the same as"
# similar to but stronger than ==
# finding the smallest value
smallest = None
for thing in [2, 4, 5, 6, 75, 90]:
    if smallest is None:
        smallest = thing
    elif smallest > thing:
        smallest = thing
print(smallest)

# chapter 5 exercise 1
count = 0
total = 0
answer = input('Emter a number: ')
while answer != 'done':
    try:
        answer = int(answer)
        count += 1
        total += answer
    except:
        print('Invalid input')
    answer = input('Emter a number: ')
print(total, count, total / count)

# make it better
count = 0
total = 0

while True:
    answer = input('Emter a number: ')
    if answer == 'done':
        break
    try:
        answer = int(answer)
        count += 1
        total += answer
    except:
        print('Invalid input')
print(total, count, total / count)
