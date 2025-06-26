import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Caesar Cipher Function
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Encrypt/Decrypt Action
def encrypt_decrypt():
    output_text.delete("1.0", tk.END)
    try:
        text = input_text.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        mode = mode_var.get()

        if not text:
            messagebox.showwarning("Input Error", "Please enter a message.")
            return

        result = caesar_cipher(text, shift, mode)
        output_text.insert("end", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Hover Effects
def on_enter(event=None):
    encrypt_button.configure(bg="#00c853")

def on_leave(event=None):
    encrypt_button.configure(bg="#00e676")

# === GUI ===
root = tk.Tk()
root.title("🚀 Caesar Cipher – Futuristic Edition")
root.configure(background="#1e1e2f")
root.geometry("600x500")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1e1e2f", foreground="#ffffff", font=("Consolas", 12))
style.configure("TEntry", font=("Consolas", 12))
style.configure("TCombobox", font=("Consolas", 12))
style.configure("TFrame", background="#1e1e2f")

# Main Frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# Header
header = tk.Label(main_frame, text="🛡️ Caesar Cipher Encoder/Decoder", font=("Orbitron", 18, "bold"),
                  fg="#00e676", bg="#1e1e2f")
header.pack(pady=(0, 20))

# Input Message
ttk.Label(main_frame, text="🔤 Message:").pack(anchor="w")
input_text = tk.Text(main_frame, height=5, width=60, bg="#2e2e3e", fg="#ffffff", insertbackground="white",
                     font=("Consolas", 12), bd=0, relief="flat")
input_text.pack(pady=5)

# Shift
ttk.Label(main_frame, text="🔢 Shift Value:").pack(anchor="w", pady=(10, 0))
shift_entry = ttk.Entry(main_frame, width=10)
shift_entry.pack(pady=5, anchor="w")

# Mode
ttk.Label(main_frame, text="⚙️ Mode:").pack(anchor="w", pady=(10, 0))
mode_var = tk.StringVar(value="encrypt")
mode_combobox = ttk.Combobox(main_frame, textvariable=mode_var,
                              values=["encrypt", "decrypt"], width=15, state="readonly")
mode_combobox.pack(anchor="w", pady=5)

# Encrypt/Decrypt Button
encrypt_button = tk.Button(main_frame, text="🚀 Run Cipher", command=encrypt_decrypt,
                           bg="#00e676", fg="#000000", font=("Orbitron", 12, "bold"),
                           activebackground="#00c853", activeforeground="#ffffff", bd=0, relief="flat",
                           padx=20, pady=10)
encrypt_button.pack(pady=20)
encrypt_button.bind("<Enter>", on_enter)
encrypt_button.bind("<Leave>", on_leave)

# Output
ttk.Label(main_frame, text="📄 Result:").pack(anchor="w")
output_text = tk.Text(main_frame, height=5, width=60, bg="#2e2e3e", fg="#00e676", insertbackground="white",
                      font=("Consolas", 12), bd=0, relief="flat")
output_text.pack(pady=5)

root.mainloop()
