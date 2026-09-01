import tkinter as tk
from tkinter import messagebox

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora - App")
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        
        self.expresion = ""
        self.nuevo_numero = True

        # Pantalla de visualización 
        self.pantalla = tk.Entry(
            root, font=("Arial", 20), justify="right", bd=10, insertwidth=4, width=14
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=15)
        self.pantalla.insert(0, "0")

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('C', 1, 0), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
        ]

        for (texto, fila, columna) in botones:
            ancho = 3 if texto != '0' else 7
            colspan = 1 if texto != '0' else 2
            
            bg_color = "#e0e0e0"
            if texto in ['+', '-', '*', '/', '=']:
                bg_color = "#ff9800"
            elif texto == 'C':
                bg_color = "#f44336"

            btn = tk.Button(
                self.root, text=texto, font=("Arial", 14, "bold"),
                width=ancho, height=2, bg=bg_color,
                command=lambda t=texto: self.procesar_evento(t)
            )
            btn.grid(row=fila, column=columna, columnspan=colspan, padx=3, pady=3, sticky="nsew")
