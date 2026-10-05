max_tam = 10


def ingresar_valores(frente, final, cola, contador):
    if (final + 1) % max_tam == frente:
        print("Desbordamiento de la cola")
        return frente, final, cola, contador

    elemento = int(input("Ingrese un elemento para la cola: "))
    final = (final + 1) % max_tam
    cola[final] = elemento
    contador += 1
    print("Elemento", contador, "agregado a la cola: ", elemento)
    return frente, final, cola, contador


def eliminar_elemento(frente, final, contador):
    if frente == final:
        print("La cola esta vacia, no se puede eliminar")
        return frente, contador

    frente = (frente + 1) % max_tam
    contador -= 1
    print("Elemento eliminado de la cola.")
    return frente, contador


def imprimir(frente, final, cola):
    print("Elementos de la cola en el orden de ingreso: ")
    i = (frente + 1) % max_tam
    while i != (final + 1) % max_tam:
        print(" " + str(cola[i]))
        i = (i + 1) % max_tam
    print()


def main():
    cola = [0] * max_tam
    contador = 0
    frente = 0
    final = 0

    respuesta = input("Desea agregar elementos a la cola? (s/n): ").lower()

    while respuesta == "s" and contador < 10:
        frente, final, cola, contador = ingresar_valores(
            frente, final, cola, contador
        )
        if contador < 10:
            respuesta = input(
                "Desea agregar mas elementos a la cola? (s/n): "
            ).lower()

    if frente == final:
        print("La cola esta vacia")
        return

    primer_elemento = cola[(frente + 1) % max_tam]
    print("El primer elemento de la cola es: ", primer_elemento)

    frente, contador = eliminar_elemento(frente, final, contador)
    imprimir(frente, final, cola)


if __name__ == "__main__":
    main()