class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        self.livros.append(titulo)

    def listar_livros(self):
        return self.livros

# Teste
def testar_biblioteca():
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro("Duna")
    biblioteca.adicionar_livro("Neuromancer")
    
    livros = biblioteca.listar_livros()
    assert "Duna" in livros
    assert "Neuromancer" in livros
    print("Testes de biblioteca passaram.")

testar_biblioteca()
