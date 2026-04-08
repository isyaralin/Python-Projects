import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime, timedelta


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        self.current_date = datetime.today()
        self.events_file = "events.txt"
        self.events = self.load_events()
        self.selected_date = None

        self.create_widgets()
        self.display_calendar()

    def load_events(self):
        events = {}
        try:
            with open(self.events_file, "r") as file:
                for line in file:
                    date, event = line.strip().split("|", 1)
                    if date in events:
                        events[date].append(event)
                    else:
                        events[date] = [event]
        except FileNotFoundError:
            pass
        return events

    def save_events(self):
        with open(self.events_file, "w") as file:
            for date, event_list in self.events.items():
                for event in event_list:
                    file.write(f"{date}|{event}\n")

    def create_widgets(self):
        self.title_label = tk.Label(self.root, font=("Helvetica", 16))
        self.title_label.grid(row=0, column=1)

        self.prev_button = tk.Button(self.root, text="<", command=self.prev_month)
        self.prev_button.grid(row=0, column=0)

        self.next_button = tk.Button(self.root, text=">", command=self.next_month)
        self.next_button.grid(row=0, column=2)

        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.grid(row=1, column=0, columnspan=3)

        self.actions_frame = tk.Frame(self.root)
        self.actions_frame.grid(row=2, column=0, columnspan=3)

        self.add_button = tk.Button(self.actions_frame, text="Add Event", command=self.add_event_action)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(self.actions_frame, text="Edit Events", command=self.edit_event_action)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.actions_frame, text="Delete Event", command=self.delete_event_action)
        self.delete_button.grid(row=0, column=2, padx=5)

    def display_calendar(self):
   
        self.title_label.config(text=self.current_date.strftime("%B %Y"))

        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        first_day_of_month = self.current_date.replace(day=1)
        start_day = first_day_of_month.weekday()
        days_in_month = self.days_in_month(self.current_date.year, self.current_date.month)
    
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days_of_week):
            label = tk.Label(self.calendar_frame, text=day, width=10, height=2, relief="solid")
            label.grid(row=0, column=i)

        row, col = 1, start_day
        for day in range(1, days_in_month + 1):
            event_key = self.current_date.replace(day=day).strftime("%Y-%m-%d")
            event_texts = self.events.get(event_key, [])
        
            event_display = "\n".join(event_texts) if event_texts else ""
        
    
            if event_texts and self.current_date.replace(day=day) < datetime.today() and not (self.current_date.day == day):
                font_style = ("Helvetica", 10, "overstrike")
            else:
                font_style = ("Helvetica", 10)

        
            button = tk.Button(
                self.calendar_frame,
                text=f"{day}\n{event_display}",
                width=10,
                height=4,
                relief="solid",
                bg="white",  
                font=font_style,  
                command=lambda day=day: self.select_date(day),
                )
            button.grid(row=row, column=col)

            col += 1
            if col > 6:
                col = 0
                row += 1


    def prev_month(self):
        self.current_date = self.current_date.replace(day=1) - timedelta(days=1)
        self.current_date = self.current_date.replace(day=1)
        self.display_calendar()

    def next_month(self):
        next_month = self.current_date.replace(day=28) + timedelta(days=4)
        self.current_date = next_month.replace(day=1)
        self.display_calendar()

    def days_in_month(self, year, month):
        next_month = month % 12 + 1
        next_month_year = year if month < 12 else year + 1
        first_of_next_month = datetime(next_month_year, next_month, 1)
        return (first_of_next_month - timedelta(days=1)).day

    def select_date(self, day):
        self.selected_date = self.current_date.replace(day=day)

    def add_event_action(self):
        if self.selected_date is not None:
            event_key = self.selected_date.strftime("%Y-%m-%d")
            event_info = simpledialog.askstring("Add Event", f"Enter a new event for {self.selected_date.strftime('%Y-%m-%d')}:")
            if event_info:
                if event_key in self.events:
                    self.events[event_key].append(event_info)
                else:
                    self.events[event_key] = [event_info]
                self.save_events()
                self.display_calendar()
        else:
            messagebox.showinfo("No Date Selected", "Please select a date first.")

    def edit_event_action(self):
        if self.selected_date is not None:
            event_key = self.selected_date.strftime("%Y-%m-%d")
            if event_key in self.events and self.events[event_key]:
                events = self.events[event_key]
                event_list = "\n".join(f"{idx + 1}: {event}" for idx, event in enumerate(events))
                event_choice = simpledialog.askstring("Edit Event", f"Choose an event to edit:\n{event_list}\n\nEnter the event number:")

                if event_choice:
                    try:
                        choice = int(event_choice) - 1
                        if choice < 0 or choice >= len(events):
                            raise ValueError("Invalid event number")
                        new_event = simpledialog.askstring("Edit Event", f"Edit the event:\n{events[choice]}")
                        if new_event:
                            events[choice] = new_event
                            self.save_events()
                            self.display_calendar()
                    except ValueError:
                        messagebox.showerror("Invalid Choice", "Please choose a valid event number.")
            else:
                messagebox.showinfo("No Events", f"No events found for {self.selected_date.strftime('%Y-%m-%d')}.")
        else:
            messagebox.showinfo("No Date Selected", "Please select a date first.")

    def delete_event_action(self):
        if self.selected_date is not None:
            event_key = self.selected_date.strftime("%Y-%m-%d")
            if event_key in self.events and self.events[event_key]:
                events = self.events[event_key]
                event_list = "\n".join(f"{idx + 1}: {event}" for idx, event in enumerate(events))
                event_choice = simpledialog.askstring("Delete Event", f"Choose an event to delete:\n{event_list}\n\nEnter the event number:")

                if event_choice:
                    try:
                        choice = int(event_choice) - 1
                        if choice < 0 or choice >= len(events):
                            raise ValueError("Invalid event number")
                        del events[choice]
                        if not events:
                            del self.events[event_key]
                        self.save_events()
                        self.display_calendar()
                    except ValueError:
                        messagebox.showerror("Invalid Choice", "Please choose a valid event number.")
            else:
                messagebox.showinfo("No Events", f"No events found for {self.selected_date.strftime('%Y-%m-%d')}.")
        else:
            messagebox.showinfo("No Date Selected", "Please select a date first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
    
