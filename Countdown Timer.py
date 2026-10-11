import time

print('\nWELCOME TO YOUR COUNTDOWN TIMER\n___________________________________\n')
minutes = int(input('Minutes: '))
secs = int(input('Seconds: '))

total = minutes * 60 + secs

while total > 0:
    m = total // 60
    s = total % 60
    print(str(m) + ':' + str(s))
    time.sleep(1)
    total = total - 1

print('\nTime is up!\n')