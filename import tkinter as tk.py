import tkinter as tk
from tkinter import messagebox

recorded_data = []

def display_info():
    try:
        revenue = float(entry_revenue.get())
        cost = float(entry_cost.get())
        profit = revenue - cost
        recorded_data.append((revenue, cost, profit))
        label_result.config(text=f"Profit: {profit:.2f}")
        update_display()
    except ValueError:
        label_result.config(text="Enter valid numerical values.")

def show_recorded_data():
    data_str = "\n".join([f"Revenue: {entry[0]}, Cost: {entry[1]}, Profit: {entry[2]:.2f}" for entry in recorded_data])
    messagebox.showinfo("Recorded Data", data_str or "No data recorded yet.")
    update_display()  # Update display after showing recorded data

def update_display():
    canvas.delete("all")
    update_bar_chart()

def update_bar_chart():
    if recorded_data:
        profit_list = [entry[2] for entry in recorded_data]
        max_profit = max(profit_list)

        for i, profit in enumerate(profit_list):
            bar_height = (profit / max_profit) * 150
            canvas.create_rectangle(i * 60 + 20, 180 - bar_height, (i + 1) * 60 + 20, 180, fill="blue")
            canvas.create_text((i + 0.5) * 60 + 20, 190, text=f"{profit:.2f}")

# Create the main window
window = tk.Tk()
window.title("Profit Calculator with Data Recording")

# Create entry and label widgets for revenue and costs
labels = ["Revenue:", "Costs:"]
entries = []

for label_text in labels:
    tk.Label(window, text=label_text).pack(pady=5)
    entry = tk.Entry(window)
    entry.pack(pady=5)
    entries.append(entry)

# Assign entry widgets to variables
entry_revenue, entry_cost = entries

# Create buttons to calculate profit, show recorded data, and update bar chart
tk.Button(window, text="Calculate Profit", command=display_info).pack(pady=10)
tk.Button(window, text="Show Recorded Data", command=show_recorded_data).pack(pady=10)

# Create a label for displaying the result
label_result = tk.Label(window, text="")
label_result.pack(pady=10)

# Create a canvas for the bar chart
canvas = tk.Canvas(window, width=400, height=200, bg="white")
canvas.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
