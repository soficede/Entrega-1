
class Implantes:
    def __init__(self, medico, fecha, estado, cantidad, cedula):
        self.__medico = medico
        self.__fecha = fecha
        self.__estado = estado
        self.__cantidad = cantidad
        self.__cedula = cedula
    @property

    def medico(self):
        return self.__medico
    @medico.setter
    def medico(self, medico):
        self.__medico = medico
    @property

    def fecha(self):
        return self.__medico
    @fecha.setter
    def fecha(self,fecha):
        self.__fecha = fecha
    @property

    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self,estado):
        self.__estado = estado
    @property

    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
    @property

    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self,cedula):
        self.__cedula = cedula

class Protesiscadera(Implantes):
    def __init__(self,  medico, fecha, estado, cantidad, cedula, fijacion, tamaño, material):
        super().__init__( medico, fecha, estado, cantidad, cedula)
        self.__fijacion = fijacion
        self.__tamano = tamaño
        self.__material = material

    def __str__(self):
        return f"Prótesis cadera: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n fijacion:{self.fijacion} \n tamaño:{self.tamaño} \n material:{self.material}"
    @property

    def fijacion(self):
        return self.__fijacion
    @fijacion.setter

    def fijacion(self,fijacion):
        self.__fijacion = fijacion
    @property

    def tamaño(self):
        return self.__tamaño
    @tamaño.setter

    def tamaño(self,tamaño):
        self.__tamaño = tamaño
    @property

    def material(self):
        return self.__material
    @material.setter

    def material(self,material):
        self.__material = material

class Marcapasos(Implantes):
    def __init__(self,  medico, fecha, estado, cantidad, cedula, frecuencia, electrodos, alambrico):
        super().__init__(medico, fecha, estado, cantidad,cedula)
        self.__frecuencia = frecuencia
        self.__electrodos = electrodos
        self.__alambrico=alambrico

    def __str__(self):
        return f"Marcapasos: \n médico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n frecuencia:{self.frecuencia} \n #electrodos:{self.electrodos} \n alambrico:{self.alambrico}"
    @property

    def frecuencia(self):
        return self.__frecuencia
    @frecuencia.setter
    def frecuencia(self,frecuencia):
        self.__frecuencia = frecuencia
    @property

    def electrodos(self):
        return self.__electrodos
    @electrodos.setter
    def electrodos(self,electrodos):
        self.__electrodos = electrodos
    @property

    def alambrico(self):
        return self.__alambrico
    @alambrico.setter
    def alambrico(self,alambrico):
        self.__alambrico=alambrico

class Stents (Implantes):
    def __init__(self,  medico, fecha, estado, cantidad, cedula, longitud, diametro, material):
        super().__init__(medico, fecha, estado,cantidad,cedula)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__material = material

    def __str__(self):
        return f"Stents: \n médico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cédula:{self.cedula} \n longitud:{self.longitud} \n diametro:{self.diametro} \n material:{self.material}"
    @property

    def longitud(self):
        return self.__longitud
    @longitud.setter
    def longitud(self,longitud):
        self.__longitud=longitud
    @property

    def diametro(self):
        return self.__diametro
    @diametro.setter
    def diametro(self,diametro):
        self.__diametro=diametro
    @property

    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material=material

class ImplantesDentales(Implantes):
    def __init__(self,  medico, fecha, estado, cantidad, cedula, forma, sistfij, material):
        super().__init__(medico, fecha, estado, cantidad, cedula)
        self.__forma = forma
        self.__sistfij = sistfij
        self.__material = material

    def __str__(self):
        return f"Implantes_dentales: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n sistema de fijacion:{self.sistfij} \n forma:{self.forma} \n material:{self.material}"
    @property

    def forma(self):
        return self.__forma
    @forma.setter
    def material(self,forma):
        self.__forma = forma
    @property

    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material = material
    @property

    def sistfij(self):
        return self.__sistfij
    @sistfij.setter
    def material(self,sistfij):
        self.__sistfij = sistfij

class ProtesisRodilla(Implantes):
    def __init__(self,  medico, fecha, estado, cantidad, cedula, fijacion, tamaño, material):
        super().__init__( medico, fecha, estado, cantidad, cedula)
        self.__fijacion = fijacion
        self.__tamaño = tamaño
        self.__material = material

    def __str__(self):
        return f"ProtesisRodilla: \n médico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cédula:{self.cedula} \n tipo de fijación:{self.fijacion} \n tamaño:{self.tamaño} \n material:{self.material}"
    @property

    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material = material
    @property

    def tamaño(self):
        return self.__tamaño
    @tamaño.setter
    def tamaño(self,tamaño):
        self.__tamaño = tamaño
    @property

    def fijacion(self):
        return self.__fijacion
    @fijacion.setter
    def fijacion(self,fijacion):
        self.__fijacion = fijacion

class Sistema():
    def __init__(self):
        self.implantes=[]

    def agregar_implante(self,implante):
        self.implantes.append(implante)

    def ver_implante(self):
        if not self.implantes:
            print("No hay implantes registrados.")
            return
        
        for i, implante in enumerate(self.implantes, 1):
            print(f"implante #{i}:")
            print(implante)
            print("-" * 40)

    def actualizar_implante(self, indice, implante_actualizado):
        if indice >= 0 and indice < len(self.implantes):
            self.implantes[indice] = implante_actualizado
            print(f"implante #{indice + 1} actualizado:")
            print(implante_actualizado)
        else:
            print("Índice de implante no válido.")

    def eliminar_implante(self, indice):
        if indice >= 0 and indice < len(self.implantes):
            implante_eliminado = self.implantes.pop(indice)
            print(f"Implante #{indice + 1} eliminado:")
            print(implante_eliminado)
        else:
            print("Índice de implante no válido.")