class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


livro1 = Livro("Orgulho e Preconceito", "Jane Austen", "1813")
livro2 = Livro("O Alquimista", "Paulo Coelho", "1988")
livro3 = Livro("1984", "George Orwell", "1949")

print(livro1.titulo, livro1.autor,  livro1.ano_publicacao)
print(livro2.titulo, livro2.autor,  livro2.ano_publicacao)
print(livro3.titulo, livro3.autor,  livro3.ano_publicacao)
