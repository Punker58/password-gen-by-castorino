# -  import ttk
from tkinter import *
import random
import string
import pyperclip
import pygame
import customtkinter

# - import codice backend
#from logic.core import *

# - dichiaro root, title, finestra
customtkinter.set_appearance_mode("System")
root = customtkinter.CTk()
root.title("Password generator by castorino v3")
root.geometry('500x500')
#root.iconbitmap('./icona.ico')
root.minsize(width=355, height=250)
root.maxsize(width=355, height=250)

root["bg"] = "#222234"

pygame.mixer.init()

#####
#####    BISOGNA PASSARE LA FUNZIONA NEL FILE CORE ***
#####

# - genera password

def generaPsswd():

    # -  assegno alias 

    lun = lunghezza.get()
    num = numeri.get()
    sim = simboli.get()

    if lun == 0 or lun == None:
        lun = 6
    else:
        lun = lunghezza.get()


    # - condizioni

    if num == TRUE and sim == TRUE: # - caso : numeri + simboli
        caratteri = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(caratteri) for n in range(lun))
        testobox.set(password)
    elif num == TRUE:  # - caso : numeri 
        caratteri = string.digits + string.ascii_letters 
        password = ''.join(random.choice(caratteri) for n in range(lun))
        testobox.set(password)
    elif sim == TRUE: # - caso : simboli
        caratteri = string.ascii_letters + string.punctuation
        password = ''.join(random.choice(caratteri) for n in range(lun))
        testobox.set(password)
    else: # - caso : senza numeri e simboli
        caratteri = string.ascii_letters
        password = ''.join(random.choice(caratteri) for n in range(lun))
        testobox.set(password)

# -  copia testo

def copiaTesto():
    box = testobox.get()

    if box == '':
        dialog = customtkinter.CTkInputDialog(master = None, text = "Hai scoperto una sezione easter egg:", title = "ERRORE BARONOSO!")
        easterEgg = dialog.get_input()

        if easterEgg == 'fuck off bitch':

            label = customtkinter.CTkLabel(master = root,
                                            text = "FUCK OFF BARO",
                                            width = 120,
                                            height = 25,
                                            corner_radius = 8)
            label.pack()  
        else:
            pass

        pygame.mixer.music.load("logic/culattone.wav")
        pygame.mixer.music.play(loops=0)
    else:
        pyperclip.copy(testobox.get())


# - print easter egg

def easterEgg():
    print('ciao')

# - assegnazione valori  

testobox = StringVar(root,)
numeri = IntVar()
simboli = IntVar()
lunghezza = IntVar()

# - assegnazione tasti

box = customtkinter.CTkEntry(master = root,
                            textvariable = testobox,
                            state = DISABLED)

boxCopia = customtkinter.CTkButton(master = root,
                                    text = 'COPIA',
                                    command=copiaTesto)

checkNumeri = customtkinter.CTkSwitch( master = root,
                                        text = "Numeri",
                                        variable=numeri)

checkSimboli = customtkinter.CTkSwitch(master = root,
                                        text = "Simboli",
                                        variable=simboli)

label = customtkinter.CTkLabel(master = root,
                                textvariable = lunghezza,
                                text = '6-128',
                                width = 120,
                                height = 25,
                                corner_radius = 8)
  
sliderLunghezza = customtkinter.CTkSlider(master = root,
                                        from_= 6,
                                        to = 128,
                                        orient=HORIZONTAL,
                                        variable=lunghezza)

bottone = customtkinter.CTkButton(master = root,
                                    text = "GENERA",
                                    command=generaPsswd)

# - pack =  servono per renderizzare i tasti ecc..

box.pack(pady=10)
boxCopia.pack(pady=10)
checkNumeri.pack()
checkSimboli.pack(pady=5)
label.pack() 
sliderLunghezza.pack(pady=5)
bottone.pack()

# - renderizza la finestra

root.mainloop()


