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

task1()
task2()
task3()