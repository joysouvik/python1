from tkinter import *
from tkinter.ttk import*

window=Tk()
window.title('PhoneBook')

dictionary_phone_book={}


#Creating ADD to contacts
def add_to_contact():
    window_1 =  Toplevel(window)

    fr1 = Frame(window_1)
    fr1.pack()
    fr2 = Frame(window_1)
    fr2.pack()

    window_1.title('Add Contacts')

    l1=Label(fr1,text='Name')
    l1.pack(side='left')

    e1=Entry(fr1,text='25')
    e1.pack(side='right')

    l2=Label(fr2,text='Number')
    l2.pack(side='left')

    e2=Entry(fr2,text='10')
    e2.pack(side='right')

    #Function to add the contact
    def add():
        name=e1.get()
        num=e2.get()
        dictionary_phone_book[name]=num
        e1.delete(0,END)
        e2.delete(0,END)

        print(dictionary_phone_book)

    bu2=Button(window_1,text='Add',command=add)
    bu2.pack()

#Creating Search Window

def search_contact():

    window_2 = Toplevel(window)

    fr3 = Frame(window_2)
    fr3.pack()
    fr4 = Frame(window_2)
    fr4.pack()

    window_2.title('Search Directory')

    l3=Label(fr3,text='Name')
    l3.pack(side='left')

    e3=Entry(fr3,text='25')
    e3.pack(side='right')

    l4 = Label(fr4, text='Number')
    l4.pack(side='left')

    e4 = Entry(fr4, text='10')
    e4.pack(side='right')

    #search function
    def find():
        name1=e3.get()
        num1=e4.get()
        if num1 !='':
            num2=int(num1)
        else:
            pass
        e3.delete(0, END)
        e4.delete(0, END)

        if name1 in dictionary_phone_book.keys():
            print(f'Name:{name1} Number:{dictionary_phone_book[name1]}')

        elif num1 in dictionary_phone_book.values():

            def get_key(val):
                for key, value in dictionary_phone_book.items():
                    if value==val:
                        return key

            k=(get_key(num1))
            print(f'Name:{k} Number:{dictionary_phone_book[k]}')

        else:
            print('contact not found')

    #Creation of Find button
    button3=Button(window_2,text='Find',command=find)
    button3.pack()


#Creation of Search button
button1=Button(window,text='Search',command=search_contact)
button1.pack()

#Creatiion of Add contact button
button2=Button(window,text='Add Contact',command= add_to_contact)
button2.pack()

window.mainloop()
