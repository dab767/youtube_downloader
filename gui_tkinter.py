import tkinter as tk
from PIL import ImageTk

background_color = "#3d6466"

# Initiallize the App
root = tk.Tk()
root.title("Recipe Picker")
#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

# create frame widget
frame1 = tk.Frame(root, width=500, height=700, bg=background_color)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=background_color)
logo_widget.image = logo_img
logo_widget.pack()

root.mainloop()