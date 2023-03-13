# This program says hello and asks for your name

print('Hello, world')
print('What is your name ?') # Asking or user name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of you name is: ')
print(len(myName))
print('What is your Age? ') # asking for user age
try:
    myAge = int(input())
except ValueError:
    print('Enter a valid age . e.g 34')
else:
    print('You will be ' + str(myAge + 1) + ' in a year.')
