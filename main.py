import tkinter as tk
from tkinter import messagebox
from backend.csv_handler import read_data
from backend.plot import plot_sleep_duration, plot_water_intake, plot_workout_duration
from ui.inputui import add_record_ui, update_record_ui, delete_record_ui
from ui.outputui import display_results

# Create Main Window
root = tk.Tk()
root.title("Health Tracker")
root.geometry("600x400")
root.configure(bg="#f7f7f7")  # Light neutral background

# Fonts
LABEL_FONT = ("Helvetica", 12, "bold")
BUTTON_FONT = ("Helvetica", 10)

# Functions for Buttons
def open_input_ui():
    input_window = tk.Toplevel(root)
    input_window.title("Manage Records")
    input_window.geometry("400x300")
    input_window.configure(bg="#2c3e50")  # Dark background for better contrast
    labels = ["Username", "Date", "Weight", "Sleep", "Water", "Activity", "Workout Duration"]
    entries = {}

    # Create Entry Fields and Labels
    for i, label in enumerate(labels):
        tk.Label(input_window, text=label, font=LABEL_FONT, bg="#2c3e50", fg="white").grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(input_window, font=LABEL_FONT, bg="#34495e", fg="white")
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label.lower().replace(" ", "_")] = entry

    entry_username = entries["username"]
    entry_date = entries["date"]
    entry_weight = entries["weight"]
    entry_sleep = entries["sleep"]
    entry_water = entries["water"]
    entry_activity = entries["activity"]
    entry_workout_duration = entries["workout_duration"]

    # Create Buttons with updated, more readable colors
    tk.Button(input_window, text="Add", command=lambda: add_record_ui(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration), font=BUTTON_FONT, bg="#16a085", fg="black").grid(row=len(labels), column=0, padx=10, pady=10)
    tk.Button(input_window, text="Update", command=lambda: update_record_ui(entry_username, entry_date, entry_weight, entry_sleep, entry_water, entry_activity, entry_workout_duration), font=BUTTON_FONT, bg="#27ae60", fg="black").grid(row=len(labels), column=1, padx=10, pady=10)
    tk.Button(input_window, text="Delete", command=lambda: delete_record_ui(entry_username, entry_date), font=BUTTON_FONT, bg="#e74c3c", fg="black").grid(row=len(labels)+1, column=0, columnspan=2, padx=10, pady=10)



def open_output_ui():
    output_window = tk.Toplevel(root)
    output_window.title("Activity Analysis")
    output_window.geometry("400x300")
    output_window.configure(bg="#2c3e50")  # Dark background for better contrast

    tk.Label(output_window, text="Enter Username:", font=("Helvetica", 12, "bold"), bg="#2c3e50", fg="white").pack(pady=10)
    username_entry = tk.Entry(output_window, font=("Helvetica", 12), bg="#34495e", fg="white")
    username_entry.pack(pady=5)

    tk.Label(output_window, text="Enter Activity (Cycling, Walking, Running, Swimming):", font=("Helvetica", 12, "bold"), bg="#2c3e50", fg="white").pack(pady=10)
    activity_entry = tk.Entry(output_window, font=("Helvetica", 12), bg="#34495e", fg="white")
    activity_entry.pack(pady=5)

    # Result label to display the output
    result_label = tk.Label(output_window, text="", font=("Helvetica", 14), fg="lightgreen", bg="#2c3e50")
    result_label.pack(pady=10)

    # Button to start the calculation
    tk.Button(output_window, text="Start", command=lambda: display_results(username_entry, activity_entry, result_label), font=("Helvetica", 12, "bold"), bg="#e67e22", fg="white").pack(pady=10)

def generate_plots_ui():
    def generate():
        username = username_entry.get()
        if not username:
            messagebox.showerror("Error", "Username is required!")
            return

        plot_sleep_duration(username, days=[], duration=[])
        plot_water_intake(username, days=[], glasses=[])
        plot_workout_duration(username, days=[], duration=[])

        messagebox.showinfo("Success", "Plots saved in the 'output' folder.")

    plot_window = tk.Toplevel(root)
    plot_window.title("Generate Plots")
    plot_window.geometry("400x200")
    plot_window.configure(bg="#f7f7f7")  # Match main window background

    tk.Label(plot_window, text="Enter Username:", font=LABEL_FONT, bg="#f7f7f7").pack(pady=5)
    username_entry = tk.Entry(plot_window, font=LABEL_FONT)
    username_entry.pack(pady=5)

    tk.Button(plot_window, text="Generate Plots", command=generate, font=BUTTON_FONT, bg="#fff3cd", fg="black").pack(pady=10)


# Main Menu Buttons
tk.Label(root, text="Health Tracker", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=20)

tk.Button(root, text="Manage Records", command=open_input_ui, font=BUTTON_FONT, bg="#d1e7dd", fg="black").pack(pady=10)
tk.Button(root, text="Activity Analysis", command=open_output_ui, font=BUTTON_FONT, bg="#d9f7f5", fg="black").pack(pady=10)
tk.Button(root, text="Generate Plots", command=generate_plots_ui, font=BUTTON_FONT, bg="#fff3cd", fg="black").pack(pady=10)
tk.Button(root, text="Exit", command=root.destroy, font=BUTTON_FONT, bg="#f8d7da", fg="black").pack(pady=20)

# Run Main Window
root.mainloop()
