import tkinter as tk
from tkinter import ttk
import string

# Function to assess password strength
def assess_password():
    password = entry.get()
    lower = upper = digit = special = 0
    feedback = []

    for char in password:
        if char in string.ascii_lowercase:
            lower += 1
        elif char in string.ascii_uppercase:
            upper += 1
        elif char in string.digits:
            digit += 1
        elif char in string.punctuation:
            special += 1

    length = len(password)
    score = 0

    if lower: score += 1
    else: feedback.append("➤ Add lowercase letters")

    if upper: score += 1
    else: feedback.append("➤ Add uppercase letters")

    if digit: score += 1
    else: feedback.append("➤ Add numbers")

    if special: score += 1
    else: feedback.append("➤ Add special characters")

    if length >= 8: score += 1
    else: feedback.append("➤ Use at least 8 characters")

    if score <= 2:
        result.set("🟥 Weak Password")
        result_label.config(foreground="#ff4d4d")
    elif score == 3 or score == 4:
        result.set("🟧 Moderate Password")
        result_label.config(foreground="#ffaa00")
    else:
        result.set("🟩 Strong Password")
        result_label.config(foreground="#33cc33")

    if feedback:
        feedback_text.set("\n".join(feedback))
    else:
        feedback_text.set("✔ Great job! Your password is strong.")

# App window
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("500x350")
root.configure(bg="#10162F")

# Style configuration
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#10162F",
                foreground="white",
                font=("Helvetica Neue", 12))

style.configure("TEntry",
                font=("Segoe UI", 12),
                fieldbackground="#ffffff",
                padding=5)

style.configure("TButton",
                font=("Segoe UI Semibold", 12),
                background="#444",
                foreground="#fff",
                padding=6)

# UI Layout
ttk.Label(root, text="🔐 Enter Your Password:", font=("Segoe UI", 13, "bold")).pack(pady=(30, 10))

entry = ttk.Entry(root, show='*', width=35)
entry.pack(pady=(0, 10))

ttk.Button(root, text="Check Strength", command=assess_password).pack(pady=10)

result = tk.StringVar()
result_label = ttk.Label(root, textvariable=result, font=("Helvetica Neue", 14, "bold"))
result_label.pack(pady=5)

feedback_text = tk.StringVar()
feedback_label = ttk.Label(root, textvariable=feedback_text, wraplength=440, justify="left", font=("Segoe UI", 10))
feedback_label.pack(pady=10)

# Run
root.mainloop()
