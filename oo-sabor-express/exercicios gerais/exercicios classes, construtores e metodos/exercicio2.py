class Livro:
    def __init__(self, titulo, autor, ano_publicacao):   
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
    
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("A Revolução dos Bichos", "George Orwell", 1945)

print(livro1)
print(livro2)