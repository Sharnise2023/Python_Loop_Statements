# Task 1:
import random

# List of moods
moods = ["Happy", "Sad", "Energectic", "Calm", "Excited", "Relaxed", "Anxious"]

# List of days of the week
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of different times of the day
times_of_day = ["Morning", "Afternoon", "Evening"]

# out Loop for each day of the week
for day in days_of_the_week:
    print(f"{day}:")
    # in loop for each time of the day
    for time in times_of_day:
        mood = random.choice(moods)
        print(f" {time}: {mood}")
    print() 


