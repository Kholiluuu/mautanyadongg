import tkinter as tk
from tkinter import messagebox
import random

def on_no_hover(event):
    # Buat tombol "No" bergerak ke posisi acak saat kursor mendekat
    x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=x, y=y)

def on_yes_click():
    # Memunculkan pesan memaki
    messagebox.showerror("Response", "Dasar orang gila! Hahaha")

# Membuat jendela utama
root = tk.Tk()
root.title("Pertanyaan Serius")
root.geometry("400x300")

# Label pertanyaan
label = tk.Label(root, text="Are you gay/lesbian?", font=("Arial", 16))
label.pack(pady=20)

# Tombol Yes
yes_button = tk.Button(root, text="Yes", font=("Arial", 12), command=on_yes_click)
yes_button.pack(pady=10)

# Tombol No
no_button = tk.Button(root, text="No", font=("Arial", 12))
no_button.place(x=150, y=150)

# Menambahkan event hover pada tombol No
no_button.bind("<Enter>", on_no_hover)

# Menjalankan aplikasi
root.mainloop()
