# Name: Georgia Vrana
# Date Submitted: Thursday, May 9th, 2024
# Assignment-13: Countries of the World
# Description: This Python program features a GUI titled "Countries of the World" that 
#              allows users to import a list of countries from a file, export this list 
#              to a specified new file, and quit the application, all managed through 
#              three interactive buttons.

import tkinter as tk
from tkinter import filedialog, messagebox

def import_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, 'r') as file:
            global countries
            countries = file.readlines()
        messagebox.showinfo("Success", "Countries have been successfully imported!")

def print_countries():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, 'w') as file:
            for country in countries:
                file.write(country)
        messagebox.showinfo("Success", "Countries have been successfully exported!")

def quit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Countries of the World")
root.geometry('300x300')

# Initialize countries list
countries = []

# Create buttons
import_button = tk.Button(root, text="Import File", command=import_file, width=15)
import_button.pack(pady=10)

print_button = tk.Button(root, text="Print Countries", command=print_countries, width=15)
print_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_program, width=15)
quit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()