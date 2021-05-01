# Noob-coding :)
# Trying to have some fun with Python Imaging Library(PIL)
# Using Tkinter to mix it with a simple gui

# Import everything
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.font as font
import tkinter.messagebox as tkmb
import os
from functools import partial
import webbrowser as wb

# declaring some needed variables
filename = ""
img = None
tkImage = None
bgc = "#4b4c57"
imformat = "jpg"
w = 0
h = 0

cropL = 0
cropR = 0
cropT = 0
cropB = 0

# Lots of functions to define
# one for each command
# opening image
def openImage():
    global filename, img
    try:
        filename = filedialog.askopenfilename()
        img = Image.open(filename)
        showimage()
        change_button_state()
    # For selecting any unknown file
    except AttributeError:
        return

# Activate buttons after opening image
# Set initial value for some variables

def change_button_state():
    x, y = img.size
    saveButton["state"] = "normal"
    processButton["state"] = "normal"
    resxentry["state"] = "normal"
    resxentry.delete(0, tkinter.END)
    resxentry.insert(-1, str(int(x * 2 / 3)))
    resyentry["state"] = "normal"
    resyentry.delete(0, tkinter.END)
    resyentry.insert(-1, str(int(y * 2 / 3)))
    qualityentry["state"] = "normal"
    qualityentry.delete(0, tkinter.END)
    qualityentry.insert(-1, "85")
    proportionButton["state"] = "normal"
    tmp1, tmp2 = os.path.splitext(filename)
    if tmp2 != ".jpg":
        jpgButton["state"] = "normal"
        whiteButton["state"] = "normal"
    cropLentry["state"] = "normal"
    cropLentry.delete(0, tkinter.END)
    cropLentry.insert(0, "0")
    cropRentry["state"] = "normal"
    cropRentry.delete(0, tkinter.END)
    cropRentry.insert(0, "0")
    cropTentry["state"] = "normal"
    cropTentry.delete(0, tkinter.END)
    cropTentry.insert(0, "0")
    cropBentry["state"] = "normal"
    cropBentry.delete(0, tkinter.END)
    cropBentry.insert(0, "0")

    scaleL.config(from_=0)
    scaleL.config(to=int(x/1.5-4))
    scaleR.config(from_=0)
    scaleR.config(to=int(x/1.5-4))
    scaleT.config(from_=0)
    scaleT.config(to=int(y/1.5-4))
    scaleB.config(from_=0)
    scaleB.config(to=int(y/1.5-4))

# Show image in loop, need to call this to update after every change
def showimage():
    global tkImage, w, h
    img2 = img
    w, h = img.size
    if int(h * (750 / w)) <= 600 and w > 750:
        img2 = img.resize((750, int(h * (750 / w))))
    elif h > 600:
        img2 = img.resize((int(w * (600 / h)), 600))

    tkImage = ImageTk.PhotoImage(img2)
    canvas.create_image(390, 340, image=tkImage, anchor="center")
    x, y = img2.size
    croprect(rect, x, y)
    canvas.lift(rect)

# Processing entry Inputs
# Limiting values to avoid error
def resxinput(event):
    if img is not None:
        x = int(resxentry.get())
        resxentry.delete(0, tkinter.END)
        if x > w:
            resxentry.insert(0, str(w))
        elif x < 4:
            resxentry.insert(0, str(4))
        else:
            resxentry.insert(0, str(x))
        x = int(resxentry.get())
        if proportional.get():
            resyentry.delete(0, tkinter.END)
            resyentry.insert(0, str(int(x * h / w)))


def resyinput(event):
    x = int(resyentry.get())
    resyentry.delete(0, tkinter.END)
    if x > h:
        resyentry.insert(0, str(h))
    elif x < 2:
        resyentry.insert(0, str(2))
    else:
        resyentry.insert(0, str(x))
    x = int(resyentry.get())
    if proportional.get():
        resxentry.delete(0, tkinter.END)
        resxentry.insert(0, str(int(x * w / h)))


def qualityinput(event):
    quality = int(qualityentry.get())
    qualityentry.delete(0, tkinter.END)
    if quality < 5:
        qualityentry.insert(0, str(5))
    elif quality > 100:
        qualityentry.insert(0, str(100))
    else:
        qualityentry.insert(0, str(quality))


