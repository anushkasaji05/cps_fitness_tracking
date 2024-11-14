import tkinter as tk
from tkinter import messagebox
from backend.csv_handler import insert_record, update_record, delete_record

# Function to add a record
def add_record():
    record = get_form_data()
    if not all(record.values()):
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if insert_record(record):
        messagebox.showinfo("Success", "Record added successfully!")
    else:
        messagebox.showerror("Error", "Failed to add record.")

# Function to update a record
def update_record_ui():
    record = get_form_data()
    if not all(record.values()):
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if update_record(record):
        messagebox.showinfo("Success", "Record updated successfully!")
    else:
        messagebox.showerror("Error", "Record not found for update.")

# Function to delete a record
def delete_record_ui():
    username = entry_username.get()
    date = entry_date.get()
    if not username or not date:
        messagebox.showerror("Error", "Username and Date are required to delete a record!")
        return
    if delete_record(username, date):
        messagebox.showinfo("Success", "Record deleted successfully!")
    else:
        messagebox.showerror("Error", "Record not found for deletion.")

# Function to get form data
def get_form_data():
    return {
        "username": entry_username.get(),
        "date": entry_date.get(),
        "weight": entry_weight.get(),
        "sleep": entry_sleep.get(),
        "water": entry_water.get(),
        "activity": entry_activity.get(),
        "workout_duration": entry_workout_duration.get()
    }

# Create the main application window
root = tk.Tk()
root.title("Health Tracker")

# Create labels and entry fields
labels = ["Username", "Date", "Weight", "Sleep", "Water", "Activity", "Workout Duration"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label.lower().replace(" ", "_")] = entry

# Assign specific entry variables for easier access
entry_username = entries["username"]
entry_date = entries["date"]
entry_weight = entries["weight"]
entry_sleep = entries["sleep"]
entry_water = entries["water"]
entry_activity = entries["activity"]
entry_workout_duration = entries["workout_duration"]

# Create buttons
tk.Button(root, text="Add", command=add_record).grid(row=len(labels), column=0, padx=10, pady=10)
tk.Button(root, text="Update", command=update_record_ui).grid(row=len(labels), column=1, padx=10, pady=10)
tk.Button(root, text="Delete", command=delete_record_ui).grid(row=len(labels)+1, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()