import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

# Encryption function (handles overflow properly)
def encrypt_image(img_array, key=100):
    return np.mod(img_array.astype(np.int16) + key, 256).astype(np.uint8)

# Decryption function
def decrypt_image(img_array, key=100):
    return np.mod(img_array.astype(np.int16) - key, 256).astype(np.uint8)

# Load image from file
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    global original_img, img_array
    original_img = cv2.imread(file_path)
    img_array = original_img.copy()
    show_image(img_array)

# Encrypt the image and display it
def encrypt_and_show():
    global img_array
    if img_array is None:
        messagebox.showerror("Error", "No image loaded")
        return
    img_array = encrypt_image(img_array, key=127)
    show_image(img_array)

# Decrypt the image and display it
def decrypt_and_show():
    global img_array
    if img_array is None:
        messagebox.showerror("Error", "No image loaded")
        return
    img_array = decrypt_image(img_array, key=127)
    show_image(img_array)

# Display the image after resizing
def show_image(array):
    img_rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)

    # Resize to max 400x300 to fit UI nicely
    max_size = (400, 300)
    img_pil.thumbnail(max_size)

    img_tk = ImageTk.PhotoImage(img_pil)

    image_display.configure(image=img_tk)
    image_display.image = img_tk

# Tkinter window setup
root = tk.Tk()
root.title("🔐 Image Encryption Tool")
root.geometry("700x500")
root.configure(bg="#10162F")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12), padding=6)
style.configure("TLabel", background="#10162F", foreground="white", font=("Segoe UI", 11))

# UI layout
ttk.Label(root, text="Pixel Manipulation Based Image Encryptor", font=("Segoe UI", 14, "bold")).pack(pady=10)

ttk.Button(root, text="📁 Load Image", command=load_image).pack(pady=5)
ttk.Button(root, text="🔒 Encrypt Image", command=encrypt_and_show).pack(pady=5)
ttk.Button(root, text="🔓 Decrypt Image", command=decrypt_and_show).pack(pady=5)

# Image display area
image_display = ttk.Label(root)
image_display.pack(pady=10)

# Global image storage
img_array = None
original_img = None

# Start the app
root.mainloop()
