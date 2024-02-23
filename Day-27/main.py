from tkinter import *

# window = Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# my_label = Label(text="This is a label", font=("Arial", 24, "normal"))
# # my_label.pack(expand=False)

# # my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.grid(column=0 , row=0 )


# #Button
# def button_clicked():
#     my_label.config(text="Button got Clicked")

# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)


# #Entry 
# inputs = Entry(width=10)
# inputs.grid(column=3, row=4)
# def inputGet():
#     x = inputs.get()
#     my_label.config(text=x)
# inputButton = Button(text="Click Me",command=inputGet)
# inputButton.grid(column=0, row=3)



# window.mainloop()

# # def add(*arg):
# #     print(arg)
# #     sum = 0
# #     for n in arg:
# #         sum += n
# #     print(sum)

# # add(5,10,15,20)

# # def calculate(n, **kwargs):
# #     print(kwargs)
# #     # for (key, value) in kwargs.items():
# #     #     print(key)
# #     #     print(value)
# #     # print(kwargs["add"])
# #     n+= kwargs["add"]
# #     n*= kwargs["multiply"]
# #     print(n)

# # calculate(2,add=3, multiply=9)


# # class Car:
# #     def __init__(self, **kw):
# #         self.make= kw.get("make")
# #         self.model = kw.get("model")


# # my_car = Car(make="Nissan")#, model= "GT-R"
# # print(my_car.model)
# # print(my_car.make)


# Miles to KM conavator

window = Tk()
window.title("Miles to KM conavator")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

km = 0
def calculate():
    km = round(float(inputs.get()) * 1.61)
    myText2.config(text=f"is equal to    {km}    km ", font=("Arial", 15, "normal"))



inputs = Entry(width=10)
inputs.grid(column=2, row=1)
myText1 = Label(text="Miles", font=("Arial", 10, "normal"))
button = Button(text="Calculate",command=calculate)
myText2 = Label(text=f"is equal to    {km}    km ", font=("Arial", 15, "normal"))
myText1.grid(column=3,row=1)
myText2.grid(column=1,row=2)
button.grid(column=2, row=3)
# myText1.pack()
# myText2.pack()
# button.pack()


window.mainloop()