from tkinter import *
from tkinter import ttk

# Function to print the receipt
def print_receipt():
    tott = float(totText.get())
    top = Toplevel()
    top.geometry("300x300")
    top.config(bg="white")
    l = Label(top, text='---------RECEIPT----------')
    l.pack()
    l.config(bg="white")
    heading = Label(top, text='\tItem\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(bg="white")

    for child in listBox.get_children():
        item = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty = float(listBox.item(child, 'values')[2])
        tot = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t{price}\t{qty}\t{tot}')
        item1.config(bg="white")
        item1.pack()

    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()

# Function to add items to the list
def show():
    tot = 0
    for i, var in enumerate(checkbox_vars):
        if var.get():
            price = int(entries[i].get())
            qty = int(entries[i+5].get())
            tot = int(price * qty)
            listBox.insert("", "end", values=(labels[i], price, qty, tot))

    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3])
    totText.set(sum1)

# Initialize tkinter
root = Tk()
root.title("Payment Receipt Generator")
root.geometry("1000x600")
root.configure(bg="lightblue")  

# Heading label
heading_label = Label(root, text="Payment Receipt Generator", font="arial 22 bold", bg="lightblue")
heading_label.place(x=5, y=10)

# Labels for items
labels = ["Coca Cola", "Bun", "Chicken Fry", "Roll", "Fish Fried Rice"]

# Create Checkbutton instances and store their variables in the list
checkbox_vars = []
for i, label in enumerate(labels):
    var = IntVar()  # Create IntVar instance for each Checkbutton
    checkbox_vars.append(var)  # Add variable to the list
    Checkbutton(root, text=label, variable=var, bg="lightblue").place(x=10, y=50 + 30 * i)

# Entries for price and quantity
entries = []
for i in range(len(labels)):
    e = Entry(root)
    e.place(x=140, y=50 + 30 * i)
    entries.append(e)

for i in range(len(labels)):
    e = Entry(root)
    e.place(x=300, y=50 + 30 * i)
    entries.append(e)

# Total label
totText = StringVar()
tot = Label(root, text="", font="arial 22 bold", textvariable=totText, bg="lightgray")
tot.place(x=600, y=10)

# Add and Print buttons
Button(root, text="Add", command=show, height=3, width=13).place(x=10, y=50 + 30 * len(labels))
Button(root, text="Print", command=print_receipt, height=3, width=13).place(x=850, y=120)

# Labels for column headings
Label(root, text="Item", bg="lightblue").place(x=10, y=260)
Label(root, text="Price", bg="lightblue").place(x=140, y=260)
Label(root, text="Qty", bg="lightblue").place(x=300, y=260)
Label(root, text="Total", bg="lightblue").place(x=450, y=260)

# Listbox for displaying items
cols = ('Item', 'Price', 'Qty', 'Total')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=300)

root.mainloop()
