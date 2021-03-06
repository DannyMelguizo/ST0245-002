import numpy as np

class ArrayList:

    CAPACIDAD_DEFECTO = 10
    cantidad = 0
    lista = []

    def arrelgo(self):
        self.lista = np.zeros(self.CAPACIDAD_DEFECTO)

    def tamaño(self):
        return self.cantidad
    
    def añadir_final(self, var):
        self.lista.append(var)
        self.cantidad = self.cantidad + 1


    def posicion(self, i):
        return self.lista[i]

    def añadir_pos(self, pos, var):
        for i in range(pos, self.lista.size - 1):
            self.lista[i+1] = self.lista[i]

        self.lista.insert[pos, var]

    def del_var(self, var):
        self.lista.remove(var)