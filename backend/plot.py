import matplotlib.pyplot as plt
from backend.csv_handler import read_data

plt.style.use('fivethirtyeight')

# Function to plot sleep duration for a specific user and save the plot as an image
def plot_sleep_duration(username, days, duration):
    data = read_data()

    for i in range(len(data)):
        if (data[i][0] == username):
            days.append(data[i][1])
            duration.append(float(data[i][3]))

    plt.figure(figsize=(10, 10))
    plt.bar(days, duration)
    plt.xlabel("Days")
    plt.ylabel("Sleep Duration (in hours)")
    plt.title(f"Sleep Duration for {username}")
    plt.savefig("output/sleep.jpg")
    plt.close()

# Function to plot water intake for a specific user and save the plot as an image
def plot_water_intake(username, days, glasses):
    data = read_data()

    for i in range(len(data)):
        if (data[i][0] == username):
            days.append(data[i][1])
            glasses.append(float(data[i][4]))

    plt.figure(figsize=(10, 10))
    plt.bar(days, glasses)
    plt.xlabel("Days")
    plt.ylabel("Water Intake (in litres)")
    plt.title(f"Water Intake for {username}")
    plt.savefig("output/water.jpg")
    plt.close()

# Function to plot workout duration for a specific user and save the plot as an image
def plot_workout_duration(username, days, duration):
    data = read_data()

    for i in range(len(data)):
        if (data[i][0] == username):
            days.append(data[i][1])
            duration.append(float(data[i][6]))

    plt.figure(figsize=(10, 10))
    plt.bar(days, duration)
    plt.xlabel("Days")
    plt.ylabel("Workout Duration (in hours)")
    plt.title(f"Workout Duration for {username}")
    plt.savefig("output/workout.jpg")
    plt.close()

