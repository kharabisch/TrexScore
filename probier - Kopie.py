from tkinter import *


'''
# To do
# Eingabefeld leer
def zahl_holen():
    zahl1 = int(entry_zahl1.get())
    zahl2 = int(entry_zahl2.get())
'''

def addieren():
    # Übernahme der Daten aus den Eigabefeldern mit der Funktin get()
    trex1 = int(entry_trex1.get())
    king1 = int(entry_king1.get())
    dame1 = int(entry_dame1.get())
    karo1 = int(entry_karo1.get())
    plus1 = int(entry_plus1.get())

    # Addiere beide Zahlen
    erg = trex1 + king1 + dame1 + karo1 + plus1
    # erg in label schreiben
    label_result.config(text = str(erg))


# Erstelle das Hauptfenster
fenster = Tk()
# Titel festlegen
fenster.title("Rechner")
# Größe des Fensters
fenster.geometry("600x400")
label_trex1 = Label(fenster, text = "Trex1")
label_trex1.place(x = 10, y = 10)
# Eingabefelder
entry_trex1 = Entry(fenster, bg = "white")
entry_trex1.place(x = 80, y = 10)

label_king1 = Label(fenster, text = "King1")
label_king1.place(x = 10, y = 40)
entry_king1 = Entry(fenster, bg = "white")
entry_king1.place(x = 80, y = 40)

label_dame1 = Label(fenster, text = "Dame1")
label_dame1.place(x = 10, y = 70)
entry_dame1 = Entry(fenster, bg = "white")
entry_dame1.place(x = 80, y = 70)

label_karo1 = Label(fenster, text = "Karo1")
label_karo1.place(x = 10, y = 100)
entry_karo1 = Entry(fenster, bg = "white")
entry_karo1.place(x = 80, y = 100)

label_plus1 = Label(fenster, text = "Plus1")
label_plus1.place(x = 10, y = 130)
entry_plus1 = Entry(fenster, bg = "white")
entry_plus1.place(x = 80, y = 130)

label_ergebnis = Label(fenster, text = "Total1")
label_ergebnis.place(x = 10, y = 160)

label_result = Label(fenster, text = "")
label_result.place(x = 80, y = 160)

# Aktionen, Buttons, um Aktionen auslösen zu können
button_plus = Button(fenster, font = "20", text = "+", command = addieren)
button_plus.place(x = 230, y = 10, width = 20, height = 130)

#--------------------------------TREX1------------------------------------------------------------

def addieren1():
    # Übernahme der Daten aus den Eigabefeldern mit der Funktin get()
    trex2 = int(entry_trex2.get())
    king2 = int(entry_king2.get())
    dame2 = int(entry_dame2.get())
    karo2 = int(entry_karo2.get())
    plus2 = int(entry_plus2.get())

    # Addiere beide Zahlen
    erg2 = trex2 + king2 + dame2 + karo2 + plus2
    # erg in label schreiben
    label_result1.config(text = str(erg2))




def summe():
    result = int(label_result.get())            ###########     UPDATE !!!!!!!!  #''#######################
    result1= int(label_result1.get())
    totalo = result+result1
    label_total.config(text=str(totalo))

'''# Erstelle das Hauptfenster
fenster = Tk()
# Titel festlegen
fenster.title("Rechner")
# Größe des Fensters
fenster.geometry("600x400")'''
label_trex2 = Label(fenster, text = "Trex2")
label_trex2.place(x = 10, y = 200)
# Eingabefelder
entry_trex2 = Entry(fenster, bg = "white")
entry_trex2.place(x = 80, y = 200)

label_king2 = Label(fenster, text = "King2")
label_king2.place(x = 10, y = 230)
entry_king2 = Entry(fenster, bg = "white")
entry_king2.place(x = 80, y = 230)

label_dame2 = Label(fenster, text = "Dame2")
label_dame2.place(x = 10, y = 260)
entry_dame2 = Entry(fenster, bg = "white")
entry_dame2.place(x = 80, y = 260)

label_karo2 = Label(fenster, text = "Karo2")
label_karo2.place(x = 10, y = 290)
entry_karo2 = Entry(fenster, bg = "white")
entry_karo2.place(x = 80, y = 290)

label_plus2 = Label(fenster, text = "Plus2")
label_plus2.place(x = 10, y = 320)
entry_plus2 = Entry(fenster, bg = "white")
entry_plus2.place(x = 80, y = 320)

label_ergebnis2 = Label(fenster, text = "Total2")
label_ergebnis2.place(x = 10, y = 350)

label_result1 = Label(fenster, text = "")
label_result1.place(x = 80, y = 350)


label_total = Label(fenster, text = "")
label_total.place(x = 420, y = 350)
# Aktionen, Buttons, um Aktionen auslösen zu können
button_plus = Button(fenster, font = "20", text = "+", command = addieren1)
button_plus.place(x = 230, y = 200, width = 20, height = 130)

button_total = Button(fenster, font = "20", text = "=", fg = 'white',command = summe)########  Summe Button ################
button_total.place(x = 390, y = 190, width = 50, height = 130)

fenster.mainloop()

# Übung:
# Implementieren Sie die restlichen drei Button ( button_minus, button_mult und button_div)

