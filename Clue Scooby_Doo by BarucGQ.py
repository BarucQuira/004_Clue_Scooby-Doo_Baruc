# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:51:03 2023

@author: DELL
"""


import random

import tkinter as tk
from PIL import Image, ImageTk

from tkinter import  messagebox



# Define los personajes, habitaciones y armas
personajes = ["Shaggy", "Fred", "Vilma", "Daphne", "Scooby-Doo"]
habitaciones = ["Castillo Tenebroso","Biblioteca","Muelle Abandonado", "Cocina", "Sótano"]
armas = ["Espada Embrujada", "Poción Misteriosa", "Red de Atrapar", "Antorcha Encantada", "Lupa Detectiva"]


# Genera una solución aleatoria
def Aleatorio(solucion):
    solucion = {
        "personaje": random.choice(personajes),
        "habitacion": random.choice(habitaciones),
        "arma": random.choice(armas)
    }
    return solucion

def casos(opc):
    n_sol = {}
    
    txtHis = ''' '''
    personaje = opc['personaje']
    
    if personaje == 'Scooby-Doo':  
        txtHis = '''
            Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los invitados corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Scrappy-Doo, tendido en el suelo. Junto a él,
            se encontraba una antorcha encantada manchada de sangre, y no había señales 
            de entrada forzada.
            
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
                
            -Scooby-Doo afirmó que había salido al muelle abandonado para fumar un 
             cigarro con sabor a Scooby-galleta.
            -Vilma dijo que estaba en la biblioteca buscando un libro en ese momento.
            -Shaggy mencionó que estaba en la cocina preparando una taza de té mientras 
             veía a Daphne admirar las luciernagas.
            -Daphne alegó que había estado en el muelle abandonado admirando las 
             luciernagas.
            -Fred declaró que estaba en el castillo tenebroso quitando el polvo de los 
             cuadros.
            '''
        n_sol = {
            "personaje":"Scooby-Doo",
            "habitacion": "Sótano",
            "arma": "Antorcha Encantada"
        }
    if personaje == 'Vilma':
        txtHis = '''
            Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los invitados corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Scrappy-Doo, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
            
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
                
            -Scooby-Doo afirmó que estaba comiendo una manzana en la biblioteca con 
             Shaggy.
            -Vilma dijo que estaba en el castillo tenebroso quitando el polvo de los 
             cuadros.
            -Shaggy mencionó que estaba con Scooby-Doo mientras sostenia una red de 
             atrapar que encontró por ahí.
            -Daphne alegó que no encontraba su poción misteriosa en el sótano por lo
             que fue a la cocina donde a veces tambien la esconde.
            -Fred declaró que estaba arreglando el sistema de tuberias del muelle 
             abandonado, pero se dio cuenta que no habia agua en todo el lugar.
            '''
        n_sol = {
            "personaje":"Vilma",
            "habitacion": "Castillo Tenebroso",
            "arma": "Espada Embrujada"
        }
    if personaje == 'Shaggy':
        txtHis = '''
            Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los invitados corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Scrappy-Doo, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
            
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
                
            -Scooby-Doo afirmó que estaba haciendo yoga en el muelle abandonado con 
             una red de atrapar.
            -Vilma dijo que estaba en la cocina lavando los platos y cuchillos.
            -Shaggy mencionó que estaba cerrando la ventana de la biblioteca porque 
             llovió fuerte, dijo que tenia su poción misteriosa con él.
            -Daphne alegó que estaba arreglando la antorcha encantada del sótano, ya 
             que el calor no la dejaba salir.
            -Fred declaró que estaba buscando su lupa detectiva en el castillo tenebroso.
            '''
        n_sol = {
            "personaje":"Shaggy",
            "habitacion": "Muelle Abandonado",
            "arma": "Red de Atrapar"
        }
    if personaje == 'Daphne':
        txtHis = '''
            Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los invitados corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Scrappy-Doo, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
            
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
                
            -Scooby-Doo afirmó que estaba recogiendo la nieve del muelle abandonado 
             pero se tropezó con una red de atrapar.
            -Vilma dijo que estaba temblando de frio en la cocina lavando los platos 
             y cuchillos.
            -Shaggy mencionó que estaba cerrando la ventana de la biblioteca porque 
             nevo fuerte, dijo que tenia su poción misteriosa con él.
            -Daphne alegó que estaba arreglando la antorcha encantada del sótano, ya 
             que el calor no la dejaba salir.
            -Fred declaró que estaba buscando su lupa detectiva en el castillo para 
             ver mejor y arrglar el clima.
            '''
        n_sol = {
            "personaje":"Daphne",
            "habitacion": "Sótano",
            "arma": "Antorcha Encantada"
        }
    if personaje == 'Fred':
        txtHis = '''
            Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo,
            después del postre, se escuchó un estruendo proveniente de la sala de estar. 
            Los invitados corrieron hacia donde escucharon el ruido y encontraron el 
            cuerpo sin vida del anfitrión, Scrappy-Doo, tendido en el suelo. Junto a él,
            se encontraba el arma manchada de sangre, y no había señales de entrada 
            forzada.
            
            La investigación comenzó de inmediato, y cada uno de los personajes 
            principales proporcionó sus coartadas:
                
            -Scooby-Doo afirmó que estaba recogiendo la nieve del muelle abandonado 
             pero se tropezó con una red de atrapar.
            -Vilma dijo que estaba en la cocina lavando los platos y cuchillos.
            -Shaggy mencionó que estaba cerrando la ventana de la biblioteca porque 
             nevó fuerte, dijo que tenia su poción misteriosa con él.
            -Daphne alegó que estaba arreglando la antorcha encantada del sotano cuando 
             escucho a Scooby-Doo caer en el muelle abandonado.
            -Fred declaró que estaba buscando su lupa detectiva en el muelle abandonado.
            '''
        n_sol = {
            "personaje":"Fred",
            "habitacion": "Castillo Tenebroso",
            "arma": "Lupa Detectiva"
        }
     
    return txtHis, n_sol


class Ventana2_DTrama:
    def __init__(self, master, venIm):
        self.master = master
        self.venIm = venIm
        
        self.solucion = {}
        
        # Variables para almacenar la selección
        self.opc_Pers = tk.StringVar()
        self.opc_Place = tk.StringVar()
        self.opc_Arma = tk.StringVar()
        
        # Añadimos un contador de intentos
        self.intentos = 0
        self.max_intentos = 3
        
        #Etiquetas
        #Historia
        self.lbl_hist = tk.Label(self.master, text="", justify="left", font=("Arial", 11))
        self.lbl_hist.pack()
        
        
        #Preguntas
        self.lbl_pers = tk.Label(self.master, text="¿Quién es el asesino?", justify="center", font=("Arial", 11), fg="blue")
        self.lbl_pers.pack()
        self.lbl_pers.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.lbl_pers.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=40)
        
        self.lbl_place = tk.Label(self.master, text="¿Dónde se cometió el crimen?", justify="center", font=("Arial", 11), fg="green")
        self.lbl_place.pack()
        self.lbl_place.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.lbl_place.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=100)
     
        
        self.lbl_arma = tk.Label(self.master, text="¿Qué arma se usó?", justify="center", font=("Arial", 11), fg="red")
        self.lbl_arma.pack()
        self.lbl_arma.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.lbl_arma.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=160)
        
        # Crear radio buttons
        #Personaje
        self.radio_boton1 = tk.Radiobutton(self.master, text="Shaggy", variable=self.opc_Pers, value="Shaggy")
        self.radio_boton2 = tk.Radiobutton(self.master, text="Fred", variable=self.opc_Pers, value="Fred")
        self.radio_boton3 = tk.Radiobutton(self.master, text="Vilma", variable=self.opc_Pers, value="Vilma")
        self.radio_boton4 = tk.Radiobutton(self.master, text="Daphne", variable=self.opc_Pers, value="Daphne")
        self.radio_boton5 = tk.Radiobutton(self.master, text="Scooby-Doo", variable=self.opc_Pers, value="Scooby-Doo")
        
        #Lugar
        self.radio_boton6 = tk.Radiobutton(self.master, text="Castillo Tenebroso", variable=self.opc_Place, value="Castillo Tenebroso")
        self.radio_boton7 = tk.Radiobutton(self.master, text="Biblioteca", variable=self.opc_Place, value="Biblioteca")
        self.radio_boton8 = tk.Radiobutton(self.master, text="Muelle Abandonado", variable=self.opc_Place, value="Muelle Abandonado")
        self.radio_boton9 = tk.Radiobutton(self.master, text="Cocina", variable=self.opc_Place, value="Cocina")
        self.radio_boton10 = tk.Radiobutton(self.master, text="Sótano", variable=self.opc_Place, value="Sótano")
        
        
        #Arma
        self.radio_boton11 = tk.Radiobutton(self.master, text="Espada Embrujada", variable=self.opc_Arma, value="Espada Embrujada")
        self.radio_boton12 = tk.Radiobutton(self.master, text="Poción Misteriosa", variable=self.opc_Arma, value="Poción Misteriosa")
        self.radio_boton13 = tk.Radiobutton(self.master, text="Red de Atrapar", variable=self.opc_Arma, value="Red de Atrapar")
        self.radio_boton14 = tk.Radiobutton(self.master, text="Antorcha Encantada", variable=self.opc_Arma, value="Antorcha Encantada")
        self.radio_boton15 = tk.Radiobutton(self.master, text="Lupa Detectiva", variable=self.opc_Arma, value="Lupa Detectiva")
        
        
        # Posicionar radio buttons
        
        self.radio_boton1.pack()
        self.radio_boton2.pack()
        self.radio_boton3.pack()
        self.radio_boton4.pack()
        self.radio_boton5.pack()
        self.radio_boton6.pack()
        self.radio_boton7.pack()
        self.radio_boton8.pack()
        self.radio_boton9.pack()
        self.radio_boton10.pack()
        self.radio_boton11.pack()
        self.radio_boton12.pack()
        self.radio_boton13.pack()
        self.radio_boton14.pack()
        self.radio_boton15.pack()
        
        
        self.radio_boton1.place(x=10,y=400)
        self.radio_boton2.place(x=110,y=400)
        self.radio_boton3.place(x=220,y=400)
        self.radio_boton4.place(x=330,y=400)
        self.radio_boton5.place(x=440,y=400)
        
        self.radio_boton6.place(x=5,y=460)
        self.radio_boton7.place(x=130,y=460)
        self.radio_boton8.place(x=220,y=460)
        self.radio_boton9.place(x=370,y=460)
        self.radio_boton10.place(x=450,y=460)
        
        self.radio_boton11.place(x=5,y=520)
        self.radio_boton12.place(x=235,y=520)
        self.radio_boton13.place(x=425,y=520)
        self.radio_boton14.place(x=150,y=540)
        self.radio_boton15.place(x=350,y=540)


        # Botón para mostrar selección
        self.boton_mostrar = tk.Button(self.master, text="Comprobar suposiciones", command=self.comp_sup)
        self.boton_mostrar.pack()
        self.boton_mostrar.config(font=("Arial", 14))
        self.boton_mostrar.config(bg="purple", fg="white")
        self.boton_mostrar.place(x=180,y=600)
        
        
        self.selec_random()
        self.mostrar_hist()
        
        
    def cerrar_ventana(self):
        self.master.destroy()
        
    def cerrar_ventanas(self):
        self.master.destroy()  # Cierra la ventana principal
        if hasattr(self, "ventana_secundaria"):
            self.ventana_secundaria.destroy()  # Cierra la ventana secundaria
        self.venIm.destroy()
    def selec_random(self):
        self.solucion = Aleatorio(self.solucion)
    
    def mostrar_hist(self):
        self.historia,self.n_sol = casos(self.solucion)
        self.txt = self.historia
        self.solucion = self.n_sol
 
        
        self.lbl_hist.config(text= self.txt)
    
    def comp_sup(self):
        self.sel_pers = self.opc_Pers.get()
        self.sel_place = self.opc_Place.get()
        self.sel_arma = self.opc_Arma.get()
        
        
        #print("Personaje",self.solucion["personaje"])
        #print("Lugar",self.solucion["habitacion"])
        #print("Arma",self.solucion["arma"])


        
        self.intentos += 1
        
        if self.sel_pers in self.solucion["personaje"] and self.sel_place in self.solucion["habitacion"] and self.sel_arma in self.solucion["arma"]:
            messagebox.showinfo("¡Ganaste!", "¡Has adivinado correctamente!")
                  
            # Preguntar si desea jugar de nuevo
            if messagebox.askyesno("Jugar de nuevo", "¿Deseas volver a jugar?"):
                self.intentos = 0
                self.selec_random()
                self.mostrar_hist()
            else:
                self.cerrar_ventanas()
                        
      
        else:
            if self.intentos < self.max_intentos:
                messagebox.showinfo("¡Fallaste!", "Intenta de nuevo.")
            
            if self.intentos >= self.max_intentos:
                messagebox.showinfo("¡Fallaste!", "Has agotado tus intentos.")

                # Preguntar si desea jugar de nuevo
                if messagebox.askyesno("Jugar de nuevo", "¿Deseas volver a jugar?"):
                    self.intentos = 0
                    self.selec_random()
                    self.mostrar_hist()
                else:
                    self.cerrar_ventanas()



class Ventana1_MostrarPers:
    def __init__(self, master):
        self.master = master

        #Etiquetas
        
        self.lbl_title = tk.Label(master, text="¡Bienvenido al juego Clue - Scooby-Doo!")
        self.lbl_title.config(font=("Arial Bold", 20))
        self.lbl_title.config(fg="green")
        self.lbl_title.place(x=75,y=5)
        
        self.lbl_title2 = tk.Label(master, text="Murdered")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="red")
        self.lbl_title2.place(x=650,y=2)
        
        self.lbl_title2 = tk.Label(master, text="Personajes")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=90,y=40)
        
        self.lbl_title2 = tk.Label(master, text="Escenas de Crimen")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=345,y=80)
        
        self.lbl_title2 = tk.Label(master, text="Armas")
        self.lbl_title2.config(font=("Arial Bold", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=655,y=135)
        
        
        #Imagenes
        
        #Personajes
        
        img_Scrappy = Image.open("Scrappy.png")  
        img_Scrappy_tk = ImageTk.PhotoImage(img_Scrappy)
        self.lbl_img_Scrappy = tk.Label(master, image=img_Scrappy_tk)
        self.lbl_img_Scrappy.image = img_Scrappy_tk
        self.lbl_img_Scrappy.pack()
        self.lbl_img_Scrappy.place(x=675,y=27)
        
        img_Scooby_Doo = Image.open("Scooby_Doo.png")  
        img_Scooby_Doo_tk = ImageTk.PhotoImage(img_Scooby_Doo)
        self.lbl_img_Scooby_Doo = tk.Label(master, image=img_Scooby_Doo_tk)
        self.lbl_img_Scooby_Doo.image = img_Scooby_Doo_tk
        self.lbl_img_Scooby_Doo.pack()
        self.lbl_img_Scooby_Doo.place(x=100,y=75)
        
        img_Shaggy = Image.open("Shaggy.png")  
        img_Shaggy_tk = ImageTk.PhotoImage(img_Shaggy)
        self.lbl_img_Shaggy = tk.Label(master, image=img_Shaggy_tk)
        self.lbl_img_Shaggy.image = img_Shaggy_tk
        self.lbl_img_Shaggy.pack()
        self.lbl_img_Shaggy.place(x=100,y=195)
                    
        img_Velma = Image.open("Velma.png")  
        img_Velma_tk = ImageTk.PhotoImage(img_Velma)
        self.lbl_img_Velma = tk.Label(master, image=img_Velma_tk)
        self.lbl_img_Velma.image = img_Velma_tk
        self.lbl_img_Velma.pack()
        self.lbl_img_Velma.place(x=100,y=315)
        
        img_Daphne = Image.open("Daphne.png")  
        img_Daphne_tk = ImageTk.PhotoImage(img_Daphne)
        self.lbl_img_Daphne = tk.Label(master, image=img_Daphne_tk)
        self.lbl_img_Daphne.image = img_Daphne_tk
        self.lbl_img_Daphne.pack()
        self.lbl_img_Daphne.place(x=100,y=435)
        
        img_Fred= Image.open("Fred.png")  
        img_Fred_tk = ImageTk.PhotoImage(img_Fred)
        self.lbl_img_Fred = tk.Label(master, image=img_Fred_tk)
        self.lbl_img_Fred.image = img_Fred_tk
        self.lbl_img_Fred.pack()
        self.lbl_img_Fred.place(x=100,y=555)
        
        #Personajes
        
        img_Cocina = Image.open("Cocina.png")  
        img_Cocina_tk = ImageTk.PhotoImage(img_Cocina)
        self.lbl_img_Cocina = tk.Label(master, image=img_Cocina_tk)
        self.lbl_img_Cocina.image = img_Cocina_tk
        self.lbl_img_Cocina.pack()
        self.lbl_img_Cocina.place(x=345,y=115)
        
        img_Biblioteca = Image.open("Biblioteca.png")  
        img_Biblioteca_tk = ImageTk.PhotoImage(img_Biblioteca)
        self.lbl_img_Biblioteca = tk.Label(master, image=img_Biblioteca_tk)
        self.lbl_img_Biblioteca.image = img_Biblioteca_tk
        self.lbl_img_Biblioteca.pack()
        self.lbl_img_Biblioteca.place(x=345,y=230)
                    
        img_Castillo = Image.open("Castillo.png")  
        img_Castillo_tk = ImageTk.PhotoImage(img_Castillo)
        self.lbl_img_Castillo = tk.Label(master, image=img_Castillo_tk)
        self.lbl_img_Castillo.image = img_Castillo_tk
        self.lbl_img_Castillo.pack()
        self.lbl_img_Castillo.place(x=345,y=345)
        
        img_Muelle = Image.open("Muelle.png")  
        img_Muelle_tk = ImageTk.PhotoImage(img_Muelle)
        self.lbl_img_Muelle = tk.Label(master, image=img_Muelle_tk)
        self.lbl_img_Muelle.image = img_Muelle_tk
        self.lbl_img_Muelle.pack()
        self.lbl_img_Muelle.place(x=345,y=460)
        
        img_Sotano = Image.open("Sotano.png")  
        img_Sotano_tk = ImageTk.PhotoImage(img_Sotano)
        self.lbl_img_Sotano = tk.Label(master, image=img_Sotano_tk)
        self.lbl_img_Sotano.image = img_Sotano_tk
        self.lbl_img_Sotano.pack()
        self.lbl_img_Sotano.place(x=345,y=575)
        
        #Personajes
        
        img_Cocina = Image.open("Espada.png")  
        img_Cocina_tk = ImageTk.PhotoImage(img_Cocina)
        self.lbl_img_Cocina = tk.Label(master, image=img_Cocina_tk)
        self.lbl_img_Cocina.image = img_Cocina_tk
        self.lbl_img_Cocina.pack()
        self.lbl_img_Cocina.place(x=640,y=170)
        
        img_Biblioteca = Image.open("Lupa.png")  
        img_Biblioteca_tk = ImageTk.PhotoImage(img_Biblioteca)
        self.lbl_img_Biblioteca = tk.Label(master, image=img_Biblioteca_tk)
        self.lbl_img_Biblioteca.image = img_Biblioteca_tk
        self.lbl_img_Biblioteca.pack()
        self.lbl_img_Biblioteca.place(x=640,y=266)
                    
        img_Castillo = Image.open("Antorcha.png")  
        img_Castillo_tk = ImageTk.PhotoImage(img_Castillo)
        self.lbl_img_Castillo = tk.Label(master, image=img_Castillo_tk)
        self.lbl_img_Castillo.image = img_Castillo_tk
        self.lbl_img_Castillo.pack()
        self.lbl_img_Castillo.place(x=640,y=362)
        
        img_Muelle = Image.open("Red.png")  
        img_Muelle_tk = ImageTk.PhotoImage(img_Muelle)
        self.lbl_img_Muelle = tk.Label(master, image=img_Muelle_tk)
        self.lbl_img_Muelle.image = img_Muelle_tk
        self.lbl_img_Muelle.pack()
        self.lbl_img_Muelle.place(x=640,y=458)
        
        img_Sotano = Image.open("Pocion.png")  
        img_Sotano_tk = ImageTk.PhotoImage(img_Sotano)
        self.lbl_img_Sotano = tk.Label(master, image=img_Sotano_tk)
        self.lbl_img_Sotano.image = img_Sotano_tk
        self.lbl_img_Sotano.pack()
        self.lbl_img_Sotano.place(x=640,y=594)

    def cerrar_ventana(self):
        self.master.destroy()


                
if __name__ == "__main__":
    
    # Crear la ventana inicio <principal>
    ventana_inicio = tk.Tk()
    ventana_inicio.geometry("800x695+0+0")
    ventana_inicio.title("Personajes")
 

    # Crear una instancia de ventana_inicio
    ventana1 = Ventana1_MostrarPers(ventana_inicio)
    
    # Crear una ventana secundaria a partir de la de inicio
    ventana_preg =  tk.Toplevel(ventana_inicio)
    ventana_preg.geometry("560x695+801+0")
    ventana_preg.title("Trama Pregustas")
 

    # Crear una instancia de ventana_preg
    ventana2 = Ventana2_DTrama(ventana_preg, ventana_inicio)
    
    
    ventana_inicio.mainloop()

    