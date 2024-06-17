# instrumento.py
class Instrumento:
    def __init__(self, nome, tipo):
       self.nome = nome
       self.tipo = tipo

    def mostrar_info(self):
        print(f'        Instrumento: {self.nome}, Tipo: {self.tipo}')

class Guitarra(Instrumento):
    def __init__(self, nome, tipo, num_cordas):
       super().__init__(nome, tipo)
       self.num_cordas = num_cordas

    def mostrar_info(self):
       super().mostrar_info()
       print(f'         Número de Cordas: {self.num_cordas}')

class Bateria(Instrumento):
    def __init__(self, nome, tipo, num_tambores):
       super().__init__(nome, tipo)
       self.num_tambores = num_tambores

    def mostrar_info(self):
       super().mostrar_info()
       print(f'         Número de Tambores: {self.num_tambores}')

class Microfone(Instrumento):
    def __init__(self, nome, tipo, tamanho):
       super().__init__(nome, tipo)
       self.tamanho = tamanho

    def mostrar_info(self):
       super().mostrar_info()
       print(f'         Tamanho: {self.tamanho}')
 
 

