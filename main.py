from tkinter import *

random_sayı = Tk()


def random():
    import random
    sayı_aralığı = int(entry.get())
    sayı_aralığı2 = int(entry2.get())
    label.config(text=random.randrange(sayı_aralığı, sayı_aralığı2))


entry = Entry(random_sayı)
entry.place(x=70, y=120)

entry2 = Entry(random_sayı)
entry2.place(x=70, y=160)

label = Label(random_sayı)
label.config(text="random sayı", font=("Arial", 20))
label.place(x=20, y=60)

label2 = Label(random_sayı)
label2.config(text="Min. sayı giriniz:", font=("Arial", 8))
label2.place(x=70, y=100)

label3 = Label(random_sayı)
label3.config(text="Mak. sayı giriniz:", font=("Arial", 8))
label3.place(x=70, y=140)

buton = Button(random_sayı)
buton.config(text="random", bg="black", fg="white", command=random)
buton.place(x=70, y=200)

mainloop()
