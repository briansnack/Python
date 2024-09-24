class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):   
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
        
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
    
    def emprestar(self):
        self.disponivel = False
        
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]  
        return livros_disponiveis
    
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("A Revolução dos Bichos", "George Orwell", 1945)
livro3 = Livro("Python 1", "Samuel", 2019)

Livro.livros = [livro1, livro2, livro3]