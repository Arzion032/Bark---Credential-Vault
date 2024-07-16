from tkinter import *
from pathlib import Path
import backend
import re

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Label, messagebox
    
BASE_PATH = Path(__file__).parent

ASSETS_PATH = BASE_PATH / 'assets' / 'frame0'

column_heading = ["Student_ID", "Student_Name","Contact_No", "Department"]

def Create():
    if entry_1.get() == "" or entry_2.get() == "" or entry_3.get() == "" or entry_4.get() == "":
        messagebox.showerror("ERROR", "It looks like you missed a spot! Please fill in all required fields.")
        if entry_1.get() == "":
            error_label_1.config(text="*This field cannot be left blank")
        if entry_2.get() == "":
            error_label_2.config(text="*This field cannot be left blank")
        if entry_3.get() == "":
            error_label_3.config(text="*This field cannot be left blank")
        if entry_4.get() == "":
            error_label_4.config(text="*This field cannot be left blank")
    else:
        if e1_validate_if_empty() and e2_validate_if_empty() and e3_validate_if_empty() and e4_validate_if_empty():
                backend.Create(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
                Destroy()
                Show()
        else:
            messagebox.showerror("ERROR", "Please Input Valid Entry")
    

def Read():
    table.delete(*table.get_children())
    records = backend.Read(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
    for i, (Student_ID, Student_Name, Contact_No, Department) in enumerate(records, start=1):
        table.insert("", "end", values=(Student_ID, Student_Name, Contact_No, Department))
def Update():
    backend.Update(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
    Show()
    Destroy()
    
def Delete():
    backend.Delete(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
    Destroy()
    Show()
def Show():
    
    table.delete(*table.get_children())
    records = backend.Show()
    for i, (Student_ID, Student_Name, Contact_No, Department) in enumerate(records, start=1):
        table.insert("", "end", values=(Student_ID, Student_Name, Contact_No, Department))
    Destroy()  
    
def Destroy():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_1.focus_set()
    error_label_1.config(text=" ")
    error_label_2.config(text=" ")
    error_label_3.config(text=" ")
    error_label_4.config(text=" ")
def GetValue(event):
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    row_id = table.selection()[0]
    select = table.set(row_id)
    entry_1.insert(0,select['Student_ID'])
    entry_2.insert(0,select['Student_Name'])
    entry_3.insert(0,select['Contact_No'])
    entry_4.insert(0,select['Department'])
def e1_validate_if_empty():
    
    value = entry_1.get()
    pattern = r'^\d{4}-[A-Z]{2}-\d{5}-\d$'
    if value == "":
        error_label_1.config(text=" ")
        return False
    else:
        if not re.match(pattern, value):
            error_label_1.config(text="* Must follow the format 2024-MN-05161-0")
            return False
        else:
            error_label_1.config(text=" ")
            return True
    
def e2_validate_if_empty():
    
    value = entry_2.get()
    pattern = r'[^a-zA-Z\s\'-]'
    if value == "":
        error_label_2.config(text=" ")
        return False
    else:
        if re.search(pattern, value):
            error_label_2.config(text="* Must not contain numbers and special characters",fg="red")
            return False
        else:
            error_label_2.config(text=" ")
            return True

def e3_validate_if_empty():
    
    value = entry_3.get()
    pattern = r'[^a-zA-Z\s\'-]'
    if value == "":
        error_label_3.config(text=" ")
        return False
    else:
        if not value[:2] == "09":
            error_label_3.config(text="* Invalid Philippine contact number (must start with \"09\")",fg="red")
            return False
        else:
            if len(value) != 11:
                error_label_3.config(text="* Error: Philippine contact number should be exactly 11 characters long",fg="red")
                return False
            else:
                error_label_3.config(text=" ")
                return True
def e4_validate_if_empty():
    
    value = entry_4.get()
    pattern = r'[^a-zA-Z0-9- ]'
    if value == "":
        error_label_4.config(text=" ")
        return False
    else:
        if re.search(pattern, value):
            error_label_4.config(text="* Must not contain any special characters aside from \"-\" ",fg="red")
            return False
        else:
            error_label_4.config(text=" ")
            return True


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x750")
window.configure(bg = "#0C0B0B")


canvas = Canvas(
    window,
    bg = "#0C0B0B",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    958.0,
    124.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    50.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    56.0,
    54.0,
    image=image_image_3
)

canvas.create_text(
    83.0,
    167.0,
    anchor="nw",
    text="Student Number",
    fill="#FFFFFF",
    font=("Itim Regular", 25 * -1)
)

canvas.create_text(
    83.0,
    317.0,
    anchor="nw",
    text="Department",
    fill="#FFFFFF",
    font=("Itim Regular", 25 * -1)
)

canvas.create_text(
    83.0,
    217.0,
    anchor="nw",
    text="Student Name",
    fill="#FFFFFF",
    font=("Itim Regular", 25 * -1)
)

canvas.create_text(
    83.0,
    267.0,
    anchor="nw",
    text="Contact No.",
    fill="#FFFFFF",
    font=("Itim Regular", 25 * -1)
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    418.5,
    182.0,
    image=entry_image_1
)

error_label_1 = Label(text = "",fg="red",background="#0D0C0C", font=("@Microsoft JhengHei",10, "bold"))
error_label_1.place(x=540, y=170.0)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12),
    validatecommand= e1_validate_if_empty,
    validate="focusout"
)


entry_1.place(
    x=321.0,
    y=162.0,
    width=195.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    418.5,
    232.0,
    image=entry_image_2,
    
)

error_label_2 = Label(text = "",fg="red",background="#0D0C0C", font=("@Microsoft JhengHei",10, "bold"))
error_label_2.place(x=540, y=220.0)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12),
    validatecommand= e2_validate_if_empty,
    validate="focusout"
)
entry_2.place(
    x=321.0,
    y=212.0,
    width=195.0,
    height=38.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    418.5,
    282.0,
    image=entry_image_3
)