def croplinput(event):
    global cropL
    l = int(cropLentry.get())
    cropLentry.delete(0, tkinter.END)
    if l + int(cropRentry.get()) >= w-4:
        cropLentry.insert(0, str(w-int(cropRentry.get())-6))
    elif l > w / 1.5 - 4:
        cropLentry.insert(0, str(int(w / 1.5 - 4)))
    elif l < 0:
        cropLentry.insert(0, str(0))
    else:
        cropLentry.insert(0, str(l))
    cropL = int(cropLentry.get())
    sliderL.set(cropL)
    showimage()


def croprinput(event):
    global cropR
    r = int(cropRentry.get())
    cropRentry.delete(0, tkinter.END)
    if r + int(cropLentry.get()) >= w-4:
        cropRentry.insert(0, str(w-int(cropLentry.get())-6))
    elif r > w / 1.5 - 4:
        cropRentry.insert(0, str(int(w / 1.5 - 4)))
    elif r < 0:
        cropRentry.insert(0, str(0))
    else:
        cropRentry.insert(0, str(r))
    cropR = int(cropRentry.get())
    sliderR.set(cropR)
    showimage()


def croptinput(event):
    global cropT
    t = int(cropTentry.get())
    cropTentry.delete(0, tkinter.END)
    if t + int(cropBentry.get()) >= h-4:
        cropTentry.insert(0, str(h-int(cropBentry.get())-6))
    elif t > h / 1.5 - 4:
        cropTentry.insert(0, str(int(h / 1.5 - 4)))
    elif t < 0:
        cropTentry.insert(0, str(0))
    else:
        cropTentry.insert(0, str(t))
    cropT = int(cropTentry.get())
    sliderT.set(cropT)
    showimage()


def cropbinput(event):
    global cropB
    b = int(cropBentry.get())
    cropBentry.delete(0, tkinter.END)
    if b + int(cropTentry.get()) >= h-4:
        cropBentry.insert(0, str(h-int(cropTentry.get())-6))
    if b > h / 1.5 - 4:
        cropBentry.insert(0, str(int(h / 1.5 - 4)))
    elif b < 0:
        cropBentry.insert(0, str(0))
    else:
        cropBentry.insert(0, str(b))
    cropB = int(cropBentry.get())
    sliderB.set(cropB)
    showimage()

# Main function for cropping
# Crop after changing resolution
# So keep the ratio same with some  simple calculations
def crop(x, y):
    global cropL, cropR, cropT, cropB, img
    cropR = w - cropR
    cropB = h - cropB
    cropL = x * cropL / w
    cropR = x * cropR / w
    cropT = y * cropT / h
    cropB = y * cropB / h
    img = img.crop((cropL, cropT, cropR, cropB))
    cropLentry.delete(0, tkinter.END)
    cropLentry.insert(0, "0")
    cropRentry.delete(0, tkinter.END)
    cropRentry.insert(0, "0")
    cropTentry.delete(0, tkinter.END)
    cropTentry.insert(0, "0")
    cropBentry.delete(0, tkinter.END)
    cropBentry.insert(0, "0")
    cropL = 0
    cropR = 0
    cropT = 0
    cropB = 0
    sliderL.set(0)
    sliderR.set(0)
    sliderT.set(0)
    sliderB.set(0)

# For showing the red rectangle referring the crop bounding box
def croprect(rect, x, y):
    canvas.coords(rect, 390 - x / 2 + cropL*x/w, 340 - y / 2 + cropT*y/h, 390 + x / 2 - cropR*x/w, 340 + y / 2 - cropB*y/h)

# Process the image and show
def process():
    try:
        global img, imformat, w, h
        x = int(resxentry.get())
        y = int(resyentry.get())
        img = img.resize((x, y), Image.ANTIALIAS)
        crop(x, y)
        w, h = img.size
        if IsJpg.get():
            if IsWhite.get() and img.mode == "RGBA":
                im = Image.new("RGBA", img.size, "WHITE")
                im.paste(img, (0, 0), img)
                img = im
                img = img.convert("RGB")
                IsWhite.set(False)
                whiteButton["state"] = "disabled"

            else:
                img = img.convert("RGB")
                whiteButton["state"] = "disabled"
        else:
            temp, imformat = os.path.splitext(filename)
        resxentry.delete(0, tkinter.END)
        resxentry.insert(-1, str(w))
        resyentry.delete(0, tkinter.END)
        resyentry.insert(-1, str(h))
        showimage()
        tkmb.showinfo("ProcessInfo", "Image compressed and resized successfully. \nSave the new image before quitting.")
    except:
        tkmb.showwarning("Error", "Enter valid values as input")

