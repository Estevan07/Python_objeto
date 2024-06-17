class Album:
    def __init__(self, titulo, ano_lancamento, lista_faixas):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.lista_faixas = lista_faixas
    
    def mostrar_info(self):
        print(f'Album: {self.titulo}, {self.ano_lancamento}, {self.lista_faixas} ')
