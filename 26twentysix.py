# Day : 26 Solution of Exercise 2

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("Enter Hour: "))
print(hour)

if(hour >= 0 and hour < 12):
    print("Good Morning Sir!")
elif(hour >= 12 and hour < 16):
    print("Good Afternoon Sir!")
elif(hour >= 16 and hour < 20):
    print("Good Evening Sir!")
elif(hour >= 20 and hour <= 24):
    print("Good Night Sir!")