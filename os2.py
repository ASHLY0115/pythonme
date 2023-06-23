import tkinter as tk

def convert_rupee_to_euro():
    rupee_amount = float(rupee_entry.get())
    euro_amount = rupee_amount * 0.011  # Conversion rate: 1 INR = 0.011 EUR
    euro_entry.delete(0, tk.END)  # Clear the Euro field
    euro_entry.insert(0, euro_amount)  # Update the Euro field

def convert_euro_to_rupee():
    euro_amount = float(euro_entry.get())
    rupee_amount = euro_amount / 0.011  # Conversion rate: 1 INR = 0.011 EUR
    rupee_entry.delete(0, tk.END)  # Clear the Rupee field
    rupee_entry.insert(0, rupee_amount)  # Update the Rupee field

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create and arrange the labels and entry fields
rupee_label = tk.Label(window, text="Indian Rupees:")
rupee_label.grid(row=0, column=0)
rupee_entry = tk.Entry(window, width=10)
rupee_entry.insert(0, "0.0")
rupee_entry.grid(row=1, column=0)

euro_label = tk.Label(window, text="Euros:")
euro_label.grid(row=0, column=1)
euro_entry = tk.Entry(window, width=10)
euro_entry.insert(0, "0.0")
euro_entry.grid(row=1, column=1)

# Create and arrange the conversion buttons
convert_rupee_button = tk.Button(window, text="R->E", command=convert_rupee_to_euro)
convert_rupee_button.grid(row=2, column=0)

convert_euro_button = tk.Button(window, text="E->R", command=convert_euro_to_rupee)
convert_euro_button.grid(row=2, column=1)

# Start the main event loop
window.mainloop()