error_label_3 = Label(text = "",fg="red",background="#0D0C0C", font=("@Microsoft JhengHei",10, "bold"))
error_label_3.place(x=540, y=270.0)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12),
    validatecommand= e3_validate_if_empty,
    validate="focusout"
)
entry_3.place(
    x=321.0,
    y=262.0,
    width=195.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    418.5,
    332.0,
    image=entry_image_4
)

error_label_4 = Label(text = "",fg="red",background="#0D0C0C", font=("@Microsoft JhengHei",10, "bold"))
error_label_4.place(x=540, y=320.0)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12),
    validatecommand= e4_validate_if_empty,
    validate="focusout"
)
entry_4.place(
    x=321.0,
    y=312.0,
    width=195.0,
    height=38.0
)
custom_font = ('Helvetica', 14, 'bold')

button_1 = Button(
    window, 
    text="Create", 
    font=custom_font, 
    relief="flat",
    command= lambda: Create()
)
button_1.place(
    x=146.0,
    y=385.0,
    width=76.0,
    height=43.0
)

button_2 = Button(
    window,
    text="Read", 
    font=custom_font, 
    relief="flat",
    command= lambda: Read()
)
button_2.place(
    x=242.0,
    y=385.0,
    width=107.0,
    height=43.0
)

button_3 = Button(
    window, 
    text="Update", 
    font=custom_font, 
    relief="flat",
    command = lambda: Update()
)
button_3.place(
    x=369.0,
    y=385.0,
    width=107.0,
    height=43.0
)

button_4 = Button(
    window, 
    text="Delete", 
    font=custom_font, 
    relief="flat", 
    command= lambda: Delete()
    )
button_4.place(
    x=496.0,
    y=385.0,
    width=107.0,
    height=43.0
)
button_5 = Button(
    window, 
    text="Show", 
    font=custom_font, 
    relief="flat", 
    command= lambda: Show()
    )
button_5.place(
    x=623.0,
    y=385.0,
    width=107.0,
    height=43.0
)
button_6 = Button(
    window, 
    text="Clear", 
    font=custom_font, 
    relief="flat", 
    command= lambda: Destroy()
    )
button_6.place(
    x=750.0,
    y=385.0,
    width=107.0,
    height=43.0
)
################################################################ FOR TABLE/TREEVIEW
style = ttk.Style()
style.theme_use("clam")  # Choose a ttk theme

table = ttk.Treeview(master=window, columns= column_heading, show = "headings")

#Scroll bar
def on_mousewheel(event):
    scroll_amount = 0.1  # Adjust this value for smoother or slower scrolling
    table.yview_scroll(-1 * int(event.delta/120 * scroll_amount), "units")
    
vsb = ttk.Scrollbar(window, orient="vertical", command=table.yview,style="Custom.Vertical.TScrollbar")
style.configure("Custom.Vertical.TScrollbar", gripcount=0, background="white", troughcolor="black", bordercolor="black", arrowcolor="black", width=20)

table.configure(yscrollcommand=vsb.set)


for column in column_heading:
    table.heading(column, text = column)
    if column == "No.":
        table.column(column, width = 0, anchor="w")
    else:
        table.column(column, width = 70, anchor="w")


    
#Headding
style.configure("Treeview.Heading", background="black", fieldbackground="black", font=("@Malgun Gothic", 13))
style.map("Treeview.Heading", foreground=[("!active", "white"), ("active", "black")])       

#Rows
style.configure("Treeview", font=("@Malgun Gothic Semilight", 11), rowheight=25)
table.tag_configure('evenrow', background='white')
table.tag_configure('oddrow', background='lightgray')
style.map("Treeview", background=[('selected', 'black')])

table.bind("<MouseWheel>", on_mousewheel)

table.place(x=146.0, y=455, width=700,height=240)
vsb.place(x=846, y=455, height=240)
Show()

table.bind('<Double-Button-1>',GetValue)
window.resizable(False, False)

window.mainloop()
