class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_todos_livros(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            print(f"- {livro.titulo}")

    def buscar_livros_por_autor(self, autor):
        livros_do_autor = [livro.titulo for livro in self.livros if livro.autor == autor]
        if livros_do_autor:
            print(f"Livros de {autor}:")
            for livro in livros_do_autor:
                print(f"- {livro}")
        else:
            print(f"Não foram encontrados livros do autor {autor}.")

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling")
livro2 = Livro("Código Limpo", "Robert Cecil Martin")
livro3 = Livro("O Mar de Monstros", "Rick Riordan")
livro4 = Livro("Harry Potter e o Prisioneiro de Azkaban", "J. K. Rowling")
livro5 = Livro("O Ladrão de Raios", "Rick Riordan")
livro6 = Livro("Harry Potter e a Câmara Secreta", "J. K. Rowling")


biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)
biblioteca.adicionar_livro(livro5)
biblioteca.adicionar_livro(livro6)

biblioteca.listar_todos_livros()

autor_procurado = input("Digite o nome do autor: ")
biblioteca.buscar_livros_por_autor(autor_procurado)