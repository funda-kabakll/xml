from xml.etree import ElementTree as ET
from tkinter import Tk, Label, Button, Canvas, Scrollbar, Frame
from PIL import Image, ImageTk
import webbrowser

pencere = Tk()
pencere.title("XML Project")
pencere.geometry("600x650")

navigasyon = 0

def ileriGit():
    global navigasyon
    navigasyon += 1
    if navigasyon >= num_entries:
        navigasyon = 0
    goster(navigasyon)

def geriGit():
    global navigasyon
    navigasyon -= 1
    if navigasyon < 0:
        navigasyon = num_entries - 1
    goster(navigasyon)

def open_link(event):
    identifier_value = event.widget.cget("text")
    webbrowser.open(identifier_value)

tree = ET.parse('veriSeti.xml')
root = tree.getroot()
num_entries = len(root)

def goster(navigasyon):
    resim = root[navigasyon][1].text
    icerik = root[navigasyon][0].text
    subject = root[navigasyon][2].text
    creator = root[navigasyon][3].text
    contributor = root[navigasyon][4].text
    description = root[navigasyon][5].text
    language = root[navigasyon][6].text
    identifier = root[navigasyon][7].text

    gorsel = ImageTk.PhotoImage(Image.open(resim))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=9, columnspan=2, padx=10, pady=10)

    frame = Frame(pencere)
    frame.grid(row=2, columnspan=2, padx=10, pady=10)

    canvas = Canvas(frame, width=500, height=200, scrollregion=(0, 0, 500, 500))
    canvas.grid(row=0, column=0, padx=10, pady=10)

    scrollbar = Scrollbar(frame, command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    canvas.config(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas)
    canvas.create_window(0, 0, window=inner_frame, anchor='nw')

    metin = Label(inner_frame, text=icerik, wraplength=500, justify="left")
    metin.grid(row=0, column=0, padx=10, pady=10)

    metin2 = Label(inner_frame, text=subject, wraplength=500, justify="left")
    metin2.grid(row=1, column=0, padx=10, pady=10)

    metin3 = Label(inner_frame, text=creator, wraplength=500, justify="left")
    metin3.grid(row=2, column=0, padx=10, pady=10)

    metin4 = Label(inner_frame, text=contributor, wraplength=500, justify="left")
    metin4.grid(row=3, column=0, padx=10, pady=10)

    metin5 = Label(inner_frame, text=description, wraplength=500, justify="left")
    metin5.grid(row=4, column=0, padx=10, pady=10)

    metin6 = Label(inner_frame, text=language, wraplength=500, justify="left")
    metin6.grid(row=5, column=0, padx=10, pady=10)

    metin7 = Label(inner_frame, text=identifier, wraplength=500, justify="left", fg="blue", cursor="hand2")
    metin7.grid(row=6, column=0, padx=10, pady=10)
    metin7.bind("<Button-1>", open_link)

ileriButon = Button(pencere, text="İleri", command=ileriGit)
geriButon = Button(pencere, text="Geri", command=geriGit)

ileriButon.grid(row=1, column=1, padx=10, pady=10)
geriButon.grid(row=1, column=0, padx=10, pady=10)

goster(navigasyon)

pencere.mainloop()
