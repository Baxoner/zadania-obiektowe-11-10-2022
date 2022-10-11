def task1():
    while True:
        if input('[sudo] password for user: ') == 'root':
            print('Password correct, thou shall pass to rest of the code')
            break
        else:
            print('Try again')

def task2():
    nums = str.split(input('Enter 6 numbers the space as a separator: '), ' ')
    print(nums)
    sum = 0
    for i in range(6):
        sum += int(i)
    if sum > 30:
        print('Sum is greater than 30')
    

task1()
task2()