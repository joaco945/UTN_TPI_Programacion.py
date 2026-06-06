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
        print("El campo no puede estar vacio.")


def mostrar_en_consola(lista):
    if not lista:
        print("Sin resultados para mostrar.")
        return
    print("Nombre               | Continente      | Poblacion       | Superficie")
    print("----------------------------------------------------------------------")
    for p in lista:
        print(
            f"{p.nombre:<20} | {p.continente:<15} | {p.poblacion:<15} | {p.superficie:<15}"
        )


def menu():
    gestor = GestorPaises()

    while True:
        print("""--- MENU PRINCIPAL ---
        1. Ver lista completa de paises
        2. Registrar un pais
        3. Modificar poblacion/superficie de un pais
        4. Buscar pais por nombre
        5. Filtrar paises
        6. Ordenar paises
        7. Ver reportes estadisticos
        8. Borrar un pais
        9. Salir del programa""")

        op = input("Elija una opcion (1-9): ").strip()

        if op == "1":
            mostrar_en_consola(list(gestor.paises.values()))

        elif op == "2":
            print("-- Carga del nuevo pais --")
            nom = leer_texto("Nombre: ")
            con = leer_texto("Continente: ")
            pob = leer_entero("Cantidad de habitantes: ")
            sup = leer_float("Superficie en km2: ")
            gestor.agregar_pais(nom, con, pob, sup)

        elif op == "3":
            print("-- Modificar datos --")
            nom = leer_texto("Nombre del pais a buscar: ")
            pob = leer_entero("Nueva poblacion: ")
            sup = leer_float("Nueva superficie: ")
            gestor.actualizar_datos(nom, pob, sup)

        elif op == "4":
            print("-- Busqueda exacta o parcial --")
            b = leer_texto("Buscar: ")
            res = gestor.buscar_por_nombre(b)
            mostrar_en_consola(res)

        elif op == "5":
            print("""-- Menu de filtros --
            1. Por Continente
            2. Por rango de Poblacion
            3. Por rango de Superficie""")
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
                print("Opcion de filtrado no valida.")

        elif op == "6":
            print("-- Menu de ordenamiento --")
            crit = leer_texto(
                "Criterio (nombre / poblacion / superficie): "
            ).lower()
            sentido = (
                input("¿Quiere ordenar de forma descendente? (S/N): ").strip().lower()
            )
            desc = True if sentido == "s" else False

            res_ordenado = gestor.ordenar_paises(criterio=crit, descendente=desc)
            mostrar_en_consola(res_ordenado)

        elif op == "7":
            gestor.mostrar_estadisticas()

        elif op == "8":
            print("-- Eliminar un pais --")
            nom = leer_texto("Nombre del pais que quiere eliminar: ")
            gestor.borrar_pais(nom)

        elif op == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, reintente por favor.")


if __name__ == "__main__":
    menu()
