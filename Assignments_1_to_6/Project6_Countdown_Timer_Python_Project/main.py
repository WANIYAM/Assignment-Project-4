# You enter a time (in seconds or minutes), and it counts down to zero — then prints a message when the timer is done.

import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # overwrite the line
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

# Get user input
try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown(total_seconds)
except ValueError:
    print("Please enter a valid number!")

