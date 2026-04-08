import tkinter as tk
from tkinter import ttk, messagebox
from src.bank_system.db import (
    init_db,
    insert_customer,
    get_all_customers,
    delete_customer,
    update_customer,
    search_customer
)


class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank System")

        init_db()

        # Inputs
        tk.Label(root, text="ID").grid(row=0, column=0)
        tk.Label(root, text="Name").grid(row=1, column=0)
        tk.Label(root, text="Address").grid(row=2, column=0)
        tk.Label(root, text="Phone").grid(row=3, column=0)

        self.id_entry = tk.Entry(root)
        self.name_entry = tk.Entry(root)
        self.address_entry = tk.Entry(root)
        self.phone_entry = tk.Entry(root)

        self.id_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.phone_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Add", command=self.add).grid(row=4, column=0)
        tk.Button(root, text="Update", command=self.update).grid(row=4, column=1)
        tk.Button(root, text="Delete", command=self.delete).grid(row=5, column=0)
        tk.Button(root, text="Search", command=self.search).grid(row=5, column=1)
        tk.Button(root, text="Refresh", command=self.refresh).grid(row=6, column=0, columnspan=2)

        # Table
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Address", "Phone"), show="headings")

        for col in ("ID", "Name", "Address", "Phone"):
            self.tree.heading(col, text=col)

        self.tree.grid(row=7, column=0, columnspan=2)

        self.tree.bind("<ButtonRelease-1>", self.select_row)

        self.refresh()

    def get_input(self):
        try:
            cid = int(self.id_entry.get())
        except:
            messagebox.showerror("Error", "Invalid ID")
            return None

        return (
            cid,
            self.name_entry.get(),
            self.address_entry.get(),
            self.phone_entry.get()
        )

    def add(self):
        data = self.get_input()
        if not data:
            return

        cid, name, address, phone = data

        if insert_customer(cid, name, address, phone):
            self.refresh()
        else:
            messagebox.showerror("Error", "ID already exists")

    def update(self):
        data = self.get_input()
        if not data:
            return

        cid, name, address, phone = data
        update_customer(cid, name, address, phone)
        self.refresh()

    def delete(self):
        try:
            cid = int(self.id_entry.get())
        except:
            messagebox.showerror("Error", "Invalid ID")
            return

        delete_customer(cid)
        self.refresh()

    def search(self):
        try:
            cid = int(self.id_entry.get())
        except:
            messagebox.showerror("Error", "Invalid ID")
            return

        row = search_customer(cid)

        if row:
            self.populate_fields(row)
        else:
            messagebox.showerror("Error", "Not found")

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in get_all_customers():
            self.tree.insert("", tk.END, values=row)

    def select_row(self, event):
        selected = self.tree.focus()
        values = self.tree.item(selected, "values")

        if values:
            self.populate_fields(values)

    def populate_fields(self, values):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

        self.id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.address_entry.insert(0, values[2])
        self.phone_entry.insert(0, values[3])
