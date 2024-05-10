import os
import tkinter as tk
from tkinter import filedialog, messagebox

def compare_folders():
    folder1_path = entry_folder1.get()
    folder2_path = entry_folder2.get()

    if not folder1_path or not folder2_path:
        messagebox.showerror("Error", "Mohon isi kedua lokasi folder.")
        return

    if not os.path.exists(folder1_path) or not os.path.exists(folder2_path):
        messagebox.showerror("Error", "Salah satu atau kedua folder tidak ditemukan.")
        return

    folder1_files = set(os.listdir(folder1_path))
    folder2_files = set(os.listdir(folder2_path))

    unique_folder1_files = folder1_files - folder2_files
    unique_folder2_files = folder2_files - folder1_files

    messagebox.showinfo("Hasil Perbandingan", 
        f"File unik di Folder 1: {', '.join(unique_folder1_files)}\n"
        f"File unik di Folder 2: {', '.join(unique_folder2_files)}")

def browse_folder1():
    folder1_path = filedialog.askdirectory()
    entry_folder1.delete(0, tk.END)
    entry_folder1.insert(0, folder1_path)

def browse_folder2():
    folder2_path = filedialog.askdirectory()
    entry_folder2.delete(0, tk.END)
    entry_folder2.insert(0, folder2_path)

# Membuat GUI
root = tk.Tk()
root.title("Perbandingan Folder by Haris Lukman Hakim")

label_folder1 = tk.Label(root, text="Folder 1:")
label_folder1.grid(row=0, column=0, padx=5, pady=5)

entry_folder1 = tk.Entry(root, width=50)
entry_folder1.grid(row=0, column=1, padx=5, pady=5)

button_browse1 = tk.Button(root, text="Browse", command=browse_folder1)
button_browse1.grid(row=0, column=2, padx=5, pady=5)

label_folder2 = tk.Label(root, text="Folder 2:")
label_folder2.grid(row=1, column=0, padx=5, pady=5)

entry_folder2 = tk.Entry(root, width=50)
entry_folder2.grid(row=1, column=1, padx=5, pady=5)

button_browse2 = tk.Button(root, text="Browse", command=browse_folder2)
button_browse2.grid(row=1, column=2, padx=5, pady=5)

button_compare = tk.Button(root, text="Bandingkan Folder", command=compare_folders)
button_compare.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
