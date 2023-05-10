import csv
import tkinter as tk
from tkinter import messagebox, Listbox

# Define a function that suggests homes based on user input
def suggest_homes():
    # Get the user input values
    price = float(price_entry.get())
    state = state_entry.get().upper()
    bedrooms = int(bedrooms_entry.get())
    bathrooms = int(bathrooms_entry.get())

    # Open the CSV file
    with open('fakeHousing.csv', 'r') as file:
        reader = csv.DictReader(file)

        # Create a dictionary to store the suggested homes
        suggested_homes = {}

        # Loop through each row in the CSV file
        for row in reader:
            # Check if the home meets the user's criteria
            if (row['State'] == state
                    and float(row['Price']) <= price
                    and int(row['Bedrooms']) >= bedrooms
                    and int(row['Bathrooms']) >= bathrooms):
                # Add the suggested home to the dictionary with its address as the key
                suggested_homes[row['Address']] = row

                # Stop if we have suggested 5 homes
                if len(suggested_homes) == 5:
                    break

        # If there are suggested homes, display them in a listbox
        if suggested_homes:
            # Create a new window to display the suggested homes
            homes_window = tk.Toplevel(root)
            homes_window.title("Suggested Homes")

            # Create a listbox to display the suggested home addresses
            homes_listbox = Listbox(homes_window)
            homes_listbox.pack(fill=tk.BOTH, expand=1)

            # Add each suggested home address to the listbox
            for address in suggested_homes:
                homes_listbox.insert(tk.END, address)

            # Create a function to display the details of a selected home
            def show_home_details(event):
                # Get the selected home address from the listbox
                selected_address = homes_listbox.get(homes_listbox.curselection())

                # Get the details of the selected home from the dictionary
                selected_home = suggested_homes[selected_address]

                # Create a new window to display the details of the selected home
                details_window = tk.Toplevel(homes_window)
                details_window.title(selected_address)

                # Create labels and display the details of the selected home
                tk.Label(details_window, text=f"Address: {selected_home['Address']}").pack()
                tk.Label(details_window, text=f"Price: ${selected_home['Price']}").pack()
                tk.Label(details_window, text=f"Bedrooms: {selected_home['Bedrooms']}").pack()
                tk.Label(details_window, text=f"Bathrooms: {selected_home['Bathrooms']}").pack()

            # Bind the function to the double click event on the listbox
            homes_listbox.bind("<Double-Button-1>", show_home_details)

        else:
            # If no homes meet the user's criteria, display an error message
            messagebox.showerror("Error", "No homes found that meet your criteria")

# Create a GUI window
root = tk.Tk()
root.title("Home Suggester")

# Create labels and entry fields for user input
tk.Label(root, text="Max Price:").grid(row=0, column=0, padx=5, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="State:").grid(row=1, column=0, padx=5, pady=5)
state_entry = tk.Entry(root)
state_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Bedrooms:").grid(row=2, column=0, padx=5, pady=5)
bedrooms_entry = tk.Entry(root)
bedrooms_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Bathrooms:").grid(row=3, column=0, padx=5, pady=5)
bathrooms_entry = tk.Entry(root)
bathrooms_entry.grid(row=3, column=1, padx=5, pady=5)

# Create a button to submit the user input and suggest homes
submit_button = tk.Button(root, text="Submit", command=suggest_homes)
submit_button.grid(row=4, column=1, padx=5, pady=5)

# Run it!
root.mainloop()

