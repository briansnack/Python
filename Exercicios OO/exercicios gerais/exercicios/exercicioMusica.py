class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
        
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao}")
    
musica1 = Musica("Stairway to heaven", "Led Zeppelin", 7.39)
musica2 = Musica("Bohemian Rhapsody", "Queen", 5.55)
musica3 = Musica("Californication", "Red Hot Chili Peppers", 5.29)

Musica.listar_musicas()