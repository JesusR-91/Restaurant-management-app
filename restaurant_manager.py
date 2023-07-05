from tkinter import *
import math
import random
import datetime
from tkinter import filedialog, messagebox

# Variables
num_invoice = 0
operator = ""

# Products
food_list = ["Bravas", "Chicken wings", "Roasted Chicken with fries", "Lamb with rice",
             "Salmon with salad", "Hake with salad", "Mediterranean Salad", "Greek salad"]

drink_list = ["Coke", "Zero Coke", "Diet Coke", "Alhambra", "Estrella Galicia", "Estrella Galicia 0%",
              "Red house wine", "White house wine"]

deserts_list = ["Coulant", "Cheese cake", "Chocolate cake", "Brownie",
                "Mouse", "Ice cream", "Melon", "Dessert of the day"]
food_prices = [6, 5, 12, 12, 15, 17, 8, 8]
drinks_prices = [1.99, 1.99, 2.5, 2.5, 3, 3, 2.5, 2.5]
deserts_prices = [5.6, 6, 5.8, 7, 5.5, 4.5, 4.5, 3]


# Functions

# Calculator functions
def click_button(num):
    global operator
    operator = operator + num
    calculator.delete(0, END)
    calculator.insert(END, operator)


def delete():
    calculator.delete(0, END)
    global operator
    operator = ""


def calculate_resoult():
    global operator
    try:
        resoult = str(eval(operator))
        calculator.delete(0, END)
        calculator.insert(0, resoult)
        operator = ""
    except:
        calculator.delete(0, END)
        calculator.insert(0, "ERR")
        operator = ""


# Function for enable/disable select items checkbox
def checking():
    x = 0

    for c in food_list:
        if food_variable[x].get() == 1:
            food_ammount[x].config(state=NORMAL)
            if food_ammount[x].get() == "0":
                food_ammount[x].delete(0, END)
            food_ammount[x].focus()
        else:
            food_ammount[x].config(state=DISABLED)
            food_text[x].set("0")
        x += 1

    x = 0

    for c in drink_list:
        if drinks_variable[x].get() == 1:
            drinks_ammount[x].config(state=NORMAL)
            if drinks_ammount[x].get() == "0":
                drinks_ammount[x].delete(0, END)
            drinks_ammount[x].focus()
        else:
            drinks_ammount[x].config(state=DISABLED)
            drinks_text[x].set("0")
        x += 1
    x = 0

    for c in deserts_list:
        if deserts_variable[x].get() == 1:
            deserts_ammount[x].config(state=NORMAL)
            if deserts_ammount[x].get() == "0":
                deserts_ammount[x].delete(0, END)
            deserts_ammount[x].focus()
        else:
            deserts_ammount[x].config(state=DISABLED)
            deserts_text[x].set("0")
        x += 1


# Total button function
def total_calculated():
    # Food
    food_subtotal = 0
    p = 0
    for ammount in food_text:
        food_subtotal = food_subtotal + (float(ammount.get()) * float(food_prices[p]))
        p += 1

    # Drinks
    drinks_subtotal = 0
    p = 0
    for ammount in drinks_text:
        drinks_subtotal = drinks_subtotal + (float(ammount.get()) * float(drinks_prices[p]))
        p += 1

    # Deserts
    deserts_subtotal = 0
    p = 0
    for ammount in deserts_text:
        deserts_subtotal = deserts_subtotal + (float(ammount.get()) * float(deserts_prices[p]))
        p += 1

    all_subtotal = food_subtotal + drinks_subtotal + deserts_subtotal
    all_taxes = all_subtotal * 0.21
    final_total = all_subtotal + all_taxes

    var_food_price.set(f'€{round(food_subtotal, 2)}')
    var_drinks_price.set(f'€{round(drinks_subtotal, 2)}')
    var_deserts_price.set(f'€{round(deserts_subtotal, 2)}')
    var_subtotal.set(f'€{round(all_subtotal, 2)}')
    var_taxes.set(f'€{round(all_taxes, 2)}')
    var_total.set(f'€{round(final_total, 2)}')


