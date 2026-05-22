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

# Função para verificar se a cidade existe
def Verificar_Cidade_Existe(lista_cidades, nome_cidade):
    for cidade in lista_cidades:
        if cidade.nome_cidade == nome_cidade:
            return True

def Entrada_De_Cidade():
    try:
        cidade = input(": ")
        
        if cidade == "": # Se a entrada for vazia
            print("-"*30)
            print("A entrada não pode ficar vazia, insira algum valor.")
            Continuar()
            return ""
        else:
            # Verificando se tem algum número na entrada
            tem_numero = any(letra.isdigit() for letra in cidade)
            
            if tem_numero == True: # Se tiver número
                raise ValueError
            else: # Se não tiver número
                cidade = cidade.title()
                #* Retornando a cidade
                return cidade

    except ValueError:
        print("-"*30)
        print("Erro na entrada. A entrada deve conter apenas letras.")
        Continuar()
    except Exception as error:
        print("-"*30)
        print("Erro inesperado na entrada. Tente novamente.")
        print(f"Mensagem de erro: {error}")
        Continuar()

def Cadastrar_Cidade(lista_cidades):
    running = True

    while running:
        print("-"*30)
        print("Cadastro de uma Cidade\n")

        print("Digite o nome da cidade:")
        
        nome_cidade = Entrada_De_Cidade()
        
        if nome_cidade == "":
            continue
        else:
            cidade_existe = Verificar_Cidade_Existe(lista_cidades, nome_cidade)
            
            if not cidade_existe:
                print("Cadastrando cidade...")
                
                try:
                    lista_cidades.append(Vertice(nome_cidade))
                    
                    print("\nCidade cadastrada com sucesso.")
                    Continuar()
                    
                    running = False
                except Exception as error:
                    print("-"*30)
                    print("Ocorreu um erro inesperado durante o cadastro da cidade.")
                    print("Tente novamente.")
                    Continuar()
                    continue

            else:
                print("\nEsta cidade já existe na lista de cidades.")
                print("Encerrando o cadastro...")
                Continuar()
                running = False

def Cadastrar_Conexao(lista_cidades, lista_conexoes):
    running = True

    while running:
        print("-"*30)
        print("Cadastro de uma Conexão\n")
        
        if len(lista_cidades) < 2: # Se não existir Cidades o suficiente
            print("-"*30)
            print("Não há cidades suficientes para criar uma conexão.")
            print("Adicione mais cidades antes desta conexão.\n")
            Continuar()
            running = False
        else:
            print("Digite o nome da primeira cidade:")
            cidade_1 = Entrada_De_Cidade()
            cidade_1_existe = Verificar_Cidade_Existe(lista_cidades)
            
            if cidade_1 != "" and cidade_1_existe:
                print("Digite o nome da segunda cidade:")
                cidade_2 = Entrada_De_Cidade()
                cidade_2_existe = Verificar_Cidade_Existe
                
                if cidade_2 != "" and cidade_2_existe:
                    print("Digite a distância entre estas cidades:")
                    print("- Utilize Km")
                    distancia = float(input(": "))

def Continuar():
    print("-"*30)
    input("Continuar...")

def Test(lista_cidades):
    for cidade in lista_cidades:
        cidade.Info_Vertice()
    
    Continuar()

#* Função Principal
if __name__ == '__main__':
    lista_cidades = []
    lista_conexoes = []
    
    running = True

    while running:
        print()
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
        print("10 - TESTE")

        try:
            escolha = int(input("\n: "))
        except ValueError:
            print("-"*30)
            print("Erro na entrada. A entrada deve conter apenas um número válido")
            Continuar()
            continue
        except Exception as error:
            print("-"*30)
            print("Erro inesperado na entrada. Tente novamente.")
            print(f"Mensagem de erro: {error}")
            Continuar()
            continue
        
        if escolha == 10:
            Test(lista_cidades)
        
        if escolha == 0:
            print("-"*30)
            print("Saindo...")
            Continuar()
            running = False
        elif escolha == 1:
            Cadastrar_Cidade(lista_cidades)
        
        elif escolha == 2:
            Cadastrar_Conexao(lista_cidades, lista_conexoes)
        
        else:
            print("-"*30)
            print("Opção inválida, tente novamente.")
            continue