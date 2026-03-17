import time

timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

name = input("Enter your name: ")

if 0 <= hour < 12:
    print(f"Good Morning, {name}")
elif 12 <= hour < 18:
    print(f"Good Afternoon, {name}")
else:
    print(f"Good Evening, {name}")
