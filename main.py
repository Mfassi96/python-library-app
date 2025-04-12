from tkinter import *
import backend

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        list1.insert(END, row)

def insert_command():
    backend.insert(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def get_selected_row(event):
    global selected_row
    index = list1.curselection()[0]
    selected_row = list1.get(index)
    title_entry.delete(0, END)
    title_entry.insert(0, selected_row[1])
    author_entry.delete(0, END)
    author_entry.insert(0, selected_row[2])
    year_entry.delete(0, END)
    year_entry.insert(0, selected_row[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(0, selected_row[4])

def delete_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


window = Tk()
window.title("Bookstore App")

title_lbl = Label(window, text="Title").grid(row=0, column=0)
title_text = StringVar()
title_entry = Entry(window, textvariable=title_text) 
title_entry.grid(row=0, column=1) 
year_lbl = Label(window, text="Year").grid(row=1, column=0)
year_text = StringVar()
year_entry = Entry(window, textvariable=year_text) 
year_entry.grid(row=1, column=1) 

author_lbl = Label(window, text="Author").grid(row=0, column=2)
author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3) 

isbn_lbl = Label(window, text="ISBN").grid(row=1, column=2)
isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text) 
isbn_entry.grid(row=1, column=3) 

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_command).grid(row=3, column=3)
b3 = Button(window, text="Add Entry", width=12, command=insert_command).grid(row=4, column=3)
b4 = Button(window, text="Update", width=12,command=update_command).grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12, command=delete_command).grid(row=6, column=3)
b6 = Button(window, text="Close", width=12,command=window.destroy).grid(row=7, column=3)

window.mainloop()