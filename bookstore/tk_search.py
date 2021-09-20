from tkinter import *
import tk_search_back as backend
import time

def get_selected_row(event):
    global selected_record
    try:
        index=list1.curselection()[0]
        selected_record=list1.get(index)
        #print(type(selected_record[1]))
        

        E1.delete(0, END)
        E1.insert(END, selected_record[1])
        E2.delete(0, END)
        E2.insert(END, selected_record[2])
        E3.delete(0, END)
        E3.insert(END, selected_record[3])
        E4.delete(0, END)
        E4.insert(END, selected_record[4])
        return selected_record[0]
    except:
        pass


def delete_command():
    backend.delete(selected_record[0])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def insert_command():
    list1.delete(0, END)
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def update_command():
    backend.update(selected_record[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def close_command():
    root.quit()


root = Tk()

backend.connect()

#this is the front end 
L1 = Label(root, text="Title")
L1.grid(row=0, column=0)

L2 = Label(root, text="Author")
L2.grid(row=0, column=2)

L3 = Label(root, text="Year")
L3.grid(row=1, column=0)

L4 = Label(root, text="ISBN")
L4.grid(row=1, column=2)

title_text=StringVar()
E1=Entry(root, textvariable=title_text)
E1.grid(row=0, column=1)

author_text=StringVar()
E2=Entry(root, textvariable=author_text)
E2.grid(row=0, column=3)

year_text=StringVar()
E3=Entry(root, textvariable=year_text)
E3.grid(row=1, column=1)

isbn_text=StringVar()
E4=Entry(root, textvariable=isbn_text)
E4.grid(row=1, column=3)

list1 = Listbox(root, height=8, width=50)
list1.grid(row=2, column=0, rowspan=8, columnspan=5)

sb1=Scrollbar(root)
sb1.grid(row=2, column=6, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(root, text="View all", width=12, command=view_command)
b1.grid(row=2, column=6)

b2=Button(root, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=6)

b3=Button(root, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=6)

b4=Button(root, text="Update select", width=12, command=update_command)
b4.grid(row=5, column=6)

b5=Button(root, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=6)

b6=Button(root, text="Close", width=12, command=root.destroy)
b6.grid(row=7, column=6)

root.title("Calo Book Store")

root.mainloop()



