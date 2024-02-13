class Carro():
    #metodo constructor
    def __init__(self, placa, tipo_de_vehiculo):
    
        self.placa = placa
        self.tipo_de_vehiculo = tipo_de_vehiculo

    #metodo constructor
    

class Cliente():
    
    def __init__(self, nombre, documento_identidad, contacto, lista_carros):
    
        self.nombre = nombre 
        self.documento_identidad = documento_identidad 
        self.contacto = contacto
        self.lista_carros = lista_carros
    
    def addCar(self,car):
        self.lista_carros.append(car)
        
    def listCar(self):
        for i in self.lista_carros:
            print("carro con placas:"+ i.placa)
            
class Cupo():
    def __init__(self, letra):
        self.letra = letra
        
class Pago():
    
    def __init__ (self,
                  fecha_inicio,
                  hora_inicio,
                  fecha_fin,
                  hora_fin,
                  valor,
                  carro,
                  cupo,
                  nombre_empleado):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.valor = valor
        self.carro = carro
        self.cupo = cupo
        self.nombre_empleado = nombre_empleado
        
class Empleado():
    
    def __init__(self,
                 nombre_empleado,
                 id_empleado):
        self.nombre_empleado = nombre_empleado
        self.id_empleado = id_empleado
        
"""
    from app.entities import Carro, Cliente, Cupo, Pago, Empleado
    carrito1 = Carro("OKL 712","Camioneta") 
    carrito2 = Carro("POR 162","Deportio")
    cliente1 = Cliente("Pablo Rivas Alfonso",1116542549,3133585900,[carrito1, carrito2])
    cliente2 = Cliente("Pedro Hernandez higuera",1178382312,3148762531,lista_carros=[])
    cupo1 = Cupo("A") 
    cupo2 = Cupo("B")
    empleado1 = ("Ricardo Orjuela",7728)  
    empleado2 = ("Carlos Ortiz",7729)
    pago1 = Pago("12/09/2024","12:30PM","24/09/2024","09:14AM","86000",cliente1.lista_carros[0],cupo1,empleado1)
    pago2 = Pago("09/07/2024","08:18AM","12/08/2024","02:47PM","103000",cliente1.lista_carros[1],cupo2,empleado2)
"""