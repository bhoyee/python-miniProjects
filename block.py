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
