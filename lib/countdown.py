import time

def countdown(sec):
    while sec > 0:
        print(f'{sec} SECOND(S)!')
        sec -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(sec):
    while sec > 0:
        print(f'{sec} SECOND(S)!')
        sec -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


countdown_with_sleep(5)