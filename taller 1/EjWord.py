import tkinter as tk
from tkinter import messagebox,Toplevel

icono="cocina.ico"

# Clase Receta para almacenar nombre y lista de ingredientes
class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

# Clase GestorRecetas para gestionar las recetas
class GestorRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        except IndexError:
            return None

# Función para agregar una nueva receta
def agregar_receta():
    nombre = entry_nombre.get()
    ingredientes = entry_ingredientes.get().split(",")
    
    if nombre and ingredientes:
        gestor.agregar_receta(nombre, ingredientes)
        listbox_recetas.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)
        entry_ingredientes.delete(0, tk.END)
        messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente.")

# Función para mostrar los ingredientes de una receta seleccionada
def ver_ingredientes():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        receta = gestor.recetas[indice]
        ingredientes = ", ".join(receta.ingredientes)
        messagebox.showinfo(f"Ingredientes de {receta.nombre}", f"{ingredientes}")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para ver sus ingredientes.")

# Función para eliminar una receta seleccionada
def eliminar_receta():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        nombre = gestor.eliminar_receta(indice)
        if nombre:
            listbox_recetas.delete(indice)
            messagebox.showinfo("Receta eliminada", f"La receta '{nombre}' ha sido eliminada.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la receta.")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para eliminar.")

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
        "programa para registrar multiples recetas con sus ingredientes"
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

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Recetas")

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

# Instancia del gestor de recetas
gestor = GestorRecetas()

# Etiquetas y entradas para el nombre y los ingredientes
label_nombre = tk.Label(ventana, text="Nombre de la receta:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_ingredientes = tk.Label(ventana, text="Ingredientes (separados por coma):")
label_ingredientes.pack()
entry_ingredientes = tk.Entry(ventana)
entry_ingredientes.pack()

# Botón para agregar receta
btn_agregar = tk.Button(ventana, text="Agregar receta", command=agregar_receta)
btn_agregar.pack()

# Listbox para mostrar las recetas guardadas
listbox_recetas = tk.Listbox(ventana)
listbox_recetas.pack()

# Botones para ver y eliminar recetas
btn_ver = tk.Button(ventana, text="Ver ingredientes", command=ver_ingredientes)
btn_ver.pack()

btn_eliminar = tk.Button(ventana, text="Eliminar receta", command=eliminar_receta)
btn_eliminar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
