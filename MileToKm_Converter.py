from tkinter import *

def convert():
    miles = float(miles_input.get())
    kms = round(miles * 1.609)
    km_result.config(text = f'{kms}')


window = Tk()
window.title('My Converter')
window.config(padx = 20, pady = 20)

miles_input = Entry(width = 7)
miles_input.grid(column = 1, row = 0)

miles_label = Label(text = 'miles')
miles_label.grid(column = 2, row = 0)

is_equal_label = Label(text = 'is_equal_to')
is_equal_label.grid(column = 0, row = 1)

km_result = Label(text = '0')
km_result.grid(column = 1, row = 1)

km_label = Label(text = 'KM')
km_label.grid(column = 2, row = 1)

tics = Button(text = 'calculate', command = convert)
tics.grid(column = 1, row = 2)

window.mainloop()