from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import *

opt = {1: "Car", 6: "Hydrant", 11: "Chimney"}
i = randrange(1, 16, 5)
img_ran = {1: "c1.jpg", 2: "c2.jpg", 3: "c3.jpg", 4: "c4.jpg", 5: "c5.jpg", 6: "h1.jpg", 7: "h2.jpg", 8: "h3.jpg",
           9: "h4.jpg", 10: "h5.jpg", 11: "s1.jpg", 12: "s2.jpg", 13: "s3.jpg", 14: "s4.jpg", 15: "s6.jpg"}
i1 = randrange(1, 16, 1)
i2 = randrange(1, 16, 1)
i3 = randrange(1, 16, 1)
i4 = randrange(1, 16, 1)
i5 = randrange(1, 16, 1)
i6 = randrange(1, 16, 1)
i7 = randrange(1, 16, 1)
i8 = randrange(1, 16, 1)
i9 = randrange(1, 16, 1)
iS = [i1, i2, i3, i4, i5, i6, i7, i8, i9]
iT = []

for x in range(9):
    if (iS[x] == i or iS[x] == i + 1 or iS[x] == i + 2 or iS[x] == i + 3 or iS[x] == i + 4):
        iT.append(iS[x])

root = Tk()
root.title("Captcha Verification")
root.configure(bg='#2b2b2b')
_l1 = Label(root, text="Select all images which contain a " +
            opt[i], font=('Helvetica', 20, 'bold'))
_l1.grid(row=0, column=3, columnspan=10)

img = ImageTk.PhotoImage(Image.open(img_ran[i1]))
imglabel1 = Label(root, image=img, bg="black", width=150, height=150)
imglabel1.grid(row=2, column=0, rowspan=5, columnspan=5)
var1 = IntVar()
c1 = Checkbutton(root, variable=var1, highlightthickness=0,
                 bd=0, offvalue=0, onvalue=i1)
c1.grid(row=6, column=4)

img1 = ImageTk.PhotoImage(Image.open(img_ran[i2]))
imglabel2 = Label(root, image=img1, bg="black", width=150, height=150)
imglabel2.grid(row=2, column=5, rowspan=5, columnspan=5)
var2 = IntVar()
c2 = Checkbutton(root, variable=var2, highlightthickness=0,
                bd=0, offvalue=0, onvalue=i2)
c2.grid(row=6, column=9)

img2 = ImageTk.PhotoImage(Image.open(img_ran[i3]))
imglabel3 = Label(root, image=img2, bg="black", width=150, height=150)
imglabel3.grid(row=2, column=10, rowspan=5, columnspan=5)
var3 = IntVar()
c3 = Checkbutton(root, variable=var3, highlightthickness=0,
                bd=0, offvalue=0, onvalue=i3)
c3.grid(row=6, column=14)

img3 = ImageTk.PhotoImage(Image.open(img_ran[i4]))
imglabel4 = Label(root, image=img3, bg="black", width=150, height=150)
imglabel4.grid(row=7, column=0, rowspan=5, columnspan=5)
var4 = IntVar()
c4 = Checkbutton(root, variable=var4, highlightthickness=0,
                bd=0, offvalue=0, onvalue=i4)
c4.grid(row=11, column=4)

img4 = ImageTk.PhotoImage(Image.open(img_ran[i5]))
imglabel5 = Label(root, image=img4, bg="black", width=150, height=150)
imglabel5.grid(row=7, column=5, rowspan=5, columnspan=5)
var5 = IntVar()
c5 = Checkbutton(root, variable=var5, highlightthickness=0,
                 bd=0, offvalue=0, onvalue=i5)
c5.grid(row=11, column=9)

img5 = ImageTk.PhotoImage(Image.open(img_ran[i6]))
imglabel6 = Label(root, image=img5, bg="black", width=150, height=150)
imglabel6.grid(row=7, column=10, rowspan=5, columnspan=5)
var6 = IntVar()
c6 = Checkbutton(root, variable=var6, highlightthickness=0,
                 bd=0, offvalue=0, onvalue=i6)
c6.grid(row=11, column=14)

img6 = ImageTk.PhotoImage(Image.open(img_ran[i7]))
imglabel7 = Label(root, image=img6, bg="black", width=150, height=150)
imglabel7.grid(row=12, column=0, rowspan=5, columnspan=5)
var7 = IntVar()
c7 = Checkbutton(root, variable=var7, highlightthickness=0,
                 bd=0, offvalue=0, onvalue=i7)
c7.grid(row=16, column=4)

img7 = ImageTk.PhotoImage(Image.open(img_ran[i8]))
imglabel8 = Label(root, image=img7, bg="black", width=150, height=150)
imglabel8.grid(row=12, column=5, rowspan=5, columnspan=5)
var8 = IntVar()
c8 = Checkbutton(root, variable=var8, highlightthickness=0,
                 bd=0, offvalue=0, onvalue=i8)
c8.grid(row=16, column=9)

img8 = ImageTk.PhotoImage(Image.open(img_ran[i9]))
imglabel9 = Label(root, image=img8, bg="black", width=150, height=150)
imglabel9.grid(row=12, column=10, rowspan=5, columnspan=5)
var9 = IntVar()
c9 = Checkbutton(root, variable=var9, highlightthickness=0,
                 bd=0, offvalue=0, onvalue=i9)
c9.grid(row=16, column=14)


def verCap():
    l_var = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(),
             var6.get(), var7.get(), var8.get(), var9.get()]
    l_var1 = []
    l_var2 = []
    for i in range(9):
        if (l_var[i] != 0):
            l_var2.append(l_var[i])
            if (l_var[i] in iT):
                l_var1.append(l_var[i])

    if (len(l_var1) == len(iT) == len(l_var2)):
        imglabel1.destroy()
        c1.destroy()
        imglabel2.destroy()
        c2.destroy()
        imglabel3.destroy()
        c3.destroy()
        imglabel4.destroy()
        c4.destroy()
        imglabel5.destroy()
        c5.destroy()
        imglabel6.destroy()
        c6.destroy()
        imglabel7.destroy()
        c7.destroy()
        imglabel8.destroy()
        c8.destroy()
        imglabel9.destroy()
        c9.destroy()
        la = Label(root, text="Captcha Verified!", width=25, height=10)
        la.grid(row=1, column=1)
        but.destroy()
        _l1.destroy()
    else:
        imglabel1.destroy()
        c1.destroy()
        imglabel2.destroy()
        c2.destroy()
        imglabel3.destroy()
        c3.destroy()
        imglabel4.destroy()
        c4.destroy()
        imglabel5.destroy()
        c5.destroy()
        imglabel6.destroy()
        c6.destroy()
        imglabel7.destroy()
        c7.destroy()
        imglabel8.destroy()
        c8.destroy()
        imglabel9.destroy()
        c9.destroy()
        lb = Label(root, text="Uh Oh! Captcha Mismatch! Try Again!",
                   width=45, height=10)
        lb.grid(row=1, column=1)
        but.destroy()
        _l1.destroy()


but = Button(root, width=15, height=3, bd=5,
             fg="black", text="Submit", bg="orange", command=verCap)
but.grid(row=17, column=8)
root.mainloop()