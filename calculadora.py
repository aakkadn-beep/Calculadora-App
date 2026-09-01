import tkinter as tk
from tkinter import messagebox


#========================================================================================
def Sumar(a, b):
    return a + b

def Restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return a / b
#========================================================================================
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

    def calcular_resultado(self, segundo_operando):
        """Evalúa la operación según el operador guardado usando match case"""
        match self.operador:
            case '+':
                return Sumar(self.primer_operando, segundo_operando)
            case '-':
                return Restar(self.primer_operando, segundo_operando)
            case '*':
                return Multiplicar(self.primer_operando, segundo_operando)
            case '/':
                return Dividir(self.primer_operando, segundo_operando)
            case _:
                return segundo_operando

    def procesar_evento(self, char):
        # Evaluación principal del evento mediante Match Case
        match char:
            case 'C':
                self.expresion = ""
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "0")
                self.nuevo_numero = True

            case '.':
                texto_actual = self.pantalla.get()
                if self.nuevo_numero:
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, "0.")
                    self.nuevo_numero = False
                elif "." not in texto_actual:
                    self.pantalla.insert(tk.END, ".")

            case '+' | '-' | '*' | '/':
                self.primer_operando = float(self.pantalla.get())
                self.operador = char
                self.nuevo_numero = True

            case '=':
                if hasattr(self, 'operador') and hasattr(self, 'primer_operando'):
                    try:
                        segundo_operando = float(self.pantalla.get())
                        res = self.calcular_resultado(segundo_operando)

                        if res.is_integer():
                            res = int(res)

                        self.pantalla.delete(0, tk.END)
                        self.pantalla.insert(0, str(res))
                        self.nuevo_numero = True
                        del self.operador

                    except ZeroDivisionError as e:
                        self.pantalla.delete(0, tk.END)
                        self.pantalla.insert(0, "Error")
                        messagebox.showerror("Error Matemático", str(e))
                        self.nuevo_numero = True
                    except ValueError:
                        self.pantalla.delete(0, tk.END)
                        self.pantalla.insert(0, "Error")

            case _ if char.isdigit():
                if self.pantalla.get() == "0" or self.nuevo_numero:
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, char)
                    self.nuevo_numero = False
                else:
                    self.pantalla.insert(tk.END, char)
