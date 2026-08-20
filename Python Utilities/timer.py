import time

while True:
    alarm = int(input("Enter the time in seconds: "))
    try:
        if(alarm < 0):
            print(f"Time cannot be negative")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for remaining in range(alarm, -1, -1):
    mins, secs = divmod(remaining, 60)
    time_left = f"{mins:02}:{secs:02}"
    print(time_left, end="\r")
    time.sleep(1)

print("Time's up!")