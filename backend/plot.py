import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


def sleep():
    days = np.arange(1, 10)
    hours = np.arange(1, 10)
    plt.figure(figsize=(10, 10))
    plt.bar(days, hours)
    plt.xlabel("Days")
    plt.ylabel("Sleep (in hours)")
    plt.savefig("sleep.jpg")


def water_intake():
    days = np.arange(1, 10)
    glasses = np.arange(1, 10)
    plt.figure(figsize=(10, 10))
    plt.bar(days, glasses)
    plt.xlabel("Days")
    plt.ylabel("Water Intake (in number of glasses)")
    plt.savefig("water.jpg")


def workout_duration():
    days = np.arange(1, 10)
    duration = np.arange(1, 10)
    plt.figure(figsize=(10, 10))
    plt.bar(days, duration)
    plt.xlabel("Days")
    plt.ylabel("Workout Duration (in hours)")
    plt.savefig("duration.jpg")


sleep()
water_intake()
workout_duration()
