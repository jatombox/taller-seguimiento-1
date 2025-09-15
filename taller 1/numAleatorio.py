import tkinter as tk
from tkinter import messagebox
import random

icono="numeros.ico"

# --- Generar número aleatorio ---
numero_secreto = random.randint(1, 100)

# --- Función para comprobar ---
def comprobar():
    try:
        intento = int(entrada.get())
        if intento < 1 or intento > 100:
            messagebox.showwarning("Aviso", "Debes ingresar un número entre 1 y 100.")
        elif intento == numero_secreto:
            messagebox.showinfo("¡Correcto!", f"🎉 ¡Adivinaste! El número era {numero_secreto}")
        elif intento < numero_secreto:
            messagebox.showinfo("Pista", "El número es más grande.")
        else:
            messagebox.showinfo("Pista", "El número es más pequeño.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

def salir():
    """
    cierra la aplicacion
    """
    ventana.quit()

def mostrar_info():
    """
    mostrar ayuda
    """
    messagebox.showinfo(
        "Ayuda",
        "programa simple para adivinar el numero aleatorio"
    )

def mostrar_ayuda():
    """abrir ventana con markdown"""
    nueva=Toplevel(ventana)
    nueva.title("acerca de la calculadora")
    nueva.geometry("500x300")

   #c
    etiqueta_instruccion=tk.Label(
        nueva, text="Crado por: Jacobo Morales\nVersion 1.0\n2025")
    etiqueta_instruccion.pack(pady=10)


# --- Interfaz con Tkinter ---
ventana = tk.Tk()
ventana.title("Reto 2: Adivina el Número")
ventana.geometry("400x200")

# configurar el icono de la ventana
try:
    ventana.iconbitmap(icono)
except tk.TclError:
    print(
        f"Advertencia No se pudo cargar el icono desde: {icono}")
    
# --Menu desplegable--
barra_menu=tk.Menu(ventana)

# Menu archivo

menu_archivo=tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menu ayuda

menu_ayuda=tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Mostrar ayuda", command=mostrar_info)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# asignar la barra de menu a la ventana

ventana.config(menu=barra_menu)

# Etiqueta
etiqueta = tk.Label(ventana, text="Adivina un número entre 1 y 100.\nEl sistema genera un número aleatorio.")
etiqueta.pack(pady=10)

# Entrada
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Adivinar", command=comprobar)
boton.pack(pady=10)

ventana.mainloop()