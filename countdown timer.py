import time as t

my_time = int(input("Enter the time in seconds: "))
for i in range(my_time,0,-1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    t.sleep(1)

print("Time's UP! Buddy....")