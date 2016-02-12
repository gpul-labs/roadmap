
# Exemplo de implementacion de una pila


def crear():
    return []


def tam(s):
    return len(s)


def apilar(s, e):
    s.append(e)


def desapilar(s):
    t = s[-1]
    del s[-1]
    return t


def cima(s):
    return s[-1]


def vacia(s):
    if len(s):
        return False
    else:
        return True