savedir = ""

# Saving Image function
def saveImage():
    global savedir
    imquality = int(qualityentry.get())
    try:
        savedir = filedialog.asksaveasfilename(defaultextension=imformat, title="Enter name without extension")
        img.save(savedir, optimize=True, quality=imquality)
        tkmb.showinfo("SaveInfo", "Image has been saved. \nTo check the image, go to the save directory. ")
        img.show()
    except ValueError:
        formatwarning()
        return

# Show warning if jpg check box is unchacked
def warning():
    if IsJpg.get() == False:
        ques = tkmb.askquestion("Warning",
                                "*Only uncheck this \nif u want to keep transparecy of your image.\nIt will keep your image format same\n"
                                "But note that it will increase your file size a lot.\nDo you want to continue?")
        if ques == "yes":
            IsJpg.set(False)
            whiteButton["state"] = "disabled"
        else:
            IsJpg.set(True)
    else:
        whiteButton["state"] = "normal"

def formatwarning():
    tkmb.showwarning("Invalid file format", "Enter name without format")

def transparentinfo():
    tkmb.showinfo("Transparency Info", "Checking it will make the transparent area white otherwise black.\n"
                                       "Not applicable for image without transparency.")
# Crop slider for making the crop operation easier
def slider(side, nul):
    l = sliderL.get()
    r = sliderR.get()
    t = sliderT.get()
    b = sliderB.get()
    if side == 1:
        if l+r >= w-4:
            sliderL.set(str(int(w-r-6)))
        cropLentry.delete(0, tkinter.END)
        cropLentry.insert(0, str(int(sliderL.get())))
        croplinput(0)
    elif side == 2:
        if r + l >= w-4:
            sliderR.set(str(int(w-l-6)))
        cropRentry.delete(0, tkinter.END)
        cropRentry.insert(0, str(int(sliderR.get())))
        croprinput(0)
    elif side == 3:
        if t + b >= h-4:
            sliderT.set(str(int(h-b-6)))
        cropTentry.delete(0, tkinter.END)
        cropTentry.insert(0, str(int(sliderT.get())))
        croptinput(0)
    else:
        if t + b >= h-4:
            sliderB.set(str(int(h-t-6)))
        cropBentry.delete(0, tkinter.END)
        cropBentry.insert(0, str(int(sliderB.get())))
        cropbinput(0)

# Publishing page in github
def opengit():
    wb.open("https://github.com/UnknownComplexity/PhotoScale")


# Main code
# tkinter object
gui = tkinter.Tk()
#icon
icon = Image.open("icon.png")
icontk = ImageTk.PhotoImage(icon)
gui.iconphoto(False, icontk)
box = "#54545c"  # color
# Proportional checkbox variable
proportional = tkinter.BooleanVar(gui, value=True)
# jpg checkbox variable
IsJpg = tkinter.BooleanVar(gui, value=True)
IsWhite = tkinter.BooleanVar(gui, value=True)
#slider variables
sliderL = tkinter.IntVar(gui, value=50)
sliderR = tkinter.IntVar(gui, value=50)
sliderT = tkinter.IntVar(gui, value=50)
sliderB = tkinter.IntVar(gui, value=50)
# gui window setup
gui.title("PhotoScale")
gui.geometry("1000x650")
gui.resizable(width=False, height=False)
canvas = tkinter.Canvas(gui, width=990, height=643, bg=bgc)
canvas.create_rectangle(770, 0, 1000, 650, fill=box, width=1)
rect = canvas.create_rectangle(0, 0, 0, 0, outline="red", width=2)
buttonFont = font.Font(family='Helvetica', size=20, weight='bold')
font2 = font.Font(family='Roboto', size=8)

openButton = tkinter.Button(gui, text="open", command=openImage).place(x=10, y=10)
saveButton = tkinter.Button(gui, text=" save ", command=saveImage, state="disabled")
saveButton.place(x=55, y=10)
tkinter.Button(gui, text="Documentation/Publishing Page", command=opengit).place(x=100, y=10)

