from tkinter import messagebox
from src.bank_system.models import Bank, Customer


def add_customer(bank: Bank, app):
    try:
        customer_id = int(app.customer_id_entry.get())
        name = app.customer_name_entry.get()
        address = app.customer_address_entry.get()
        phone = app.customer_phone_entry.get()

        if not all([name, address, phone]):
            messagebox.showerror("Error", "All fields are required")
            return

        customer = Customer(customer_id, name, address, phone)

        if bank.add_customer(customer):
            messagebox.showinfo("Success", "Customer added")
            app.update_status("Customer added")
        else:
            messagebox.showerror("Error", "Customer already exists")

    except ValueError:
        messagebox.showerror("Error", "Invalid ID")


def update_customer(bank: Bank, app):
    try:
        customer_id = int(app.customer_id_entry.get())

        if not bank.find_customer(customer_id):
            messagebox.showerror("Error", "Customer not found")
            return

        address = app.customer_address_entry.get()
        phone = app.customer_phone_entry.get()

        bank.update_customer(customer_id, address, phone)
        messagebox.showinfo("Success", "Customer updated")
        app.update_status("Customer updated")

    except ValueError:
        messagebox.showerror("Error", "Invalid ID")


def delete_customer(bank: Bank, app):
    try:
        customer_id = int(app.customer_id_entry.get())

        if bank.delete_customer(customer_id):
            messagebox.showinfo("Success", "Customer deleted")
            app.update_status("Customer deleted")
        else:
            messagebox.showerror("Error", "Customer not found")

    except ValueError:
        messagebox.showerror("Error", "Invalid ID")


def search_customer(bank: Bank, app):
    try:
        customer_id = int(app.customer_id_entry.get())
        customer = bank.search_customer(customer_id)

        if customer:
            app.customer_name_entry.delete(0, "end")
            app.customer_name_entry.insert(0, customer.customer_name)

            app.customer_address_entry.delete(0, "end")
            app.customer_address_entry.insert(0, customer.customer_address)

            app.customer_phone_entry.delete(0, "end")
            app.customer_phone_entry.insert(0, customer.customer_phone)

            app.update_status("Customer found")
        else:
            messagebox.showerror("Error", "Not found")

    except ValueError:
        messagebox.showerror("Error", "Invalid ID")


def open_account(bank: Bank, app):
    try:
        customer_id = int(app.account_customer_id_entry.get())
        account_number = int(app.account_number_entry.get())

        if bank.open_account(customer_id, account_number):
            messagebox.showinfo("Success", "Account opened")
            app.update_status("Account opened")
        else:
            messagebox.showerror("Error", "Failed to open account")

    except ValueError:
        messagebox.showerror("Error", "Invalid input")


def display_all_customers(bank: Bank, app):
    customers = bank.display_all_customers()

    app.customer_text.delete(1.0, "end")

    if not customers:
        app.customer_text.insert("end", "No customers\n")
    else:
        for c in customers.values():
            app.customer_text.insert("end", str(c) + "\n\n")

    app.update_status("Customer list refreshed")
