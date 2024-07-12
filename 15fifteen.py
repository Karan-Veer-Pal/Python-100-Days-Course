# Day : 15 Exercise : 2 

# Questions : Create a python Program capaable of greeting you with Good Mornin, Good Attention & Good Evening. Your program should use time module to get the current hour. Here, is a simple program and documentation link for you. 

import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

if(timestamp.hour < 12):
    print("Good Morning")
elif(timestamp.hour >= 12):
    print("Good Afternoon")
elif(timestamp.hour <= 16):
    print("Good Afternoon")
else:
    print("Good Evening")