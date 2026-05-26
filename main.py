# Exemplo de um dado: "Porto Alegre, Pelotas, 291.3km"
#TODO Adicionar Vizinhaça

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
    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade
        self.vizinhanca = []
        self.conexoes = []

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
    
    def Adicionar_Vizinho(self, novo_vizinho):
        self.vizinhanca.append(novo_vizinho)

    def Adicionar_Conexao(self, nova_conexao):
        self.conexoes.append(nova_conexao)

# Classe Grafo (Mapa)
class Grafo:
    def __init__(self, cidades=[], conexoes=[]):
        self.cidades = []
        self.conexoes = []
    
    def Info_Cidades(self):
        print("-"*30)
        
        for cidade in self.cidades:
            print("-"*15)
            cidade.Info_Vertice()
    
    def Info_Conexoes(self):
        print("-"*30)
        
        for conexao in self.conexoes:
            print("-"*15)
            conexao.Info_Aresta()
    
    def Cadastra_Cidade(self, nova_cidade):
        self.cidades.append(nova_cidade)
    
    def Cadastra_Conexao(self, nova_conexao):
        self.conexoes.append(nova_conexao)
    
    def Listar_Vizinhanca_Da_Cidade(self, nome_cidade):
        for cidade in self.cidades:
            if cidade.nome_cidade == nome_cidade:
                cidade.Info_Vizinhos()
    
    def Busca_Cidade_Por_Nome(self, nome_cidade):
        for cidade in self.cidades:
            if cidade.nome_cidade == nome_cidade:
                return cidade

#* Funções

# Função para verificar se a cidade existe
def Verificar_Cidade_Existe(lista_cidades, nome_cidade):
    for cidade in lista_cidades:
        if cidade.nome_cidade == nome_cidade:
            return True

# Função para a entrada de uma cidade
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

# Função de cadastro de uma cidade
def Cadastrar_Cidade(grafo):
    running = True

    while running:
        print("-"*30)
        print("Cadastro de uma Cidade\n")

        print("Digite o nome da cidade:")
        
        nome_cidade = Entrada_De_Cidade()
        
        if nome_cidade == "":
            continue
        else:
            cidade_existe = Verificar_Cidade_Existe(grafo, nome_cidade)
            
            if not cidade_existe:
                print("Cadastrando cidade...")
                
                try:
                    cidade = Vertice(nome_cidade)
                    grafo.Cadastra_Cidade(cidade)
                    
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

# Função de cadastro de uma conexão
def Cadastrar_Conexao(grafo):
    running = True
    # Criando estas variaveis apenas para
    lista_cidades = grafo.cidades

    while running:
        print("-"*30)
        print("Cadastro de uma Conexão")
        
        if len(lista_cidades) < 2: # Se não existir Cidades o suficiente
            print("-"*30)
            print("\nNão há cidades suficientes para criar uma conexão.")
            print("Adicione mais cidades antes desta conexão.\n")
            Continuar()
            running = False
        else:
            recebendo_valores = True
            
            while recebendo_valores:
                print("\nDigite o nome da primeira cidade:")
                nome_cidade_1 = Entrada_De_Cidade()
                
                if nome_cidade_1 == "":
                    continue
                else:
                    cidade_1_existe = Verificar_Cidade_Existe(lista_cidades, nome_cidade_1)
                    
                    if cidade_1_existe:
                        recebendo_valores = False
                    else:
                        print("\nNão foi possível continuar com o cadastro.")
                        print("Esta cidade não existe na lista local.")
                        Continuar()
                        continue

            recebendo_valores = True
            
            while recebendo_valores:
                print("\nDigite o nome da segunda cidade:")
                nome_cidade_2 = Entrada_De_Cidade()
                
                if nome_cidade_2 == "":
                    continue
                else:
                    cidade_2_existe = Verificar_Cidade_Existe(lista_cidades, nome_cidade_2)
                    
                    if cidade_2_existe:
                        recebendo_valores = False
                    else:
                        print("Não foi possível continuar com o cadastro.")
                        print("Esta cidade não existe na lista local.")
                        Continuar()
                        continue
            
            recebendo_valores = True
            
            while recebendo_valores:
                print("\nDigite a distância entre estas cidades:")
                print("- Utilize Km.")

                try:
                    distancia = input(": ").replace(",", ".")
                    
                    distancia = float(distancia)

                except ValueError:
                    print("-"*30)
                    print("\nOcorreu um erro com o valor da distância.")
                    print("Utilize apenas números inteiros ou flutuantes.")
                    Continuar()
                    continue

                if not distancia or distancia < 0: # Se 'distância' não existe ou se for negativo
                    print("Não foi possível continuar com o cadastro.")
                    print("Verifique se: A entrada possui valores ou a cidade existe na lista local.")
                else:
                    recebendo_valores = False

            try:
                conexao = Aresta(nome_cidade_1, nome_cidade_2, distancia)

                #TODO Testar
                # Buscando os objetos destas cidades
                cidade_1 = grafo.Busca_Cidade_Por_Nome(nome_cidade_1)
                cidade_2 = grafo.Busca_Cidade_Por_Nome(nome_cidade_2)
                
                # Adicionando como vizinhos
                cidade_1.Adicionar_Vizinho(cidade_2)
                cidade_2.Adicionar_Vizinho(cidade_1)

                # Adicionando conexão ao grafo, na lista de conexões
                grafo.Cadastra_Conexao(conexao)
                print("\nCadastro realizado com sucesso.")
                Continuar()
                running = False
            except Exception as error:
                print("\nOcorreu um erro inesperado, não foi possível terminar o cadastro.")
                print(f"\nMensagem de erro: {error}")

# Função para evitar a apresentação excessiva para o usuário
def Continuar():
    print("-"*30)
    input("Continuar...")

# Função de teste, vai ser removida futuramente
def Test(grafo):
    grafo.cidades.append(Vertice("Test"))
    grafo.cidades.append(Vertice("Teste"))
    
    Continuar()

#* Função Principal
if __name__ == '__main__':
    grafo = Grafo()
    
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
            Test(grafo)
        
        elif escolha == 0:
            print("-"*30)
            print("Saindo...")
            Continuar()
            running = False
        elif escolha == 1:
            Cadastrar_Cidade(grafo)
        
        elif escolha == 2:
            Cadastrar_Conexao(grafo)
        
        elif escolha == 3:
            grafo.Info_Cidades()
        
        elif escolha == 4:
            grafo.Info_Conexoes()
        
        else:
            print("-"*30)
            print("Opção inválida, tente novamente.")
            continue