# this check if the user enter digit and if not negative number
while True:
    print('Enter your age')
    age = input()
    try:
        age = int(age)
    except:
        print('Enter only digit number')
        continue
    if age < 1:
        print('Please enter a positive number')
        continue
    break
print(f'Your age is {age}.')
