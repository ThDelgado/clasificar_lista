mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15] 


#elimina elementos duplicados

def elimina_duplicados (a:list):
    mi_set = set(a)
    return (mi_set)

#convierte a lista
def convierte_lista (a:object):
    mi_lista = list(a)
    return mi_lista

#ordena de mayor a menor
def ascendente (a:list):
    a.sort()
    return a

print(ascendente(convierte_lista(elimina_duplicados(mi_lista))))