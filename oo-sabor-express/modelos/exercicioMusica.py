class Musica:
    nome = ""
    artista = ""
    duracao = int
    
musica1 = Musica()
musica1.nome = "Starway to heaven"
musica1.artista = "Led Zeppelin"
musica1.duracao = 7.39

# Minha resposta
# print(vars(musica1))

# Resposta curso
print(f"Música: {musica1.nome} - Banda: {musica1.artista} - Duração: {musica1.duracao}")