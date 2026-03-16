import tkinter as tk
from tkinter import messagebox

from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):

        self.servicio = GarajeServicio()

        root.title("Sistema de Gestión de Garaje")

        # Labels
        tk.Label(root, text="Placa").grid(row=0, column=0)
        tk.Label(root, text="Marca").grid(row=1, column=0)
        tk.Label(root, text="Propietario").grid(row=2, column=0)

        # Entradas
        self.placa = tk.Entry(root)
        self.marca = tk.Entry(root)
        self.propietario = tk.Entry(root)

        self.placa.grid(row=0, column=1)
        self.marca.grid(row=1, column=1)
        self.propietario.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Agregar Vehículo", command=self.agregar).grid(row=3, column=0)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=3, column=1)

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=4, column=0, columnspan=2)

    def agregar(self):

        placa = self.placa.get()
        marca = self.marca.get()
        propietario = self.propietario.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo(placa, marca, propietario)

        self.servicio.agregar_vehiculo(vehiculo)

        self.lista.insert(tk.END, vehiculo)

        self.limpiar()

    def limpiar(self):

        self.placa.delete(0, tk.END)
        self.marca.delete(0, tk.END)
        self.propietario.delete(0, tk.END)