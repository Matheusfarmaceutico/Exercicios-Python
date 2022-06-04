def contador(sem_digitos):
    lista = []
    for v in sem_digitos:
        v = int(v)
        lista.append(v * len(sem_digitos))
    return lista
        


contador("04252011000110")