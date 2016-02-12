
from random import randint


def generate_random_list(a, b):
    """Xenera unha lista de 'a' enteiros entre 0 e 'b'  """
    l = []
    for ent in range(0, a):
        l.append(randint(0, b))
    return l


def verify_sort(l):
    """Verifica si unha lista está ordenada """
    for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


def insert_sort(l):
    """Ordenación por inserción """
    s = []
    for e in l:
        t = 0
        while(t <= len(s)):
            if (t == len(s)):
                s.append(e)
                break
            elif(e < s[t]):
                s.insert(t, e)
                break
            else:
                t += 1
    return s


def selection_sort(l):
    """Ordenación por selección """
    s = []
    while(l):
        minimo = l[0]
        for d in l:
            if d < minimo:
                minimo = d
        s.append(minimo)
        l.remove(minimo)
    return s


def shell_sort(l):
    raise NotImplementedError


def quicksort(l):
    raise NotImplementedError
