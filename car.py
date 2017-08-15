
gpio1='左进'
gpio2='左退'
gpio3='右进'
gpio4='右退'
while True:
    ch=input()
    if ch=='e':
        print(gpio1,gpio3)
    if ch=='d':
        print(gpio2,gpio4)
    if ch=='s':
        print(gpio2,gpio3)
    if ch=='f':
        print(gpio1,gpio4)
    if ch=='b':
        break

