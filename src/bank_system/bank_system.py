import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Optional


class Bank:
    def __init__(self, bank_id: int, bank_name: str, bank_location: str):
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.bank_location = bank_location
        self.customers: Dict[int, 'Customer'] = {}

    def add_customer(self, customer: 'Customer') -> bool:
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            return True
        return False

    def find_customer(self, customer_id: int) -> bool:
        return customer_id in self.customers

    def update_customer(self, customer_id: int, new_address: str, new_phone: str) -> bool:
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            customer.customer_address = new_address
            customer.customer_phone = new_phone
            return True
        return False

    def delete_customer(self, customer_id: int) -> bool:
        if customer_id in self.customers:
            del self.customers[customer_id]
            return True
        return False

    def search_customer(self, customer_id: int) -> Optional['Customer']:
        return self.customers.get(customer_id)

    def open_account(self, customer_id: int, account_number: int) -> bool:
        if customer_id not in self.customers:
            return False
        
        customer = self.customers[customer_id]
        if account_number in customer.accounts:
            return False
        
        customer.accounts[account_number] = 0.0  # Initial balance
        return True

    def display_all_customers(self) -> Dict[int, 'Customer']:
        return self.customers


class Customer:
    def __init__(self, customer_id: int, customer_name: str, 
                 customer_address: str, customer_phone: str):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.accounts: Dict[int, float] = {}  # account_number: balance

    def __str__(self) -> str:
        return (f"ID: {self.customer_id}, Name: {self.customer_name}\n"
                f"Address: {self.customer_address}, Phone: {self.customer_phone}\n"
                f"Accounts: {', '.join(map(str, self.accounts.keys()))}")


class BankApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("800x600")
        
        # Create bank instance (inherited from Bank)
        self.bank = Bank(1, "X Bank", "Prague")
        
        # Setup styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        
        # Create main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        self.header = ttk.Label(
            self.main_frame, 
            text=f"{self.bank.bank_name} - {self.bank.bank_location}",
            style='Header.TLabel'
        )
        self.header.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_customer_tab()
        self.create_account_tab()
        self.create_view_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(
            self.main_frame, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(5, 0))
        self.update_status("Ready")
    
    def update_status(self, message: str):
        self.status_var.set(message)
    
    def create_customer_tab(self):
        """Create the customer management tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Customer Management")
        
        # Customer ID
        ttk.Label(tab, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.customer_id_entry = ttk.Entry(tab)
        self.customer_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Customer Name
        ttk.Label(tab, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.customer_name_entry = ttk.Entry(tab)
        self.customer_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Customer Address
        ttk.Label(tab, text="Customer Address:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.customer_address_entry = ttk.Entry(tab)
        self.customer_address_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Customer Phone
        ttk.Label(tab, text="Customer Phone:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.customer_phone_entry = ttk.Entry(tab)
        self.customer_phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Buttons frame
        button_frame = ttk.Frame(tab)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Add Customer Button
        ttk.Button(
            button_frame, 
            text="Add Customer", 
            command=lambda: add_customer(self.bank, self)
        ).pack(side=tk.LEFT, padx=5)
        
        # Update Customer Button
        ttk.Button(
            button_frame, 
            text="Update Customer", 
            command=lambda: update_customer(self.bank, self)
        ).pack(side=tk.LEFT, padx=5)
        
        # Delete Customer Button
        ttk.Button(
            button_frame, 
            text="Delete Customer", 
            command=lambda: delete_customer(self.bank, self)
        ).pack(side=tk.LEFT, padx=5)
        
        # Search Customer Button
        ttk.Button(
            button_frame, 
            text="Search Customer", 
            command=lambda: search_customer(self.bank, self)
        ).pack(side=tk.LEFT, padx=5)
    
    def create_account_tab(self):
        """Create the account management tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Account Management")
        
        # Customer ID
        ttk.Label(tab, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.account_customer_id_entry = ttk.Entry(tab)
        self.account_customer_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Account Number
        ttk.Label(tab, text="Account Number:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.account_number_entry = ttk.Entry(tab)
        self.account_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Buttons
        button_frame = ttk.Frame(tab)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Open Account Button
        ttk.Button(
            button_frame, 
            text="Open Account", 
            command=lambda: open_account(self.bank, self)
        ).pack(side=tk.LEFT, padx=5)
        
        # View Accounts Button
        ttk.Button(
            button_frame, 
            text="View Accounts", 
            command=self.view_accounts
        ).pack(side=tk.LEFT, padx=5)
    
    def create_view_tab(self):
        """Create the view all customers tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="View All Customers")
        
        # Text widget to display customers
        self.customer_text = tk.Text(tab, wrap=tk.WORD, height=20, width=80)
        scrollbar = ttk.Scrollbar(tab, command=self.customer_text.yview)
        self.customer_text.configure(yscrollcommand=scrollbar.set)
        
        self.customer_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Refresh button
        ttk.Button(
            tab, 
            text="Refresh List", 
            command=lambda: display_all_customers(self.bank, self)
        ).pack(pady=5)
    
    def view_accounts(self):
        """View accounts for a specific customer"""
        try:
            customer_id = int(self.account_customer_id_entry.get())
            customer = self.bank.search_customer(customer_id)
            
            if customer:
                if customer.accounts:
                    accounts_info = "\n".join(
                        f"Account: {acc_num}, Balance: {balance}"
                        for acc_num, balance in customer.accounts.items()
                    )
                    messagebox.showinfo(
                        "Accounts", 
                        f"Accounts for {customer.customer_name}:\n{accounts_info}"
                    )
                else:
                    messagebox.showinfo("Accounts", "This customer has no accounts")
            else:
                messagebox.showerror("Error", "Customer not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid Customer ID")


# Your original functions adapted for GUI (all take bank as first parameter)
def add_customer(bank: Bank, app: BankApp):
    try:
        customer_id = int(app.customer_id_entry.get())
        customer_name = app.customer_name_entry.get()
        customer_address = app.customer_address_entry.get()
        customer_phone = app.customer_phone_entry.get()
        
        if not all([customer_name, customer_address, customer_phone]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        customer = Customer(customer_id, customer_name, customer_address, customer_phone)
        if bank.add_customer(customer):
            messagebox.showinfo("Success", "Customer added successfully")
            app.update_status(f"Customer {customer_id} added")
            # Clear fields
            app.customer_id_entry.delete(0, tk.END)
            app.customer_name_entry.delete(0, tk.END)
            app.customer_address_entry.delete(0, tk.END)
            app.customer_phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Customer ID already exists")
    except ValueError:
        messagebox.showerror("Error", "Invalid Customer ID")


def update_customer(bank: Bank, app: BankApp):
    try:
        customer_id = int(app.customer_id_entry.get())
        if not bank.find_customer(customer_id):
            messagebox.showerror("Error", "Customer doesn't exist.")
            return
        
        new_address = app.customer_address_entry.get()
        new_phone = app.customer_phone_entry.get()
        
        if bank.update_customer(customer_id, new_address, new_phone):
            messagebox.showinfo("Success", "Customer updated successfully")
            app.update_status(f"Customer {customer_id} updated")
        else:
            messagebox.showerror("Error", "Failed to update customer")
    except ValueError:
        messagebox.showerror("Error", "Invalid Customer ID")


def delete_customer(bank: Bank, app: BankApp):
    try:
        customer_id = int(app.customer_id_entry.get())
        if not bank.find_customer(customer_id):
            messagebox.showerror("Error", "Customer doesn't exist.")
            return
        
        if bank.delete_customer(customer_id):
            messagebox.showinfo("Success", "Customer deleted successfully")
            app.update_status(f"Customer {customer_id} deleted")
            # Clear fields
            app.customer_id_entry.delete(0, tk.END)
            app.customer_name_entry.delete(0, tk.END)
            app.customer_address_entry.delete(0, tk.END)
            app.customer_phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to delete customer")
    except ValueError:
        messagebox.showerror("Error", "Invalid Customer ID")


def search_customer(bank: Bank, app: BankApp):
    try:
        customer_id = int(app.customer_id_entry.get())
        customer = bank.search_customer(customer_id)
        
        if customer:
            # Update the fields with customer data
            app.customer_name_entry.delete(0, tk.END)
            app.customer_name_entry.insert(0, customer.customer_name)
            app.customer_address_entry.delete(0, tk.END)
            app.customer_address_entry.insert(0, customer.customer_address)
            app.customer_phone_entry.delete(0, tk.END)
            app.customer_phone_entry.insert(0, customer.customer_phone)
            
            app.update_status(f"Found customer {customer_id}")
            messagebox.showinfo("Customer Found", str(customer))
        else:
            messagebox.showerror("Error", "Customer doesn't exist.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Customer ID")


def open_account(bank: Bank, app: BankApp):
    try:
        customer_id = int(app.account_customer_id_entry.get())
        account_number = int(app.account_number_entry.get())
        
        if not bank.find_customer(customer_id):
            # Customer doesn't exist - create new one
            messagebox.showinfo("Info", "Customer doesn't exist. Creating new customer.")
            
            # Get customer details through dialog
            customer_name = simpledialog.askstring("New Customer", "Customer Name:")
            customer_address = simpledialog.askstring("New Customer", "Customer Address:")
            customer_phone = simpledialog.askstring("New Customer", "Customer Phone:")
            
            if not all([customer_name, customer_address, customer_phone]):
                messagebox.showerror("Error", "All customer details are required")
                return
            
            new_customer = Customer(customer_id, customer_name, customer_address, customer_phone)
            bank.add_customer(new_customer)
        
        if bank.open_account(customer_id, account_number):
            messagebox.showinfo("Success", f"Account {account_number} opened successfully")
            app.update_status(f"Account {account_number} opened for customer {customer_id}")
            app.account_number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Account already exists")
    except ValueError:
        messagebox.showerror("Error", "Invalid Customer ID or Account Number")


def display_all_customers(bank: Bank, app: BankApp):
    customers = bank.display_all_customers()
    app.customer_text.delete(1.0, tk.END)
    
    if not customers:
        app.customer_text.insert(tk.END, "No customers in the bank")
    else:
        for customer in customers.values():
            app.customer_text.insert(tk.END, str(customer) + "\n\n")
    
    app.update_status(f"Displaying {len(customers)} customers")


def main():
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
