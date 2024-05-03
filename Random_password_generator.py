import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.config(bg="#333")  # Set dark background color
        
        # Title
        self.title_label = tk.Label(master, text="Random Password Generator", font=("Arial", 16), bg="#333", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Password Length
        self.label_length = tk.Label(master, text="Password Length:", bg="#333", fg="white")
        self.label_length.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.entry_length = tk.Entry(master, width=10)
        self.entry_length.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Password Complexity
        self.label_complexity = tk.Label(master, text="Password Complexity:", bg="#333", fg="white")
        self.label_complexity.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        # Generated Password
        self.label_password = tk.Label(master, text="Generated Password:", bg="#333", fg="white")
        self.label_password.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.password_var = tk.StringVar()
        self.entry_password = tk.Entry(master, textvariable=self.password_var, width=30)
        self.entry_password.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        # Buttons
        self.button_generate = tk.Button(master, text="Generate Password", command=self.generate_password, bg="#4caf50", fg="white")
        self.button_generate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.button_copy = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#2196f3", fg="white")
        self.button_copy.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        
    def generate_password(self):
        password_length = int(self.entry_length.get())
        complexity = self.complexity_var.get()
        
        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
        
        generated_password = ''.join(random.choice(characters) for i in range(password_length))
        self.password_var.set(generated_password)
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        self.entry_password.focus_set()
        self.entry_password.selection_range(0, tk.END)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
