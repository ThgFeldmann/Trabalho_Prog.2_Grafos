# Exemplo de um dado: "Porto Alegre, Pelotas, 291.3km"

#* Classes

# Classe Aresta (Conexão)
class Aresta:
    def __init__(self, cidade_1, cidade_2, distancia):
        self.cidade_1 = cidade_1
        self.cidade_2 = cidade_2
        self.distancia = distancia
    
    def Info_Aresta(self):
        print("-"*30)
        print(f"{self.cidade_1}, {self.cidade_2}, {self.distancia}")

# Classe Vértice (Cidade)
class Vertice:
    def __init__(self, nome_cidade, vizinhanca=[], conexoes=[]):
        self.nome_cidade = nome_cidade
        self.vizinhanca = vizinhanca
        self.conexoes = conexoes

    def Info_Vertice(self):
        print("-"*30)
        print(f"Nome da cidade: {self.nome_cidade}")
        print(f"Quantidade de vizinhos: {len(self.vizinhanca)}")
        print(f"Quantidade de conexões: {len(self.conexoes)}")

    def Info_Vizinhos(self):
        print("-"*30)
        
        for vizinho in self.vizinhanca:
            print("-"*15)
            vizinho.Info_Vertice()
    
    def Info_Conexoes(self):
        print("-"*30)
        
        for conexao in self.conexoes:
            conexao.Info_Aresta()

# Classe Grafo (Mapa)
class Grafo:
    def __init__(self, cidades=[], conexoes=[]):
        self.cidades = cidades
        self.conexoes = conexoes
    
    def Info_Cidades(self):
        print("-"*30)
        
        for cidade in self.cidades:
            print("-"*15)
            cidade.Info_Vertice()
    
    def Info_conexoes(self):
        print("-"*30)
        
        for conexao in self.conexoes:
            print("-"*15)
            conexao.Info_Aresta()
    
    def Cadastra_Cidade(self, nova_cidade):
        self.cidades.append(nova_cidade)
    
    def Cadastra_Conexao(self, nova_conexao):
        self.conexoes.append(nova_conexao)

#* Funções

def Continuar():
    print("-"*30)
    input("Continuar...")
    print("-"*30)

#* Função Principal
if __name__ == '__main__':
    running = True

    while running:
        print("-"*30)
        print("Sistema Grafo")
        print("-"*30)

        print("Escolha a opção desejada:\n")
        print("1 - Cadastrar cidade")
        print("2 - Cadastrar conexão")
        print("3 - Listar cidades")
        print("4 - Listar conexôes")
        print("5 - Listar cidades vizinhas")
        print("0 - Sair")
        
        escolha = int(input("\n: "))
        
        if escolha == 0:
            print("-"*30)
            print("Saindo...")
            Continuar()
            running = False