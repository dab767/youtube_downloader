import customtkinter

def button_callback():
    print('Button pressed')
    print(check128.get())

app = customtkinter.CTk()
app.grid_columnconfigure(0, weight=1)
app.title('MyApp')
app.geometry('720x340')

input = customtkinter.CTkEntry(app,width=450,corner_radius=5)
input.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

button = customtkinter.CTkButton(app, text="Download and Convert", width=250, command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

check128 = customtkinter.IntVar(value=0)
convert128 = customtkinter.CTkCheckBox(app, text='128kbp', variable=check128, onvalue=1, offvalue=0)
convert128.grid(row=2, column=0, padx=20, pady=(0,20), stick='w')

convert192 = customtkinter.CTkCheckBox(app, text='192kbp')
convert192.grid(row=2, column=1, padx=20, pady=(0,20), stick='w')

app.mainloop()