def task1():
    while True:
        if input('[sudo] password for user: ') == 'qwerty':
            print('Password correct, thou shall pass to rest of the code')
            break
        else:
            print('Try again')

