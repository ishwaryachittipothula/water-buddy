#water buddy
#created by ishwarya
#python+ tkinter
import tkinter as tk

root = tk.Tk()
root.title("Water Buddy")
root.geometry("350x250")
root.attributes("-topmost", True)

emoji = tk.Label(
    root,
    text="🐧",
    font=("Arial", 40)
)
emoji.pack(pady=10)

label = tk.Label(
    root,
    text="🥤 Drink Water, Aishu!",
    font=("Arial", 16)
)
label.pack(pady=10)

def done():
    root.destroy()

def remind_later():
    label.config(text="⏰ Reminding in 5 seconds...")
    root.after(5000, show_reminder)

def show_reminder():
    label.config(text="🥤 Hey Aishu! Drink Water!")

ok_button = tk.Button(
    root,
    text="OK",
    command=done
)
ok_button.pack(pady=5)

remind_button = tk.Button(
    root,
    text="Remind Me Later",
    command=remind_later
)
remind_button.pack(pady=5)

root.mainloop()
