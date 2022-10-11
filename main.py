def task1():
    while True:
        if input('[sudo] password for user: ') == 'root':
            print('Password correct, thou shall pass to rest of the code')
            break
        else:
            print('Try again')

def task2():
    nums = str.split(input('Enter 6 numbers the space as a separator: '), ' ')
    sum = 0
    for i in range(6):
        sum += int(nums[i])
    if sum > 30:
        print('Sum is greater than 30')
    else:
        print('Sum is less than 30')
    
def task3():
    num = int(input('Enter a number: '))
    if num > 0:
        print(f'{num} is a positive number')
    elif num < 0:
        print(f'{num} is a negative number')
    else:
        print(f'{num} is zero')

def task4():
    nums = str.split(input('Enter 2 numbers the space as a separator: '), ' ')
    if int(nums[0]) <= int(nums[1]):
        print(nums[0], nums[1])
    else:
        print(nums[1], nums[0])

def task5():
    quantity = int(input('Enter print quantity: '))
    pricePerSinglePrint = 10
    if quantity >= 500 and quantity <= 1000:
        pricePerSinglePrint = 12
    elif quantity < 500:
        pricePerSinglePrint = 15
    total = quantity*pricePerSinglePrint
    print(f'Total is {total} zł')

def task6():
    distance = float(input('Enter travel distance [km]: '))
    if distance < 10:
        price = 20
    else:
        if distance <= 30:
            price = 10 + (.1*distance)
        else:
            price = 1 + (.8*distance)
    print(f'Total is {price} zł')

def task7():
    while not valid:
        day = int(input('Enter week day [0-6]: '))
        for i in range(7):
            if i == day:
                valid = True
    
    if day == 0 or day == 6:
        print('Sat-Sun: Closed')
    elif day == 1:
        print('Mon: 10 - 14')
    elif day == 2:
        print('Tue: 10 - 19')
    elif day >= 3 and day <= 5:
        print('Wed-Fri: 11 - 16')

def task8():
    nums = str.split(input('Enter 3 numbers the space as a separator: '), ' ')
    even = True
    for i in range(3):
        if int(nums[i]) % 2 != 0:
            even = False
            break
    if even:
        print('Numbers are even')
    else:
        print('Numbers are not even')

def task9():
    strings = []
    for i in range(3):
        strings.append(input('Enter a string: '))
    print()
    if '' in strings:
        print('At least one string is empty')
    else:
        print('Strings are not empty')

def task10():
    maxLength = 10
    stringLength = len(input('Enter a string: '))
    if stringLength < maxLength:
        print(maxLength-stringLength, 'characters left to maximum string length')
    print(f'String length is {stringLength}')

def task11():
    amountOfPeople = int(input('Enter amount of people: '))
    nights = int(input('Enter amount of nights in hotel: '))
    price = 50
    if nights <= 7 and nights >= 4:
        price = 75
    elif nights < 4:
        price = 100
    print(f'Total is {price*amountOfPeople*nights}')

task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()