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

#uing while loop
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
    print ('Hello, Joe. What is the password ? ( it is a fish.)')
    password = input()
    if password == '123':
        break
print('Access granted')
