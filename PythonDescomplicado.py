class SimpleName:
    def __init__(self, nome):
        self.nome = nome.strip()
    def mostrar_nome(self):
        print(f'O nome passado por parâmetro é {self.nome}')

simpleName = SimpleName('            Deivisson')
simpleName.mostrar_nome()

simpleName = SimpleName('Gustavo          ')
simpleName.mostrar_nome()