import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup
def initialize_db():
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            blood_group TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add donor to database
def add_donor(name, age, blood_group, contact):
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, age, blood_group, contact) VALUES (?, ?, ?, ?)",
                   (name, age, blood_group, contact))
    conn.commit()
    conn.close()

# Search donors by blood group
def search_donors(blood_group):
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors WHERE blood_group = ?", (blood_group,))
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch all donors
def fetch_all_donors():
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    results = cursor.fetchall()
    conn.close()
    return results

# Main app
class BloodBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Bank Management System")
        self.root.geometry("600x400")

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.blood_group_var = tk.StringVar()
        self.contact_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Add Donor Section
        tk.Label(self.root, text="Add Donor", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Name").pack()
        tk.Entry(self.root, textvariable=self.name_var).pack()
        tk.Label(self.root, text="Age").pack()
        tk.Entry(self.root, textvariable=self.age_var).pack()
        tk.Label(self.root, text="Blood Group").pack()
        tk.Entry(self.root, textvariable=self.blood_group_var).pack()
        tk.Label(self.root, text="Contact").pack()
        tk.Entry(self.root, textvariable=self.contact_var).pack()
        tk.Button(self.root, text="Add Donor", command=self.add_donor).pack(pady=10)

        # Search Section
        tk.Label(self.root, text="Search Donors by Blood Group", font=("Arial", 14)).pack(pady=10)
        self.search_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.search_var).pack()
        tk.Button(self.root, text="Search", command=self.search_donors).pack(pady=10)

        # Donors List
        tk.Label(self.root, text="Donor List", font=("Arial", 14)).pack(pady=10)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Blood Group", "Contact"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Blood Group", text="Blood Group")
        self.tree.heading("Contact", text="Contact")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_donors()

    def add_donor(self):
        name = self.name_var.get()
        age = self.age_var.get()
        blood_group = self.blood_group_var.get()
        contact = self.contact_var.get()

        if name and age and blood_group and contact:
            add_donor(name, int(age), blood_group, contact)
            messagebox.showinfo("Success", "Donor added successfully!")
            self.load_donors()
            self.clear_inputs()
        else:
            messagebox.showwarning("Error", "All fields are required!")

    def search_donors(self):
        blood_group = self.search_var.get()
        if blood_group:
            donors = search_donors(blood_group)
            self.update_tree(donors)
        else:
            messagebox.showwarning("Error", "Please enter a blood group!")

    def load_donors(self):
        donors = fetch_all_donors()
        self.update_tree(donors)

    def update_tree(self, donors):
        self.tree.delete(*self.tree.get_children())
        for donor in donors:
            self.tree.insert("", tk.END, values=donor)

    def clear_inputs(self):
        self.name_var.set("")
        self.age_var.set("")
        self.blood_group_var.set("")
        self.contact_var.set("")

# Run the app
if __name__ == "__main__":
    initialize_db()
    root = tk.Tk()
    app = BloodBankApp(root)
    root.mainloop()
