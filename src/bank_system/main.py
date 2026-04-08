import tkinter as tk
from src.bank_system.app import BankApp


def main():
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