# creating side Menu
tkinter.Label(gui, text="Resolution:", fg="white", bg=box).place(x=780, y=20)
tkinter.Label(gui, text="Width:", fg="white", bg=box).place(x=780, y=50)
resxentry = tkinter.Entry(gui, state="disabled")
resxentry.bind("<Return>", resxinput)
resxentry.place(x=830, y=50)
tkinter.Label(gui, text="Height:", fg="white", bg=box).place(x=780, y=80)
resyentry = tkinter.Entry(gui, state="disabled")
resyentry.place(x=830, y=80)
resyentry.bind("<Return>", resyinput)
# keeping the ratio of previous width and height same to new one
proportionButton = tkinter.Checkbutton(gui, text="proportional", variable=proportional, state="disabled",
                                       command=resxinput(0))
proportionButton.place(x=830, y=105)
# Compression quality
tkinter.Label(gui, text="Quality: 0-100 (lower = smaller file size\n but low quality output",
              anchor="e", font=font2, bg=box, fg="white").place(x=780, y=160)
qualityentry = tkinter.Entry(gui, state="disabled")
qualityentry.place(x=830, y=200)
qualityentry.bind("<Return>", qualityinput)
# Jpg = Best compression
jpgButton = tkinter.Checkbutton(gui, text="jpg", variable=IsJpg, state="disabled", command=warning)
jpgButton.place(x=810, y=225)
whiteButton = tkinter.Checkbutton(gui, text="White background",
                                  variable=IsWhite, state= "disabled", command=transparentinfo)
whiteButton.place(x=860, y=225)
# Crop menu
tkinter.Label(gui, text="Crop:", bg=box, fg="white", font=("Roboto", 11)).place(x=780, y=270)
leftLabel = tkinter.Label(gui, text="Left:", bg=box, fg="white", cursor="sb_h_double_arrow")
leftLabel.place(x=790, y=300)
cropLentry = tkinter.Entry(gui, state="disabled")
cropLentry.place(x=830, y=300)
#slider widget
scaleL = tkinter.Scale(gui, variable=sliderL, from_=0, to=0, showvalue=0, length = 200,  orient=tkinter.HORIZONTAL,
              command=partial(slider, 1))
scaleL.place(x=785, y=325)
rightLabel = tkinter.Label(gui, text="Right:", bg=box, fg="white", cursor="sb_h_double_arrow")
rightLabel.place(x=790, y=355)
cropRentry = tkinter.Entry(gui, state="disabled")
cropRentry.place(x=830, y=355)
scaleR = tkinter.Scale(gui, variable=sliderR, from_=0, to=0, showvalue=0, length = 200,  orient=tkinter.HORIZONTAL,
              command=partial(slider, 2))
scaleR.place(x=785, y=380)
topLabel = tkinter.Label(gui, text="Top:", bg=box, fg="white", cursor="sb_h_double_arrow")
topLabel.place(x=790, y=410)
cropTentry = tkinter.Entry(gui, state="disabled")
cropTentry.place(x=830, y=410)
scaleT = tkinter.Scale(gui, variable=sliderT, from_=0, to=0, showvalue=0, length = 200,  orient=tkinter.HORIZONTAL,
              command=partial(slider, 3))
scaleT.place(x=785, y=435)
bottomLabel = tkinter.Label(gui, text="Bottom:", bg=box, fg="white", cursor="sb_h_double_arrow")
bottomLabel.place(x=780, y=465)
cropBentry = tkinter.Entry(gui, state="disabled")
cropBentry.place(x=830, y=465)
scaleB = tkinter.Scale(gui, variable=sliderB, from_=0, to=0, showvalue=0, length = 200,  orient=tkinter.HORIZONTAL,
              command=partial(slider, 4))
scaleB.place(x=785, y=490)
cropLentry.bind("<Return>", croplinput)
cropRentry.bind("<Return>", croprinput)
cropTentry.bind("<Return>", croptinput)
cropBentry.bind("<Return>", cropbinput)
# Process button
processButton = tkinter.Button(gui, text="Process", font=buttonFont, fg="red4", command=process,
                               state="disabled", relief="raised", borderwidth=4)
processButton.place(x=820, y=550)
canvas.pack()
# tkinter mainloop
gui.mainloop()
