"""
Author: Rohit Kumar
Assignment: #1
"""


gym_member = "Alex Alliton"  
preferred_weight_kg = 20.5  
highest_reps = 25  
membership_active = True  
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 45),
    "Jordan": (60, 30, 40)
}

# Step c: Create a dictionary named workout_stats
for friend, minutes in workout_stats.copy().items():
    total_minutes = sum(minutes)
    workout_stats[friend + "_Total"] = total_minutes


# Step d: Calculate total workout minutes using a loop and add to dictionary
workout_list = []

for friend, minutes in workout_stats.items():
    if not friend.endswith("_Total"):
        workout_list.append(list(minutes))

print("Workout List:")
print(workout_list)


# Step e: Create a 2D nested list called workout_list
yoga_running = [row[0:2] for row in workout_list]
print("\nYoga and Running minutes for all friends:")
print(yoga_running)

# Step g: Check if any friend's total >= 120
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("\nWeightlifting minutes for last two friends:")
print(weightlifting_last_two)


# Highest and Lowest totals
print("\nFriends with total workout >= 120 minutes:")

for friend, total in workout_stats.items():
    if friend.endswith("_Total") and total >= 120:
        name = friend.replace("_Total", "")
        print(f"Great job staying active, {name}!")


# Step h: User input to look up a friend
user_name = input("\nEnter a friend's name: ")

if user_name in workout_stats:
    minutes = workout_stats[user_name]
    total = workout_stats.get(user_name + "_Total", sum(minutes))

    print(f"\nWorkout stats for {user_name}:")
    print(f"Yoga: {minutes[0]} minutes")
    print(f"Running: {minutes[1]} minutes")
    print(f"Weightlifting: {minutes[2]} minutes")
    print(f"Total: {total} minutes")

else:
    print(f"Friend {user_name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes

totals_only = {
    friend.replace("_Total", ""): total
    for friend, total in workout_stats.items()
    if friend.endswith("_Total")
}

highest_friend = max(totals_only, key=totals_only.get)
lowest_friend = min(totals_only, key=totals_only.get)

print("\nSummary:")

print(
    f"Friend with highest total workout minutes: "
    f"{highest_friend} ({totals_only[highest_friend]} minutes)"
)

print(
    f"Friend with lowest total workout minutes: "
    f"{lowest_friend} ({totals_only[lowest_friend]} minutes)"
)
