from musico import Musico
from album import Album

class Banda:
    
#adicionar
   def __init__(self, nome):
       self.nome = nome
       self.musicos = []
       self.albuns = []

   def adicionar_musico(self, musico):
       self.musicos.append(musico)

   def adicionar_album(self, album):
       self.albuns.append(album)

#mostrar 
   def mostrar_musicos(self):
        print(f'Banda: {self.nome}') 
        for musico in self.musicos: 
            musico.mostrar_info()

   def mostrar_albuns(self):
        print(f'Album: {self.nome}') 
        for album in self.albuns: 
            album.mostrar_info()


#remover
   def remover_musico(self, opcao):
      self.musicos.pop(opcao) 

   def remover_album(self, opcao):
      self.albuns.pop(opcao)     
   
   def lista_musicos (self):
      lista = []
      index = 0
      for musico in self.musicos:
         nome = musico.nome
         nome_final = str(index) + '. ' + nome
         lista.append (nome_final)
         index +=1
      return lista

   def lista_album (self):
      lista = []
      index = 0
      for album in self.albuns:
         nome = album.titulo
         nome_final = str(index) + '. ' + nome
         lista.append (nome_final)
         index +=1
      return lista
      


   



    