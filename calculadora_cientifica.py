import tkinter as tk
from math import *

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.config(bg='grey63')
        self.caja = tk.Entry(root, font=('System 20'), bg='dark olive green')
        self.caja.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        alto = 3
        ancho = 11
        
        # Colores
        color_numeros = 'light goldenrod yellow'
        color_operaciones = 'light coral'
        color_resto = 'light steel blue'
        
        # Botones
        self.botonE = tk.Button(self.root, text="e^x", width=ancho, height=alto, bg=color_resto, command=self.FuncionE)
        self.botonCero = tk.Button(self.root, text="0", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(0))
        self.botonPunto = tk.Button(self.root, text=".", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones('.'))
        self.botonInverso = tk.Button(self.root, text="1/x", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('**-1'))
        self.botonPorcen = tk.Button(self.root, text="%", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('%'))
        self.botonIgual = tk.Button(self.root, text="=", width=ancho, height=alto, bg=color_resto, command=self.igual)
        self.boton1 = tk.Button(self.root, text="1", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(1))
        self.boton2 = tk.Button(self.root, text="2", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(2))
        self.boton3 = tk.Button(self.root, text="3", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(3))
        self.botonMas = tk.Button(self.root, text="+", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('+'))
        self.botonMenos = tk.Button(self.root, text="-", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('-'))
        self.boton4 = tk.Button(self.root, text="4", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(4))
        self.boton5 = tk.Button(self.root, text="5", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(5))
        self.boton6 = tk.Button(self.root, text="6", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(6))
        self.botonMulti = tk.Button(self.root, text="*", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('*'))
        self.botonDivision = tk.Button(self.root, text="/", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('/'))
        self.boton7 = tk.Button(self.root, text="7", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(7))
        self.boton8 = tk.Button(self.root, text="8", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(8))
        self.boton9 = tk.Button(self.root, text="9", width=ancho, height=alto, bg=color_numeros, command=lambda: self.botones(9))
        self.botonDel = tk.Button(self.root, text="Del", width=ancho, height=alto, bg=color_operaciones, command=self.borrar_ultimo)
        self.botonAC = tk.Button(self.root, text="AC", width=ancho, height=alto, bg=color_operaciones, command=self.AC)
        self.botonIzquier = tk.Button(self.root, text="🢀", width=ancho, height=alto, bg=color_resto, command=self.flechaIz)
        self.botonDerecha = tk.Button(self.root, text="🢂", width=ancho, height=alto, bg=color_resto, command=self.flechaDer)
        self.botonRaiz = tk.Button(self.root, text="√", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('sqrt('))
        self.botonExponente = tk.Button(self.root, text="Exp", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('**'))
        self.botonLog = tk.Button(self.root, text="Log", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('log('))
        self.botonParentesis = tk.Button(self.root, text="(", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('('))
        self.botonParentesisII = tk.Button(self.root, text=")", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones(')'))
        self.botonTE4 = tk.Button(self.root, text="TE4splay!", width=ancho, height=alto, bg=color_resto, command=lambda: self.botones('TE4splay!'))

        self.colocar_botones()

    def colocar_botones(self):
        self.botonE.grid(row=1, column=4, padx=5, pady=5)
        self.botonParentesis.grid(row=1, column=1, padx=5, pady=5)
        self.botonParentesisII.grid(row=1, column=2, padx=5, pady=5)
        self.botonRaiz.grid(row=1, column=3, padx=5, pady=5)
        self.botonLog.grid(row=1, column=0, padx=5, pady=5)

        self.botonIzquier.grid(row=2, column=0, padx=5, pady=5)
        self.botonDerecha.grid(row=2, column=1, padx=5, pady=5)
        self.botonDivision.grid(row=2, column=2, padx=5, pady=5)
        self.botonMulti.grid(row=2, column=3, padx=5, pady=5)
        self.botonDel.grid(row=2, column=4, padx=5, pady=5)

        self.boton7.grid(row=3, column=0, padx=5, pady=5)
        self.boton8.grid(row=3, column=1, padx=5, pady=5)
        self.boton9.grid(row=3, column=2, padx=5, pady=5)
        self.botonMenos.grid(row=3, column=3, padx=5, pady=5)
        self.botonAC.grid(row=3, column=4, padx=5, pady=5)

        self.boton4.grid(row=4, column=0, padx=5, pady=5)
        self.boton5.grid(row=4, column=1, padx=5, pady=5)
        self.boton6.grid(row=4, column=2, padx=5, pady=5)
        self.botonMas.grid(row=4, column=3, padx=5, pady=5)
        self.botonExponente.grid(row=4, column=4, padx=5, pady=5)

        self.boton1.grid(row=5, column=0, padx=5, pady=5)
        self.boton2.grid(row=5, column=1, padx=5, pady=5)
        self.boton3.grid(row=5, column=2, padx=5, pady=5)
        self.botonInverso.grid(row=5, column=3, padx=5, pady=5)
        self.botonPorcen.grid(row=5, column=4, padx=5, pady=5)

        self.botonCero.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.botonPunto.grid(row=6, column=2, padx=5, pady=5)
        self.botonIgual.grid(row=6, column=3, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.botonTE4.grid(row=7, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    def botones(self, valor):
        pos = self.caja.index(tk.INSERT)
        self.caja.insert(pos, valor)

    def borrar_ultimo(self):
        pos = self.caja.index(tk.INSERT)
        if pos > 0:
            self.caja.delete(pos - 1, pos)

    def AC(self):
        self.caja.delete(0, tk.END)

    def flechaIz(self):
        index = self.caja.index(tk.INSERT)
        if index > 0:
            self.caja.icursor(index - 1)

    def flechaDer(self):
        index = self.caja.index(tk.INSERT)
        if index < len(self.caja.get()):
            self.caja.icursor(index + 1)

    def igual(self):
        try:
            ecuacion = self.caja.get()
            if "TE4splay!" in ecuacion:
                self.caja.delete(0, tk.END)
                self.caja.insert(0, "Error 404, UPM not found")
                return

            ecuacion = ecuacion.replace('e^', 'e**')  # Reemplazar e^x por e**x
            self.resultado = str(eval(ecuacion))
            self.caja.delete(0, tk.END)
            self.caja.insert(0, self.resultado)
        except Exception as e:
            self.caja.delete(0, tk.END)
            self.caja.insert(0, "Error")

    def FuncionE(self):
        pos = self.caja.index(tk.INSERT)
        self.caja.insert(pos, 'e**(')
        self.caja.icursor(pos + 4)  # Colocar el cursor después de 'e**('

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()
