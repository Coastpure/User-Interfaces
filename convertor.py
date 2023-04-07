import tkinter as tk
#from tkinter import ttk
# ttkbootstrap has better styling
import ttkbootstrap as ttk   

def convert():
    # mile_input asks gets value inout from entry_int.get(), this is the value that we get inside the text box named entry
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    # output_string prints the conversion result.
    output_string.set(km_output)

# window
window = ttk.Window(themename= 'journal')
window.title('Demo')
window.geometry('300x150')

# title
title_lable = ttk.Label(master = window, text= 'Miles to Kilometes', font= 'Calibri 20 bold')
title_lable.pack()

# input field
input_frame = ttk.Frame(master= window)
# variable that holds the value of the entry widget, in our case it's an entry integer, it will create a separate var that can store & update values (textvariable)
# entry int is defined at the very top, it will capture the values we input in entry
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
# N/B for command, we only want to pass a function, not to call it like convert()
button = ttk.Button(master = input_frame, text= 'Convert', command= convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output label, this label will change on convert.
# output_string stores the variable, it is defined at the very top
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text= 'output', textvariable= output_string,  font= 'Calibri 20')
output_label.pack(pady=5)

window.mainloop()