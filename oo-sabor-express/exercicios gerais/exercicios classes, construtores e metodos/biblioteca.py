import sys
sys.path.append(r'C:\Users\snack\Desktop\Python\oo-sabor-express\exercicios gerais\exercicios classes, construtores e metodos')

from exercicio4 import Livro

# 6) No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
dispoiveis_1949 = Livro.verificar_disponibilidade(1949)
for livro in dispoiveis_1949:
    print(livro)
