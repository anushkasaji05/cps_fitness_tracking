import tkinter as tk
from backend.csv_handler import read_activity
from datetime import datetime
import pandas as pd

# Constants for calorie calculation based on the formulas provided
CALORIES_CYCLING = 0.4
CALORIES_WALKING = 0.68
CALORIES_RUNNING = 1.01
CALORIES_SWIMMING = 0.09375

# Assumed speeds (in km/h) and laps per hour
SPEED_CYCLING = 20
SPEED_WALKING = 5.6
SPEED_RUNNING = 10.8
LAPS_SWIMMING = 20  # Laps / hour

def calculate_calories(activity, weights, durations):
    total_calories = 0
    
    for weight, duration_minutes in zip(weights, durations):
        duration_hours = duration_minutes / 60  # Convert minutes to hours
        
        if activity == "Cycling":
            distance = duration_hours * SPEED_CYCLING
            calories = CALORIES_CYCLING * weight * distance
        elif activity == "Walking":
            distance = duration_hours * SPEED_WALKING
            calories = CALORIES_WALKING * weight * distance
        elif activity == "Running":
            distance = duration_hours * SPEED_RUNNING
            calories = CALORIES_RUNNING * weight * distance
        elif activity == "Swimming":
            laps = duration_hours * LAPS_SWIMMING
            calories = CALORIES_SWIMMING * weight * laps
        else:
            calories = 0

        total_calories += calories

    return round(total_calories, 2)

# Function to display the results
def display_results(username_entry, activity_entry, result_label):
    username = username_entry.get()
    activity = activity_entry.get()

    # Fetch data using read_activity
    activity_data = read_activity(username, activity)
    if not activity_data or not activity_data[0]:
        result_label.config(text="No data found for this user and activity.", fg="red")
        return

    # Calculate total calories burned
    total_calories = calculate_calories(activity, activity_data[0], activity_data[1])

    # Display the result
    result_label.config(text=f"Total Calories burned for {activity}: {total_calories} calories", fg="lightgreen")
