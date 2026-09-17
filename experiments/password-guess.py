import random
import time

def checkPassword(x:int,y:int):
    if x==y:
        return True
    else:
        return False

def loopCheck():
    l=[]
    num=int(input())
    time1=time.time()
    while True:
        number=random.randint(1000,9999)
        if number in l:
            continue
        else:
            if checkPassword(num,number) is True:
                time2=time.time()
                print(f"Caught it! {num} {number}\nTime taken: {time2-time1}\nAttempts: {len(l)}")
                break
            else:
                l.append(number)
                print(f"Tried number {number} :(")
                continue
    return
loopCheck()
#i tried that, the password was 6349 and it guessed in 3125 attempts lol
#and time taken 0.8799097537994385 now think about c++
#the number of attempts is impressive actually, if you would do number wise, it would take 5349 attempts or something, so random was impressive
#but again, wouldn't work similarly, maybe the next time it takes more, who knows?