# Invoice buttons functions
def invoice_calculated():
    invoice_text.delete(1.0, END)
    global num_invoice
    date = datetime.datetime.now()
    date_invoice = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}:{date.second}'
    invoice_text.insert(END, f"Invoice number: {num_invoice} \t\t\t {date_invoice}\n")
    invoice_text.insert(END, f"\t" + f"-" * 40 + "\n")
    invoice_text.insert(END, f"Items\t\tAmmount\t\tPrice\n")
    invoice_text.insert(END, f"\t" + f"-" * 40 + "\n")

    # Food
    x = 0
    for food in food_text:
        if food.get() != "0":
            invoice_text.insert(END, f"{food_list[x]}\t\t{food.get()}\t\t"
                                     f"€{int(food.get()) * food_prices[x]}\n")
            x+=1

    # Drinks
    x = 0
    for drink in drinks_text:
        if drink.get() != "0":
            invoice_text.insert(END, f"{drink_list[x]}\t\t{drink.get()}\t\t"
                                     f"€{int(drink.get()) * drinks_prices[x]}\n")
            x += 1

    # Deserts
    x = 0
    for desert in deserts_text:
        if desert.get() != "0":
            invoice_text.insert(END, f"{deserts_list[x]}\t\t{desert.get()}\t\t"
                                     f"€{int(desert.get()) * deserts_prices[x]}\n")
            x += 1

    invoice_text.insert(END, f"\t" + f"-" * 40 + "\n")
    invoice_text.insert(END, f"Subtotal: \t\t\t {var_subtotal.get()}\n")
    invoice_text.insert(END, f"Taxes: \t\t\t {var_taxes.get()}\n")
    invoice_text.insert(END, f"Total: \t\t\t {var_total.get()}\n")
    invoice_text.insert(END, f"\t" + f"-" * 40 + "\n")
    invoice_text.insert(END, f"Thanks for everything, see you soon!")

    num_invoice += 1


def save_invoice():
    info_invoice = invoice_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    file.write(info_invoice)
    file.close()
    messagebox.showinfo("Information", "Your invoice has been saved")


# Reset button function
def reset_action():
    invoice_text.delete(1.0, END)

    # Food
    for text in food_text:
        text.set("0")
    for input in food_ammount:
        input.config(state=DISABLED)
    for check in food_variable:
        check.set(0)

    # Drinks
    for text in drinks_text:
        text.set("0")
    for input in drinks_ammount:
        input.config(state=DISABLED)
    for check in drinks_variable:
        check.set(0)

    # Deserts
    for text in deserts_text:
        text.set("0")
    for input in deserts_ammount:
        input.config(state=DISABLED)
    for check in deserts_variable:
        check.set(0)

    var_food_price.set("")
    var_drinks_price.set("")
    var_deserts_price.set("")
    var_subtotal.set("")
    var_taxes.set("")
    var_total.set("")

# Iniciate tkinter
app = Tk()
app.title("Restaurant manage system")
app.config(bg="dark grey")

# Screen size
screen_width = math.floor(app.winfo_screenwidth() * 0.55)
screen_height = math.floor(app.winfo_screenheight() * 0.55)
x = math.floor(app.winfo_screenwidth() / 4)
y = math.floor(app.winfo_screenheight() / 4)

app.geometry(f"{screen_width}x{screen_height}+{x}+{y}")

# Superior screen
sup_screen = Frame(app, bd=1, relief=SUNKEN)
sup_screen.pack(side=TOP)

sup_title = Label(sup_screen,
                  text="Facturation system",
                  fg="LightBlue4",
                  font=("Arial", 40),
                  bg="light grey",
                  width=40)
sup_title.grid(row=0, column=0)

# Left screen
left_screen = Frame(app,
                    bd=1,
                    relief=SUNKEN,
                    bg="dark grey")
left_screen.pack(side=LEFT)

price_screen = Frame(left_screen,
                     bd=1,
                     relief=RAISED,
                     bg="light grey")
price_screen.pack(side=BOTTOM)

# Food
food_screen = LabelFrame(left_screen,
                         text="FOOD",
                         font=("Dosis", 19, "bold"),
                         bd=1,
                         relief=RAISED,
                         fg="LightBlue4")
food_screen.pack(side=LEFT)

