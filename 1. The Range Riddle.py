# Task 1:
import random

# List of moods
moods = ["Happy", "Sad", "Energectic", "Calm", "Excited", "Relaxed", "Anxious"]

# List of days of the week
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

random.shuffle(moods)
for i in range(len(days_of_the_week)):
    print(f"{days_of_the_week[i]}: {moods[i]}")
