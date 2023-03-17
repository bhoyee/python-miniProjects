# using flow control with indentation

#using if else condition
print ('Enter name: ')
name = input()
if name == 'Python':
    print('Welcome ' + name)
    print ('Enter password: ')
    password = input()
    if password == '12345':
        print('Access granted')
    else:
        print('Invalid password')
else:
    print('invalid name')

spam = 0
if spam < 5:
    print('Hello, world')
    spam = spam + 1

#using while loop
#The while loop keep looping its condition is True
while spam < 5:
    print(spam)
    spam = spam + 1


#using while loop with break
while True:
    print('Please type your name: ')
    name = input()
    if name == 'your name':
        break
print('Thank you')

#using while loop with continue and break
while True:
    print ('Who are you?')
    name = input()
    if name != 'Tom':
        continue
    print ('Hello, Tom. What is the password ? ( it is a fish.)')
    password = input()
    if password == '123':
        break
print('Access granted')


# for Loops and the range() Function
# this is use to execute a block of code only for a certain number of times
x = range(2, 10, 5)
for i in x:
    print(i)

print('My name is ')
for i in range(5):
    print('Jimmy Five Time(' + str(i) + ')') # this print 5 times


total = 0
for num in range(101):
    total = total + num
print(total)

# using while loop to do the for loop job 
print ('My name is')
i = 0
while i < 5 :
    print ('Jimmy Five Times (' + str(i) +')')
    i = i + 1


# using modules

import random
for i in range(5):
    print(random.randint(1,10))


# working with function 
import random

def getAnswer(answerNumber): #elear a function
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber >= 7:
        return 'You in the right path'
    elif answerNumber >3 and answerNumber < 7 :
        return 'it still fair'
    elif answerNumber < 1:
        return 'bad request'
    
r = random.randint(-1, 9)

print('This number generated is', + r)
fortune = getAnswer(r)
print(fortune)

# using local and global variable

eggs = 5  # global variable
def spam1():
    eggs = 31333 # local variable
spam1()


# handling exception handling
def spams(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error : Invalid argument.')

print(spams(0))

# working with list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    

# using in and not in operators

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
 print('I do not have a pet named ' + name)
else:
 print(name + ' is my pet.')