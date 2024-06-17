# main.py
from banda import Banda
from musico import Musico
from banda import Album
from instrumento import Guitarra, Bateria,Microfone


# Criando instrumentos
guitarra = Guitarra('Fender Stratocaster', 'Cordas', 6)
bateria = Bateria('Yamaha Stage Custom', 'Percussão', 5)
microfone = Microfone('microfone', 'Vocal', 10)


# Criando músicos com instrumentos
musico1 = Musico('John', guitarra)
musico2 = Musico('Ringo', bateria)
musico3 = Musico('Vitinho', microfone)


# Criando banda e adicionando músicos
banda = Banda('The Beatles')
banda.adicionar_musico(musico1)
banda.adicionar_musico(musico2)




# criando album
album1 = Album('album_muito_loco', 1989, 8)
album2 = Album('vitinho', 1989, 8)
banda.adicionar_album(album1)
banda.adicionar_album(album2)



# Exibindo informações da banda e albuns
banda.mostrar_musicos()
banda.mostrar_albuns()





running = True
while(running):
    resposta=int(input("""clique 1 para adicionar musicos
clique 2 para adicionar album
clique 3 para remover musicos
clique 4 para remover albuns
clique 5 para sair da interface grafica
"""))
   
   
    if (resposta == 1):
        nome=str(input("nome do musico: "))
        instrumento_selecionado=str(input("selecionar instrumento: (Guitarra, Bateria, Micronfone): "))
        if (instrumento_selecionado == "guitarra"):
            novo_instrumento = Guitarra('Fender Stratocaster', 'Cordas', 6)
        if (instrumento_selecionado == "bateria"):
            novo_instrumento = Bateria('Yamaha Stage Custom', 'Percussão', 5)
        if (instrumento_selecionado == "microfone"):
            novo_instrumento = Microfone('microfone', 'Vocal', 10)
        novo_musico = Musico(nome,novo_instrumento)
        banda.adicionar_musico(novo_musico)


    if (resposta == 2):
        nome_album=str(input("nome do album: "))
        album_novo= Album(nome_album,1989, 8)
        banda.adicionar_album(album_novo)


    if (resposta == 3):
        lista = banda.lista_musicos()
        print(lista)
        opcao = int(input("numero do musico a se retirar: "))
        banda.remover_musico(opcao)
        lista = banda.lista_musicos()
        print(lista)
        

    if (resposta == 4):
        lista = banda.lista_album()
        print(lista)
        opcao = int(input("numero do album a se retirar: "))
        banda.remover_album(opcao)
        lista = banda.lista_album()
        print(lista)


    if (resposta == 5):
        running=False

print("""
      
      programa finalizado
      
      """)
banda.mostrar_musicos()
banda.mostrar_albuns()


        
    




