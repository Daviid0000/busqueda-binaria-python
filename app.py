import time
inicio = time.time()

def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) -1

    while izq <= der:
        medio = (izq+der)//2
        print(f"DEBUG: izq: {izq}, der: {der}, medio: {medio}")
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio-1
        else:
            izq = medio+1
    return -1

# Funcion para poner ejecutar la función de busqueda binaria
def main():
    while True:
        lista_str = input("Dame una lista ordenada, ejemplo: 1, 2, 3, 4, 5, 6, 7, 8, 9:")
        lista = list(map(int, lista_str.split(",")))
        if len(lista) < 2:
            print("La longitud de la lista no puede ser menor a 2")
            break
        x = int(input("¿Valor buscado?: "))
        resultado = busqueda_binaria(lista, x)
        if lista[resultado] == x:
            print(f"El valor se encuentra en el indice: {resultado}")
            break
        elif lista[resultado] != x:
            print("El valor no se encuentra en el lista")

main()

fin = time.time()

print(F"Tiempo de ejecución:{fin-inicio}")
