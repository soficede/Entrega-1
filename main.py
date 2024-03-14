#MAIN
from ClasesFunciones import *
sistema = Sistema()

while True:
    menu = int(input("""Ingrese la opcion que dese seleccionar:
    1. Ingresar un nuevo implante
    2. Eliminar implante
    3. Editar información del implante 
    4. Visualizar el inventario completo
    5. Salir del sistema
    """))

    if menu == 1: #Ingresar nuevo implante
        tipoimp = int(input("""Ingrese el implante a ingresar:
        1. Prótesis cadera
        2. Marcapasos cardíacos
        3. Stents coronarios
        4. Implantes dentales
        5. Prótesis de rodilla
        :  """))

        if tipoimp == 1: #Prótesis cadera
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            fijacion = input("Ingrese tipo de fijación:")
            tamaño = input("Ingrese tamaño:")
            material = input("Ingrese material:")

            protesisc = Protesiscadera(medico, fecha, estado, cantidad, cedula, fijacion, tamaño, material)
            sistema.agregar_implante(protesisc)

        elif tipoimp == 2: #Marcapasos cardíacos
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            frecuencia = input("Ingrese frecuencia de estimulación: ")
            electrodos = input("Ingrese número de electrodos: ")
            alambrico = input("ingrese si es alambrico o inalambrico: ")

            marcap = Marcapasos(medico, fecha, estado, cantidad, cedula, frecuencia, electrodos, alambrico)
            sistema.agregar_implante(marcap)

        elif tipoimp == 3: #Stens coronarios
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            longitud = input("Ingrese longitud :")
            diametro = input("Ingrese diametro:")
            material = input("Ingrese material:")

            stens = Stents(medico, fecha, estado, cantidad, cedula, longitud, diametro, material)
            sistema.agregar_implante(stens)

        elif tipoimp == 4: #Implantes dentales
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            forma = input("Ingrese forma: ")
            sistfij = input("Ingrese sistema de fijacion: ")
            material = input("Ingrese material: ")

            implantes = ImplantesDentales(medico, fecha, estado, cantidad, cedula, forma, sistfij, material)
            sistema.agregar_implante(implantes)

        elif tipoimp == 5: #Prótesis de rodilla
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            fijacion = input("Ingrese tipo de fijación:")
            tamaño = input("Ingrese tamaño:")
            material = input("Ingrese material:")

            protesisr = ProtesisRodilla(medico, fecha, estado, cantidad, cedula, fijacion, tamaño, material)
            sistema.agregar_implante(protesisr)

        else:
            continue

    elif menu == 2: #Eliminar implante
        ti = int(input("Ingrese índice de implante a eliminar tomando el cero como posición 1"))
        sistema.eliminar_implante(ti)

    elif menu == 3: #Editar info del implante
        indice = int(input("Ingrese índice de implante a modificar tomando el cero como posición 1"))
        nuevo_implante = int(input("""Ingrese el implante a modificar:
        1. Prótesis cadera
        2. Marcapasos cardíacos
        3. Stents coronarios
        4. Implantes dentales
        5. Prótesis de rodilla
        :  """))

        if nuevo_implante == 1: #Prótesis cadera
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            fijacion = input("Ingrese tipo de fijación:")
            tamaño = input("Ingrese tamaño:")
            material = input("Ingrese material:")

            protesisc = Protesiscadera(medico, fecha, estado, cantidad, cedula, fijacion, tamaño, material)
            sistema.actualizar_implante(indice,protesisc)

        elif nuevo_implante == 2: #Marcapasos cardíacos
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            frecuencia = input("Ingrese frecuencia de estimulación: ")
            electrodos = input("Ingrese número de electrodos: ")
            alambrico = input("ingrese si es alambrico o inalambrico: ")

            marcap = Marcapasos(medico, fecha, estado, cantidad, cedula, frecuencia, electrodos, alambrico)
            sistema.actualizar_implante(indice,marcap)

        elif nuevo_implante == 3: #Stents coronarios
            edico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            longitud = input("Ingrese longitud :")
            diametro = input("Ingrese diametro:")
            material = input("Ingrese material:")

            stens = Stents(medico, fecha, estado, cantidad, cedula, longitud, diametro, material)
            sistema.actualizar_implante(indice,stens)

        elif nuevo_implante == 4: #Implantes dentales
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            forma = input("Ingrese forma: ")
            sistfij = input("Ingrese sistema de fijacion: ")
            material = input("Ingrese material: ")

            implantes = ImplantesDentales(medico, fecha, estado, cantidad, cedula, forma, sistfij, material)
            sistema.actualizar_implante(indice,implantes)

        elif nuevo_implante == 5: #Prótesis de rodilla
            medico = int(input("Ingrese número de identificación del medico responsable: "))
            fecha = input("Ingrese fecha:  ")
            estado = input("Ingrese estado del implante:")
            cantidad = input("Ingrese cantidad:")
            cedula = int(input("Ingrese la cédula del paciente"))

            fijacion = input("Ingrese tipo de fijación:")
            tamano = input("Ingrese tamaño:")
            material = input("Ingrese material:")

            protesisr = ProtesisRodilla(medico, fecha, estado, cantidad, cedula, fijacion, tamano, material)
            sistema.actualizar_implante(indice,protesisr)
        

    elif menu == 4: #Visualizar el inventario completo
        sistema.ver_implante()

    elif menu == 5: #Salir del sistema
        break

    else:
        print("Ingrese una opción")