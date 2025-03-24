import time 

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('The timer is up!')

try:
    t = input('Enter the time in seconds: ')
    int(t)
except ValueError:
    print('Please enter a valid number.')
else:
    countdown(int(t))
