class Livro:
    def __init__(self, titulo, autor, ano_publicacao):   
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
    
    def emprestar(self):
        self.disponivel = False
        
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("A Revolução dos Bichos", "George Orwell", 1945)
livro3 = Livro("Python 1", "Samuel", 2019)

print(livro1)
print(livro2)
print(livro3)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")