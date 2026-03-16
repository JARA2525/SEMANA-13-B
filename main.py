# Punto de entrada principal de la aplicación
# Integración final del sistema de gestión de garaje

import tkinter as tk
from ui.app_tkinter import AppGaraje


def main():

    root = tk.Tk()

    app = AppGaraje(root)

    root.mainloop()


if __name__ == "__main__":
    main()