def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) -1
    print(f"valor de derecha {der}")

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

def main():
    while True:
        lista_str = input("Dame una lista ordenada ([[]] para terminar): ")
        if lista_str == "[[]]":
            break
        lista = list(map(int, lista_str.strip("[]").split(",")))
        x = int(input("¿Valor buscado?: "))
        resultado = busqueda_binaria(lista, x)
        print(f"El valor se encuentra en el indice: {resultado}")
main()