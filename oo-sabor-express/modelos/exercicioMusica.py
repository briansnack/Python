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
    
musica = Musica("Starway to heaven", "Led Zeppelin", 7.39)
Musica.listar_musicas()
