import os
import tkinter as tk
from tkinter import filedialog, messagebox

class ExtensionCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Line Counter")

        self.extension = tk.StringVar(value=".R")

        self.label_extension = tk.Label(root, text="Enter file extension (e.g., .R, .py):")
        self.label_extension.grid(row=0, column=0, padx=5, pady=5)
        self.entry_extension = tk.Entry(root, textvariable=self.extension)
        self.entry_extension.grid(row=0, column=1, padx=5, pady=5)

        self.button_select_folder = tk.Button(root, text="Select Folder and Count Lines", command=self.select_folder_and_count_lines)
        self.button_select_folder.grid(row=1, columnspan=2, padx=5, pady=5)

    def count_lines(self, directory, extension):
        total_lines = 0
        matching_files = []

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    matching_files.append(os.path.join(root, file))

        for matching_file in matching_files:
            with open(matching_file, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                total_lines += len(lines)

        return total_lines

    def select_folder_and_count_lines(self):
        folder = filedialog.askdirectory(title="Select Folder Containing Files")
        if folder:
            extension = self.entry_extension.get().strip()
            if not extension.startswith('.'):
                extension = '.' + extension
            total_lines = self.count_lines(folder, extension)
            messagebox.showinfo("Total Lines", f"Total lines in all {extension} files: {total_lines}")
        else:
            messagebox.showinfo("Folder Selection", "No folder selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExtensionCounterApp(root)
    root.mainloop()
