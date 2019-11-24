from tkinter import *
from db import Database

db = Database('store.db')

# populate list
def populate_list():
	parts_list.delete(0, END)
	for row in db.fetch():
		parts_list.insert(END, row)

def add_item():
	db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
	parts_list.delete(0, END)
	parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
	clear_text()
	populate_list()


def select_item(event):
	try:
	 global selected_item
	 index = parts_list.curselection()[0]
	 selected_item = parts_list.get(index)

	 part_entry.delete(0, END)
	 part_entry.insert(END, selected_item[1])
	 customer_entry.delete(0, END)
	 customer_entry.insert(END, selected_item[2])
	 retailer_entry.delete(0, END)
	 retailer_entry.insert(END, selected_item[3])
	 price_entry.delete(0, END)
	 price_entry.insert(END, selected_item[4])
	except IndexError:
	 pass 
	

def remove_item():
	db.remove(selected_item[0])
	clear_text()
	populate_list()

def update_item():
	db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
	populate_list()

def clear_text():
	part_entry.delete(0, END)
	customer_entry.delete(0, END)
	retailer_entry.delete(0, END)
	price_entry.delete(0, END)
	


app = Tk()

# part
part_text= StringVar()
part_label = Label(app, text='part name', font=14, pady=20)
part_label.grid(row=0, column=0, sticky='w')
part_entry = Entry(app, textvariable=part_text, bg='silver')
part_entry.grid(row=0, column=1)

# Customer
customer_text= StringVar()
customer_label = Label(app, text='customer', font=14)
customer_label.grid(row=0, column=2, sticky='w')
customer_entry = Entry(app, textvariable=customer_text, bg='silver')
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text= StringVar()
retailer_label = Label(app, text='retailer', font=14)
retailer_label.grid(row=1, column=0, sticky='w')
retailer_entry = Entry(app, textvariable=retailer_text, bg='silver')
retailer_entry.grid(row=1, column=1)

# Price
price_text= StringVar()
price_label = Label(app, text='price', font=14)
price_label.grid(row=1, column=2, sticky='w')
price_entry = Entry(app, textvariable=price_text, bg='silver')
price_entry.grid(row=1, column=3)

# Parts list (listbox)
parts_list = Listbox(app, height=9, width=80, bg='silver', bd=3)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# binding scrollbar to list box
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# buttons
add_btn = Button(app, text='Add part', width=12, bg='#a6ffd2', command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove part', width=12, bg='#ff9494' ,command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update part', width=12, bg='#94a4ff' ,command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear input', width=12, bg='#fff5f5' ,command=clear_text)
clear_btn.grid(row=2, column=3)

# populate data
populate_list()

app.title("ORDER MANAGER")
app.geometry('700x350')
app.mainloop()