# Drinks
drink_screen = LabelFrame(left_screen,
                          text="DRINKS",
                          font=("Dosis", 19, "bold"),
                          bd=1,
                          relief=RAISED,
                          fg="LightBlue4")
drink_screen.pack(side=LEFT)

# Deserts
deserts_screen = LabelFrame(left_screen,
                            text="DESERTS",
                            font=("Dosis", 19, "bold"),
                            bd=1,
                            relief=RAISED,
                            fg="LightBlue4")
deserts_screen.pack(side=LEFT)

# Right screen
right_screen = Frame(app,
                     bd=1,
                     relief=RAISED)
right_screen.pack(side=RIGHT)

# Calculate
calculator_panel = Frame(right_screen, bd=1, bg="light grey")
calculator_panel.pack()

# Invoice
invoice_panel = Frame(right_screen, bd=1, bg="light grey")
invoice_panel.pack()

# Buttons
buttons_panel = Frame(right_screen, bd=1, bg="light grey")
buttons_panel.pack()

# Food items
food_variable = []
food_ammount = []
food_text = []
count = 0

for food in food_list:

    # Creating checkbuttons
    food_variable.append("")
    food_variable[count] = IntVar()
    food = Checkbutton(food_screen,
                       text=food.title(),
                       font=("Dosis", 15, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=food_variable[count],
                       command=checking)
    food.grid(row=count,
              column=0,
              sticky=W)

    # Creating input
    food_ammount.append("")
    food_text.append("")
    food_text[count] =StringVar()
    food_text[count].set("0")
    food_ammount[count] = Entry(food_screen,
                                font=("Dosis", 15, "bold"),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=food_text[count])
    food_ammount[count].grid(row=count,
                             column=1)

    count += 1

# Drink items
drinks_variable = []
drinks_ammount = []
drinks_text = []
count = 0

for drink in drink_list:

    # Creating checkbuttons
    drinks_variable.append("")
    drinks_variable[count] = IntVar()
    drink = Checkbutton(drink_screen,
                        text=drink.title(),
                        font=("Dosis", 15, "bold"),
                        onvalue=1,
                        offvalue=0,
                        variable=drinks_variable[count],
                        command=checking)
    drink.grid(row=count,
               column=0,
               sticky=W)

    # Creating input
    drinks_ammount.append("")
    drinks_text.append("")
    drinks_text[count] = StringVar()
    drinks_text[count].set("0")
    drinks_ammount[count] = Entry(drink_screen,
                                font=("Dosis", 15, "bold"),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=drinks_text[count])
    drinks_ammount[count].grid(row=count,
                             column=1)

    count += 1

# Deserts items
deserts_variable = []
deserts_ammount = []
deserts_text = []
count = 0

for deserts in deserts_list:

    # Creating checkbuttons
    deserts_variable.append("")
    deserts_variable[count] = IntVar()
    deserts = Checkbutton(deserts_screen,
                          text=deserts.title(),
                          font=("Dosis", 15, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=deserts_variable[count],
                          command=checking)
    deserts.grid(row=count,
                 column=0,
                 sticky=W)

    # Creating input
    deserts_ammount.append("")
    deserts_text.append("")
    deserts_text[count] = StringVar()
    deserts_text[count].set("0")
    deserts_ammount[count] = Entry(deserts_screen,
                                  font=("Dosis", 15, "bold"),
                                  bd=1,
                                  width=6,
                                  state=DISABLED,
                                  textvariable=deserts_text[count])
    deserts_ammount[count].grid(row=count,
                               column=1)

    count += 1

# Cost and input fields
# Variables
var_food_price = StringVar()
var_drinks_price = StringVar()
var_deserts_price = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()

# Food
food_price = Label(price_screen,
                   text="Food",
                   font=("Dosis", 12, "bold"),
                   fg="LightBlue4",
                   bg="light grey")

food_price.grid(row=0, column=0)

food_price_text = Entry(price_screen,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_food_price)

food_price_text.grid(row=0, column=1, padx=41)


# Drinks
drinks_price = Label(price_screen,
                   text="Drinks",
                   font=("Dosis", 12, "bold"),
                   fg="LightBlue4",
                   bg="light grey")

drinks_price.grid(row=1, column=0)

drinks_price_text = Entry(price_screen,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_drinks_price)

drinks_price_text.grid(row=1, column=1, padx=41)

# Deserts
deserts_price = Label(price_screen,
                   text="Deserts",
                   font=("Dosis", 12, "bold"),
                   fg="LightBlue4",
                   bg="light grey")

deserts_price.grid(row=2, column=0)


deserts_price_text = Entry(price_screen,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_deserts_price)

deserts_price_text.grid(row=2, column=1, padx=41)

# Subtotal
subtotal = Label(price_screen,
                   text="Subtotal",
                   font=("Dosis", 12, "bold"),
                   fg="LightBlue4",
                   bg="light grey")

subtotal.grid(row=0, column=2)

subtotal_text = Entry(price_screen,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_subtotal)

subtotal_text.grid(row=0, column=3, padx=41)

# Taxes
taxes = Label(price_screen,
                   text="Taxes",
                   font=("Dosis", 12, "bold"),
                   fg="LightBlue4",
                   bg="light grey")

taxes.grid(row=1, column=2)

taxes_text = Entry(price_screen,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_taxes)

taxes_text.grid(row=1, column=3, padx=41)

# Total
total = Label(price_screen,
                   text="Total",
                   font=("Dosis", 12, "bold"),
                   fg="LightBlue4",
                   bg="light grey")

total.grid(row=2, column=2)

total_text = Entry(price_screen,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_total)

total_text.grid(row=2, column=3, padx=41)

# Buttons

buttons = ["Total", "Invoice", "Save", "Reset"]
buttons_created = []
column_count = 0

for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=("Dosis", 15, "bold"),
                    fg="LightBlue4",
                    bg="light grey",
                    bd=1,
                    width=9)
    buttons_created.append(button)

    button.grid(row=0, column=column_count)

    column_count += 1

# Buttons config
buttons_created[0].config(command=total_calculated)
buttons_created[1].config(command=invoice_calculated)
buttons_created[2].config(command=save_invoice)
buttons_created[3].config(command=reset_action)

# Invoice
invoice_text = Text(invoice_panel,
                    font=("Dosis", 15, "bold"),
                    bd=1,
                    width=42,
                    height=10)
invoice_text.grid(row=0, column=0)

# Calculator
calculator = Entry(calculator_panel,
                   font=("Dosis", 16, "bold"),
                   width=38,
                   bd=1)
calculator.grid(row=0, column=0, columnspan=4)

buttons_calculator = ["7", "8", "9", "+",
                      "4", "5", "6", "-",
                      "1", "2", "3", "x",
                      "C", "D", "0", "/"]
buttons_saved = []
calculator_row = 1
calculator_column = 0

for button in buttons_calculator:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=("Dosis", 16, "bold"),
                    fg="LightBlue4",
                    bg="light grey",
                    bd=1,
                    width=8)
    buttons_saved.append(button)
    button.grid(row=calculator_row, column=calculator_column)

    if calculator_column == 3:
        calculator_row += 1

    calculator_column += 1

    if calculator_column == 4:
        calculator_column = 0

# Calculator buttons configuration
buttons_saved[0].config(command=lambda: click_button("7"))
buttons_saved[1].config(command=lambda: click_button("8"))
buttons_saved[2].config(command=lambda: click_button("9"))
buttons_saved[3].config(command=lambda: click_button("+"))
buttons_saved[4].config(command=lambda: click_button("4"))
buttons_saved[5].config(command=lambda: click_button("5"))
buttons_saved[6].config(command=lambda: click_button("6"))
buttons_saved[7].config(command=lambda: click_button("-"))
buttons_saved[8].config(command=lambda: click_button("1"))
buttons_saved[9].config(command=lambda: click_button("2"))
buttons_saved[10].config(command=lambda: click_button("3"))
buttons_saved[11].config(command=lambda: click_button("*"))
buttons_saved[12].config(command=calculate_resoult)
buttons_saved[13].config(command=delete)
buttons_saved[14].config(command=lambda: click_button("0"))
buttons_saved[15].config(command=lambda: click_button("/"))

# App loop
app.mainloop()
