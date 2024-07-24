#1. The Range Riddle
#Task 1: Your Mood Today
import random

emotions = ["happy", "mad", "sad", "bored", "scared", "energetic", "calm", "annoyed"]
weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(weekday)

for i in range(len(weekday)):
  print("On " + weekday[i] + ", you were feeling " + random.choice(emotions))

#2. Double Scoop with Nested Loops
#Task 1: Your Mood Tracker
import random

emotions = ["happy", "mad", "sad", "bored", "scared", "energetic", "calm", "annoyed"]
weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "night"]
print(weekday)

for day in range(len(weekday)):
  for i in time_of_day:
    print("On " + weekday[i] + " " + time_of_day[i] + ", you were feeling " + random.choice(emotions))
