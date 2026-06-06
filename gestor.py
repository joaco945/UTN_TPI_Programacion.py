import csv
import os


class Pais:

    def __init__(self, nombre, continente, poblacion, superficie):
        if not nombre or not continente or not poblacion or not superficie:
            raise ValueError("Campos obligatorios vacios")

        self.nombre = str(nombre).strip()
        self.continente = str(continente).strip()
        self.poblacion = int(poblacion)
        self.superficie = float(superficie)

    def __str__(self):
        return f"{self.nombre} ({self.continente}) - Pob: {self.poblacion} hab | Sup: {self.superficie} km2"


class GestorPaises:

    def __init__(self, ruta_csv="paises.csv"):
        self.ruta_csv = ruta_csv
        self.paises = {}
        self.cargar_desde_csv()

    def cargar_desde_csv(self):
        if not os.path.exists(self.ruta_csv):
            try:
                with open(
                    self.ruta_csv, mode="w", newline="", encoding="utf-8"
                ) as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        "nombre",
                        "poblacion",
                        "superficie",
                        "continente",
                    ])
            except Exception as e:
                print("No se pudo crear el archivo base:", e)
            return

        try:
            with open(self.ruta_csv, mode="r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    try:
                        nom = fila["nombre"].strip()
                        cont = fila["continente"].strip()
                        pob = int(fila["poblacion"])
                        sup = float(fila["superficie"])

                        nuevo = Pais(nom, cont, pob, sup)
                        self.paises[nom.lower()] = nuevo
                    except Exception:
                        continue
        except Exception as e:
            print("Error al leer el archivo:", e)

    def guardar_en_csv(self):
        try:
            with open(
                self.ruta_csv, mode="w", newline="", encoding="utf-8"
            ) as f:
                campos = ["nombre", "poblacion", "superficie", "continente"]
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                for p in self.paises.values():
                    escritor.writerow({
                        "nombre": p.nombre,
                        "poblacion": p.poblacion,
                        "superficie": p.superficie,
                        "continente": p.continente,
                    })
            return True
        except Exception as e:
            print("Error al escribir el archivo:", e)
            return False

    def agregar_pais(self, nombre, continente, poblacion, superficie):
        try:
            nuevo_pais = Pais(nombre, continente, poblacion, superficie)
        except ValueError as e:
            print("Error:", e)
            return False

        clave = nuevo_pais.nombre.lower()
        if clave in self.paises:
            print("El pais ya esta registrado.")
            return False
        self.paises[clave] = nuevo_pais
        self.guardar_en_csv()
        print("Pais fue registrado con exito.")
        return True
    
    def borrar_pais(self, nombre):
        clave = nombre.lower().strip()
        if clave in self.paises:
            del self.paises[clave]
            self.guardar_en_csv()
            print("El pais fue eliminado con exito.")
            return True
        else:
            print("El pais no fue encontrado.")
            return False


    def actualizar_datos(self, nombre, nueva_poblacion, nueva_superficie):
        pais_encontrado = self.paises.get(nombre.lower())

        if not pais_encontrado:
            print("Pais no encontrado.")
            return False

        try:
            pais_encontrado.poblacion = int(nueva_poblacion)
            pais_encontrado.superficie = float(nueva_superficie)
            self.guardar_en_csv()
            print("Datos actualizados.")
            return True
        except ValueError:
            print("Error: Los datos numericos no son validos.")
            return False

    def buscar_por_nombre(self, nombre_buscar):
        nombre_buscar = nombre_buscar.lower().strip()
        resultados = []
        for k, p in self.paises.items():
            if nombre_buscar in k:
                resultados.append(p)
        return resultados

    def filtrar_paises(
        self,
        continente=None,
        pob_min=None,
        pob_max=None,
        sup_min=None,
        sup_max=None,
    ):
        resultados = list(self.paises.values())

        if continente:
            resultados = [
                p
                for p in resultados
                if p.continente.lower() == continente.lower().strip()
            ]
        if pob_min is not None:
            resultados = [p for p in resultados if p.poblacion >= pob_min]
        if pob_max is not None:
            resultados = [p for p in resultados if p.poblacion <= pob_max]
        if sup_min is not None:
            resultados = [p for p in resultados if p.superficie >= sup_min]
        if sup_max is not None:
            resultados = [p for p in resultados if p.superficie <= sup_max]

        return resultados

    def ordenar_paises(self, criterio, descendente=False):
        lista_paises = list(self.paises.values())
        criterio = criterio.lower().strip()

        if criterio == "nombre":
            return sorted(
                lista_paises, key=lambda p: p.nombre, reverse=descendente
            )
        elif criterio == "poblacion":
            return sorted(
                lista_paises, key=lambda p: p.poblacion, reverse=descendente
            )
        elif criterio == "superficie":
            return sorted(
                lista_paises, key=lambda p: p.superficie, reverse=descendente
            )
        else:
            print("Criterio de ordenamiento no valido.")
            return lista_paises

    def mostrar_estadisticas(self):
        if not self.paises:
            print("No hay paises cargados para calcular estadisticas.")
            return

        lista = list(self.paises.values())

        pais_max_pob = max(lista, key=lambda p: p.poblacion)
        pais_min_pob = min(lista, key=lambda p: p.poblacion)

        promedio_pob = sum(p.poblacion for p in lista) / len(lista)
        promedio_sup = sum(p.superficie for p in lista) / len(lista)

        conteo_continentes = {}
        for p in lista:
            if p.continente in conteo_continentes:
                conteo_continentes[p.continente] += 1
            else:
                conteo_continentes[p.continente] = 1

        print("--- ESTADISTICAS DEL DATASET ---")
        print(
            f"El pais con mayor poblacion es: {pais_max_pob.nombre} ({pais_max_pob.poblacion} hab.)"
        )
        print(
            f"El pais con menor poblacion es: {pais_min_pob.nombre} ({pais_min_pob.poblacion} hab.)"
        )
        print(f"Promedio de poblacion general: {promedio_pob:.2f}")
        print(f"Promedio de superficie general: {promedio_sup:.2f}")
        print("Paises por continente:")
        for cont, cant in conteo_continentes.items():
            print(f" - {cont}: {cant}")
        print("-------------------")
