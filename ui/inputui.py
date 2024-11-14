from backend.csv_handler import insert_record, update_record, delete_record
import tkinter as tk
from tkinter import messagebox

# Function to add a record
def add_record_ui(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration):
    record = get_form_data(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration)
    if not all(record.values()):
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if insert_record(record):  # Assuming this function correctly handles inserting the record
        messagebox.showinfo("Success", "Record added successfully!")
    else:
        messagebox.showerror("Error", "Failed to add record.")

# Function to update a record
def update_record_ui(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration):
    record = get_form_data(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration)
    if not all(record.values()):
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if update_record(record):  # Assuming this function correctly handles updating the record
        messagebox.showinfo("Success", "Record updated successfully!")
    else:
        messagebox.showerror("Error", "Record not found for update.")

# Function to delete a record
def delete_record_ui(entry_username, entry_date):
    username = entry_username.get()
    date = entry_date.get()
    if not username or not date:
        messagebox.showerror("Error", "Username and Date are required to delete a record!")
        return
    if delete_record(username, date):  # Assuming this function correctly handles deleting the record
        messagebox.showinfo("Success", "Record deleted successfully!")
    else:
        messagebox.showerror("Error", "Record not found for deletion.")

# Function to get form data
def get_form_data(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration):
    return {
        "username": entry_username.get(),
        "date": entry_date.get(),
        "weight": entry_weight.get(),
        "sleep": entry_sleep.get(),
        "water": entry_water.get(),
        "activity": entry_activity.get(),
        "workout_duration": entry_workout_duration.get()
    }
