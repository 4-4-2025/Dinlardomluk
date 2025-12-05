from random import randint
from tkinter import *

t = Tk()

def promjena_boje(val):
    print("Trenutna vrijednost: ", val)


f = Frame(t)
f.grid(padx = 100, pady = 50)

#Naslov
naslov = Label(f, text = 'Mješalica', font = ("Georgia", 30, "bold"))
naslov.grid(row = 0, column = 0, columnspan = 2)

#Trazena boja
crvena = randint(0, 255)
zelena = randint(0, 255)
plava = randint(0, 255)
boja = f'#{crvena:02x}{zelena:02x}{plava:02x}'


trazena = Canvas(f, bg = boja, height = 100, width = 100)
trazena.grid(row = 1, column = 2, padx = 50)
mijesana = Canvas(f, bg = "black", height = 100, width = 100)
mijesana.grid(row = 3, column = 2, padx = 50)

trazena_tekst = Label(f, text = 'Tražena boja', font = ("Georgia", 15, "bold"))
trazena_tekst.grid(row = 1, column = 3)
mijesana_tekst = Label(f, text = 'Miješana boja', font = ("Georgia", 15, "bold"))
mijesana_tekst.grid(row = 3, column = 3)

#Stavljanje R G B teksta
r = Label(f, text = 'R', fg = 'Red')
r.grid(row = 1, column = 0, padx = 5, pady = 5)
g = Label(f, text = 'G', fg = 'Green')
g.grid(row = 2, column = 0, padx = 5, pady = 5)
b = Label(f, text = 'B', fg = 'Blue')
b.grid(row = 3, column = 0, padx = 5, pady = 5)

#Stavljanje slidera
slider1 = Scale(f,
                  from_ = 0, to = 255,
                  orient = "horizontal",
                  length = 300,
                  #command = show_value
                )
slider1.grid(row = 1, column = 1, padx = 5, pady = 5)
slider2 = Scale(f,
                  from_ = 0, to = 255,
                  orient = "horizontal",
                  length = 300,
                  #command = show_value
                )
slider2.grid(row = 2, column = 1, padx = 5, pady = 5)
slider3 = Scale(f,
                  from_ = 0, to = 255,
                  orient = "horizontal",
                  length = 300,
                  #command = show_value
                )
slider3.grid(row = 3, column = 1, padx = 5, pady = 5)

#Gumb ('Izmiješaj')
b = Button(f, text = 'Izmiješaj!', command = promjena_boje,
           width = 15, height = 2, font = ("Georgia", 17, "bold"))
b.grid(row = 4, column = 1)

t.mainloop()

