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
                  cupo):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.valor = valor
        self.carro = carro
        self.cupo = cupo
        
