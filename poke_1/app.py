# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. hacer
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio. hacer
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck", "Eevee", "Gengar", "Mewtwo", "Vaporeon"]
        self.lista_poder_pokemones = [80, 150, 70, 90, 60, 100, 75, 120, 180, 95]
        self.lista_tipo_pokemones = ["eléctrico", "fuego", "planta", "agua", "normal", "agua", "normal", "fantasma", "psíquico", "agua"]


    def btn_mostrar_informe_1(self):
        # B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
        i = 0
        
        for i, nombre_pokemon in enumerate(self.lista_nombre_pokemones):
            print(f"{i} - {nombre_pokemon}")
            i += 1
        # 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        contador_poder = 0
        for indice, tipo in enumerate(self.lista_tipo_pokemones):
            
            if tipo == "fuego":
                poder_mas_10 = self.lista_poder_pokemones[indice] * 1.1 

                if poder_mas_10 > 100:
                    contador_poder += 1

        print(f"La cantidad de pokemones de tipo fuego que su poder supera los 100 es: {contador_poder}")

                
    
        # 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
        # contador_poder = 0
        # for indice, tipo in enumerate(self.lista_tipo_pokemones):
            
        #     if tipo == "electrico":
        #         poder_menos_15 = self.lista_poder_pokemones[indice] * 0.85 

        #         if poder_menos_15 > 100 and poder_menos_15 < 150:
        #             contador_poder += 1

        # print(f"La cantidad de pokemones de tipo electrico que su poder esta entre los 100 y los 150 es: {contador_poder}")
            
    
    def btn_mostrar_informe_2(self):
        # indicar el maximo de algo en un tipo de lista
        #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
        maximo_poder_electrico = None
        indice_poder_maximo_electrico = None
        for i, nombre_pokemon in enumerate(self.lista_nombre_pokemones):
            if elemento_pokemon == "eléctrico":
                poder_pokemones = self.lista_poder_pokemones[i]
                print(elemento_pokemon, poder_pokemones)

                if maximo_poder_electrico == None or poder > maximo_poder_electrico:
                    maximo_poder_electrico = poder_pokemones
                    indice_poder_maximo_electrico = i

        if maximo_poder_electrico != None:
            poder = self.lista_poder_pokemones[indice_poder_maximo_electrico]
            tipo = self.lista_tipo_pokemones[indice_poder_maximo_electrico]
            nombre = self.lista_nombre_pokemones[indice_poder_maximo_electrico]
            print()
        else: 
            print("no exite un maximo de electrico")    
            
        #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
        # contador_agua = self.lista_tipo_pokemones.count("agua")
        # contador_psiquico = self.lista_tipo_pokemones.count("psiquico")
        # contador_electrico = self.lista_tipo_pokemones.count("electrico")
        # contador_planta = self.lista_tipo_pokemones.count("planta")
        # contador_fantasma = self.lista_tipo_pokemones.count("fantasma")
        # contador_normal = self.lista_tipo_pokemones.count("normal")
        # contador_fuego = self.lista_tipo_pokemones.count("fuego")

        # print(f"""- Agua: {contador_agua} \n- Psiquico: {contador_psiquico} \n- Electrico: {contador_electrico} \n- Planta: {contador_planta} \n- Fantasma: {contador_fantasma} \n- Normal: {contador_normal} \n- Fuego: {contador_fuego} """)

        # lista_tipos_pokemones = [
        # contador_agua,
        # contador_psiquico,
        # contador_electrico,
        # contador_planta,
        # contador_fantasma,
        # contador_normal,
        # contador_fuego
        # ]

        # maxima_cantidad = 0
        # tipo = ""
        # for i, cantidad in enumerate(lista_tipos_pokemones):

        #     if maxima_cantidad == 0 or cantidad > maxima_cantidad:
        #         maxima_cantidad = cantidad

        #         match i:
        #             case 0:
        #                 tipo = "agua"
        #             case 1:
        #                 tipo = "psiquico"
        #             case 2:
        #                 tipo = "electrico"
        #             case 3:
        #                 tipo = "planta"
        #             case 4:
        #                 tipo = "fantasma"
        #             case 5:
        #                 tipo = "normal" 
        #             case 6:
        #                 tipo = "fuego"                           

        # print(f"El tipo maximo de tipo es: {tipo} - {maxima_cantidad}")
    def btn_mostrar_informe_3(self):
         suma = 0

         for poder in self.lista_poder_pokemones:
             suma += poder

         cantidad = len(self.lista_poder_pokemones)

         if cantidad == 0:
             print("Lista vacia")
         else:

             promedio = suma / cantidad
             print(f"Promedio = {promedio}")

             lista_nombres = []
             for i, poder in enumerate(self.lista_poder_pokemones):

                 if poder > promedio:
                     nombre = self.lista_nombre_pokemones[i]
                     poder = self.lista_poder_pokemones[i]
                     lista_nombres.append(nombre)
                     print(f"Nombre {nombre} | {poder}")

             for nombre in lista_nombres:
                 print(nombre)
    

        
    def btn_cargar_pokedex_on_click(self):
        for _ in range (10):
            nombre_pokemon = prompt("pokemon", "ingrese nombre del pokemon")
            while nombre_pokemon == None or not nombre_pokemon.isalpha():
                nombre_pokemon = prompt("pokemon", "ingrese nombre del pokemon nuevamente")
            elemento_pokemon = prompt("pokemon", "ingrese elemento del pokemon")
            while elemento_pokemon != "agua" and elemento_pokemon != "psíquico" and elemento_pokemon != "eléctrico":
               elemento_pokemon = prompt("pokemon", "ingrese elemento del pokemon") 
            poder_pokemones = prompt("pokemon", "ingrese el poder del pokemon")
            while poder_pokemones == None or not poder_pokemones.isdigit() or int(poder_pokemones) > 200 or int(poder_pokemones) < 50:
                poder_pokemones = prompt("pokemon", "ingrese el poder del pokemon nuevamente")
       
            self.lista_nombre_pokemones.append(nombre_pokemon)
            self.lista_poder_pokemones.append(poder_pokemones)
            self.lista_tipo_pokemones.append(elemento_pokemon)    

    
if __name__ == "__main__":
    app = App()
    app.mainloop()