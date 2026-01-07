import tkinter as tk

# Create main window
root = tk.Tk()
root.title("MY Space")
root.geometry("900x600")

# ===== Calendar Section (Top) =====
calendar_frame = tk.Frame(root, height=100, bg="#e6e6e6")
calendar_frame.pack(fill="x")

calendar_label = tk.Label(
    calendar_frame,
    text="Calendar (will be added here)",
    font=("Arial", 14),
    bg="#e6e6e6"
)
calendar_label.pack(pady=20)

# ===== Main Content Section =====
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both")

# Diary Section (Left)
diary_frame = tk.Frame(main_frame, bg="#f9f9f9")
diary_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

diary_label = tk.Label(
    diary_frame,
    text="Diary Entry",
    font=("Arial", 14),
    bg="#f9f9f9"
)
diary_label.pack(anchor="w")

diary_text = tk.Text(diary_frame, height=20)
diary_text.pack(expand=True, fill="both")

# Task Tracker Section (Right)
task_frame = tk.Frame(main_frame, width=250, bg="#f0f0f0")
task_frame.pack(side="right", fill="y", padx=10, pady=10)

task_label = tk.Label(
    task_frame,
    text="Task Tracker",
    font=("Arial", 14),
    bg="#f0f0f0"
)
task_label.pack(pady=5)

task_list = tk.Listbox(task_frame)
task_list.pack(expand=True, fill="both", padx=5, pady=5)

# Run app
root.mainloop()
