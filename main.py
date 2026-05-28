from gestor import GestorPaises


def leer_entero(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if n > 0:
                return n
            print("Debe ser mayor a 0.")
        except ValueError:
            print("Dato invalido. Ingrese un numero entero.")


def leer_float(mensaje):
    while True:
        try:
            n = float(input(mensaje))
            if n > 0:
                return n
            print("Debe ser mayor a 0.")
        except ValueError:
            print("Dato invalido. Ingrese un numero decimal.")


def leer_texto(mensaje):
    while True:
        t = input(mensaje).strip()
        if t:
            return t
        print("El campo no puede quedar vacio.")


def mostrar_en_consola(lista):
    if not lista:
        print("Sin resultados para mostrar.")
        return
    print("\nNombre               | Continente      | Poblacion       | Superficie")
    print("-" * 75)
    for p in lista:
        print(
            f"{p.nombre:<20} | {p.continente:<15} | {p.poblacion:<15} | {p.superficie:<15}"
        )


def menu():
    gestor = GestorPaises()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ver lista completa de paises")
        print("2. Registrar un pais")
        print("3. Modificar poblacion/superficie de un pais")
        print("4. Buscar pais por nombre")
        print("5. Filtrar paises")
        print("6. Ordenar paises")
        print("7. Ver reportes estadisticos")
        print("8. Borrar un pais")
        print("9. Salir del programa")

        op = input("Seleccione una opcion (1-9): ").strip()

        if op == "1":
            mostrar_en_consola(list(gestor.paises.values()))

        elif op == "2":
            print("\n-- Carga de nuevo pais --")
            n = leer_texto("Nombre: ")
            c = leer_texto("Continente: ")
            p = leer_entero("Cantidad de habitantes: ")
            s = leer_float("Superficie en km2: ")
            gestor.agregar_pais(n, c, p, s)

        elif op == "3":
            print("\n-- Modificar datos --")
            n = leer_texto("Nombre del pais a buscar: ")
            p = leer_entero("Nueva poblacion: ")
            s = leer_float("Nueva superficie: ")
            gestor.actualizar_datos(n, p, s)

        elif op == "4":
            print("\n-- Busqueda exacta o parcial --")
            b = leer_texto("Buscar: ")
            res = gestor.buscar_por_nombre(b)
            mostrar_en_consola(res)

        elif op == "5":
            print("\n-- Menu de filtros --")
            print("1. Por Continente")
            print("2. Por rango de Poblacion")
            print("3. Por rango de Superficie")
            tipo = input("Opcion: ").strip()

            if tipo == "1":
                cont = leer_texto("Nombre del continente: ")
                mostrar_en_consola(gestor.filtrar_paises(continente=cont))
            elif tipo == "2":
                p_min = leer_entero("Poblacion minima: ")
                p_max = leer_entero("Poblacion maxima: ")
                mostrar_en_consola(
                    gestor.filtrar_paises(pob_min=p_min, pob_max=p_max)
                )
            elif tipo == "3":
                s_min = leer_float("Superficie minima: ")
                s_max = leer_float("Superficie maxima: ")
                mostrar_en_consola(
                    gestor.filtrar_paises(sup_min=s_min, sup_max=s_max)
                )
            else:
                print("Opcion de filtrado invalida.")

        elif op == "6":
            print("\n-- Menu de ordenamiento --")
            crit = leer_texto(
                "Criterio (nombre / poblacion / superficie): "
            ).lower()
            sentido = (
                input("¿Desea orden descendente? (S/N): ").strip().lower()
            )
            desc = True if sentido == "s" else False

            res_ordenado = gestor.ordenar_paises(criterio=crit, descendente=desc)
            mostrar_en_consola(res_ordenado)

        elif op == "7":
            gestor.mostrar_estadisticas()

        elif op == "8":
            print("\n-- Eliminar un pais --")
            n = leer_texto("Nombre del pais a borrar: ")
            gestor.borrar_pais(n)

        elif op == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, reintente.")


if __name__ == "__main__":
    menu()
