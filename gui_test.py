import customtkinter

def button_callback():
    print('Button pressed')

app = customtkinter.CTk()
app.title('MyApp')
app.geometry('720x340')

button = customtkinter.CTkButton(app, text="The Button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()