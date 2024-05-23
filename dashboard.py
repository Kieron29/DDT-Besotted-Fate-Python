import tkinter as tk
from tkinter import messagebox

def exit_out():
    if messagebox.askokcancel("Exit", "Exit now?"):
        dashboard_root.destroy()

dashboard_root = tk.Tk()
dashboard_root.title("Dashboard")

dashboard_root.attributes("-fullscreen", True)

dashboard_label = tk.Label(dashboard_root, text="Scene 1", font=("MS Gothic", 50))
dashboard_label.pack(pady=20)

exit_button = tk.Button(dashboard_root, text="Exit", command=exit_out, width=20, height=5, font=("MS Gothic", 15))
exit_button.pack(pady=10)

dashboard_root.mainloop()

