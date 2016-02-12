

# Implementación de unha pila facendo uso de programacion orientada a
# obxectos.


class Stack:
    """Implementacion de unha pila facendo uso de obxectos """

    def __init__(self):
        self.items = []

    def vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def cima(self):
        if self.vacia():
            return []
        return self.items[-1]

    def desapilar(self):
        del self.items[-1]

    def tam(self):
        return len(self.items)
