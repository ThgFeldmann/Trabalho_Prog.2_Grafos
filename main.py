# Exemplo de um dado: "Porto Alegre, Pelotas, 291.3km"
#TODO Cadastro de conexões, duas mensagems de erro estão sendo mostradas juntas.

#* Classes

# Classe Aresta (Conexão)
class Aresta:
    def __init__(self, cidade_1, cidade_2, distancia):
        self.cidade_1 = cidade_1
        self.cidade_2 = cidade_2
        self.distancia = distancia
    
    def Info_Aresta(self):
        print(f"{self.cidade_1}, {self.cidade_2}, {self.distancia:.1f}km")
        print("-"*15)

# Classe Vértice (Cidade)
class Vertice:
    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade
        self.vizinhanca = []
        self.conexoes = []

    def Info_Vertice(self):
        print(f"Nome da cidade: {self.nome_cidade}")
        print(f"Quantidade de vizinhos: {len(self.vizinhanca)}")
        print(f"Quantidade de conexões: {len(self.conexoes)}")
        print("-"*15)

    def Info_Vizinhos(self):
        print("-"*30)

        # Lista onde serão armazenados dicionários: vizinho = {"nome": nome_vizinho, "distancia": distancia}
        lista_vizinhos = []

        # Lista de nomes dos vizinhos
        lista_nome_vizinhos = []
        
        # Buscando os nomes dos vizinhos e adicionando na lista
        for vizinho in self.vizinhanca:
            lista_nome_vizinhos.append(vizinho.nome_cidade)
        
        # Buscando as distâncias
        for conexao in self.conexoes:
            # Verificando se algum nome da conexão ('cidade_1' ou 'cidade_2'), são vizinhos
            if conexao.cidade_1 in lista_nome_vizinhos: # Se 'cidade_1' for vizinho
                lista_vizinhos.append({"nome": conexao.cidade_1, "distancia": conexao.distancia})
            elif conexao.cidade_2 in lista_nome_vizinhos: # Se 'cidade_2' for vizinho
                lista_vizinhos.append({"nome": conexao.cidade_2, "distancia": conexao.distancia})
        
        # Ordenando a lista pela distância dos vizinhos. Ordem ascendente
        lista_ordenada = sorted(lista_vizinhos, key=lambda vizinho: vizinho["distancia"])
        
        # Mostrando os vizinhos, já ordenados
        for vizinho in lista_ordenada:
            print(f"{vizinho["nome"]} - {vizinho["distancia"]}")
    
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
    def __init__(self):
        self.cidades = []
        self.conexoes = []
    
    def Info_Cidades(self):
        print("-"*30)
        lista_alfabetica = sorted(self.cidades, key=lambda cidade: cidade.nome_cidade)
        
        for cidade in lista_alfabetica:
            cidade.Info_Vertice()

        Continuar()
    
    def Info_Conexoes(self):
        print("-"*30)
        
        for conexao in self.conexoes:
            conexao.Info_Aresta()
    
        Continuar()
    
    def Cadastra_Cidade(self, nova_cidade):
        self.cidades.append(nova_cidade)
    
    def Cadastra_Conexao(self, nova_conexao):
        self.conexoes.append(nova_conexao)
    
    def Listar_Vizinhanca_Da_Cidade(self, nome_cidade):
        print(f"Vizinhos de: {nome_cidade}")

        for cidade in self.cidades:
            if cidade.nome_cidade == nome_cidade:
                cidade.Info_Vizinhos()
    
    def Busca_Cidade_Por_Nome(self, nome_cidade):
        for cidade in self.cidades:
            if cidade.nome_cidade == nome_cidade:
                return cidade
    
    def Verificar_Cidade_Existe(self, nome_cidade):
        for cidade in self.cidades:
            if cidade.nome_cidade == nome_cidade:
                return True
    
    def Verificar_Conexao_Existe(self, nova_conexao):
        # O retorno deste método é um booleano: 'True' se a conexão já existe e 'False' se não existe
        
        # Realizando verificações para descobrir se a conexão já existe no Grafo
        for conexao in self.conexoes:
            if conexao == nova_conexao: # Se a conexão for idêntica
                return True
            elif (conexao.cidade_1 == nova_conexao.cidade_1) and (conexao.cidade_2 == nova_conexao.cidade_2): # Se as cidades forem idênticas
                return True

            elif (nova_conexao.cidade_1 == conexao.cidade_2) and (nova_conexao.cidade_2 == conexao.cidade_1): # Se as cidades forem idênticas porém invertidas
                return True

        # Se não houver erros
        return False

#* Funções

# Função para validar o nome de uma cidade, retorna um booleano para o resultado
def Validar_Nome_Cidade(nome_cidade):
    if nome_cidade == "" or nome_cidade == None or nome_cidade == " ": # Se o nome for vazio
        print("-"*30)
        print("O nome da cidade não pode ficar vazio, insira algum valor.")
        Continuar()
        return False
    else:
        # Verificando se tem algum número no nome da cidade inserido
        tem_numero = any(letra.isdigit() for letra in nome_cidade)
        
        if tem_numero == True: # Se tiver algum número
            print("-"*30)
            print("Erro, o nome da cidade deve conter apenas letras.")
            Continuar()

        else: # Se estiver correto
            return True

# Função para a entrada do nome de uma cidade
def Entrada_De_Cidade():
    try:
        cidade = input(": ")
        cidade_e_valida = Validar_Nome_Cidade(cidade)
        
        if cidade_e_valida: # Se o nome da cidade for válido
            # retornando o nome da cidade em 'title'
            return cidade.title()
        else:
            # retornando uma 'string' vazia caso o valor seja inválido
            return ''

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
        
        if nome_cidade == "" or nome_cidade == None or nome_cidade == " ":
            continue
        else:
            cidade_existe = grafo.Verificar_Cidade_Existe(nome_cidade)
            
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
                print("-"*30)
                print("\nEsta cidade já existe na lista de cidades.")
                print("Encerrando o cadastro...")
                Continuar()
                running = False

#TODO Duas mensagens de erro são mostradas
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
            print("Não há cidades suficientes para criar uma conexão.")
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
                    cidade_1_existe = grafo.Verificar_Cidade_Existe(nome_cidade_1)
                    
                    if cidade_1_existe:
                        recebendo_valores = False
                    else:
                        print("-"*30)
                        print("Não foi possível continuar com o cadastro.")
                        print("Esta cidade não existe na lista local.")
                        Continuar()
                        continue

            recebendo_valores = True
            
            while recebendo_valores:
                print("\nDigite o nome da segunda cidade:")
                nome_cidade_2 = Entrada_De_Cidade()
                
                if nome_cidade_2 == "":
                    continue
                elif nome_cidade_2 == nome_cidade_1: # Se este nome foi inserido no campo anterior
                    print("-"*30)
                    print("Não foi possível continuar com o cadastro.")
                    print("Este nome já foi inserido no cadastro.")
                    print("\nTente novamente usando nomes diferentes.")
                    Continuar()
                    continue
                    
                else:
                    cidade_2_existe = grafo.Verificar_Cidade_Existe(nome_cidade_2)
                    
                    if cidade_2_existe:
                        recebendo_valores = False
                    else:
                        print("-"*30)
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

                if not distancia: # Se 'distância' não existe
                    print("-"*30)
                    print("Não foi possível continuar com o cadastro.")
                    print("Insira algum valor positivo como a distância.")
                    Continuar()
                    continue
                
                elif distancia < 0: # Se 'distância' for um valor negativo
                    print("-"*30)
                    print("Não foi possível continuar com o cadastro.")
                    print("Distânia não pode ser um valor negativo.")
                    Continuar()
                    continue
                
                else:
                    recebendo_valores = False

            try:
                conexao = Aresta(nome_cidade_1, nome_cidade_2, distancia)

                # Verificando se a conexão já existe
                conexao_existe = grafo.Verificar_Conexao_Existe(conexao)
                
                if not conexao_existe: # Se a conexão não existe no grafo
                    # Buscando os objetos destas cidades no Grafo
                    cidade_1 = grafo.Busca_Cidade_Por_Nome(nome_cidade_1)
                    cidade_2 = grafo.Busca_Cidade_Por_Nome(nome_cidade_2)

                    # Adicionando Vizinhos
                    cidade_1.Adicionar_Vizinho(cidade_2)
                    cidade_2.Adicionar_Vizinho(cidade_1)

                    cidade_1.Adicionar_Conexao(conexao)
                    cidade_2.Adicionar_Conexao(conexao)

                    # Adicionando conexão ao grafo, na lista de conexões
                    grafo.Cadastra_Conexao(conexao)
                    print("\nCadastro realizado com sucesso.")
                    Continuar()
                    running = False
                
                else: # Se a conexão já existe no Grafo
                    print("-"*30)
                    print("Não será possível cadastrar esta conexão, por uma das razões abaixo:")
                    print("- Ela já existe no Grafo;")
                    print("- Ela utiliza cidades que já possuem uma conexão entre sí.")
                    
                    print("\nEste cadastro foi cancelado, retornando ao menu...")
                    Continuar()
                    running = False

            except Exception as error:
                print("\nOcorreu um erro inesperado, não foi possível terminar o cadastro.")
                print(f"\nMensagem de erro: {error}")
                Continuar()
                continue

# Função para listar os vizinhos de uma cidade específica
def Listar_Vizinhos(grafo):
    running = True

    while running:
        print("-"*30)
        print("Listagem de Vizinhos de uma Cidade\n")
        nome_cidade = Entrada_De_Cidade()
        
        if nome_cidade == "":
            continue
        else:
            cidade_existe = grafo.Verificar_Cidade_Existe(nome_cidade)
            
            if cidade_existe:
                try:
                    grafo.Listar_Vizinhanca_Da_Cidade(nome_cidade)
                    Continuar()
                    running = False
                except Exception as error:
                    print("-"*30)
                    print("\nOcorreu um erro inesperado. Tente novamente.")
                    print(f"\nMensagem de erro: {error}")
                    Continuar()
                    continue

            else:
                print("\nEsta cidade não existe na lista de cidades.")
                print("\nEncerrando a busca...")
                Continuar()
                running = False

# Função para carregar os dados do arquivo para a lista local
def Carregar_Arquivo(grafo):
    running = True
    contador_linhas = 0
    contador_cadastros = 0

    while running:
        print("-"*30)
        with open("dados.csv", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    try:
                        contador_linhas += 1
                        # Normalizando a linha para uso
                        linha = linha.strip().split(",")
                        linha_cidade_1 = linha[0]
                        cidade_e_valida = Validar_Nome_Cidade(linha_cidade_1)
                        
                        if cidade_e_valida:
                            linha_cidade_1 = linha_cidade_1.title()

                            linha_cidade_2 = linha[1]
                            cidade_e_valida = Validar_Nome_Cidade(linha_cidade_2)
                            
                            if cidade_e_valida:
                                linha_cidade_2 = linha_cidade_2.title()
                                
                                linha_distancia = float(linha[2].replace(",", "."))
                                
                                # Criando a conexão
                                conexao = Aresta(linha_cidade_1, linha_cidade_2, linha_distancia)
                                
                                conexao_existe = grafo.Verificar_Conexao_Existe(conexao)
                                
                                if not conexao_existe: # Se a coneão não existe no Grafo
                                    # Criando as cidades
                                    cidade_1 = Vertice(linha_cidade_1)
                                    cidade_2 = Vertice(linha_cidade_2)
                                    
                                    # Adicionando a conexão nas cidades
                                    cidade_1.Adicionar_Conexao(conexao)
                                    cidade_2.Adicionar_Conexao(conexao)
                                    
                                    # Adicionando as cidades como vizinhas
                                    cidade_1.Adicionar_Vizinho(cidade_2)
                                    cidade_2.Adicionar_Vizinho(cidade_1)
                                    
                                    # Adicionando os objetos no Grafo
                                    grafo.Cadastra_Cidade(cidade_1)
                                    grafo.Cadastra_Cidade(cidade_2)
                                    grafo.Cadastra_Conexao(conexao)

                                    contador_cadastros += 1

                            else:
                                raise ValueError
                            
                        else:
                            raise ValueError

                    except ValueError:
                        print("-"*30)
                        print(f"Ocorreu um erro na linha: {contador_linhas}")
                        print("Verifique os valores da linha.")
                        print("A leitura do arquivo vai continuar.")
                        Continuar()
                        continue
        
        running = False
        print()
        if contador_cadastros <= 0:
            print("Nenhuma conexão foi carregada.")
        elif contador_cadastros == 1:
            print(f"Foi carregada: {contador_cadastros} conexão.")
        else:
            print(f"Foram carregadas: {contador_cadastros} conexões.")

        Continuar()

# Função para atualizar os dados do arquivo, usando a lista local
def Atualizar_Arquivo(grafo):
    running = True

    try:
        while running:
            print("-"*30)
            
            # Abrindo o arquivo para a escrita de dados
            with open('dados.csv', 'w', encoding="utf-8") as arquivo:
                # Lendo todas as conexões do Grafo
                for conexao in grafo.conexoes:
                    # Escrevendo a conexão no arquivo
                    arquivo.write(f"{conexao.cidade_1},{conexao.cidade_2},{conexao.distancia}\n")
            
            running = False

        print("\nArquivo Atualizado")
    except Exception as error:
        print("\nOcorreu um erro inesperado ao atualizar o arquivo.")
        print("Verifique os dados e tente novamente.")
        print(f"\nMensagem de erro: {error}")

    Continuar()

# Função para evitar a apresentação excessiva para o usuário
def Continuar():
    print("-"*30)
    input("Continuar...")

# Função de teste, vai ser removida futuramente
def Test(grafo):
    grafo.cidades.append(Vertice("Test"))
    grafo.cidades.append(Vertice("Teste"))
    grafo.cidades.append(Vertice("Cidade"))
    
    # grafo.conexoes.append(Aresta("Test", "Teste", 20.2))
    # grafo.conexoes.append(Aresta("Cidade", "Test", 60))
    
    Continuar()

#* Função Principal
if __name__ == '__main__':
    grafo = Grafo()
    
    running = True

    while running:
        print()
        print("-"*30)
        print("\tSistema Grafo")
        print("-"*30)

        print("Escolha a opção desejada:\n")
        print("1 - Cadastrar cidade")
        print("2 - Cadastrar conexão")
        print("3 - Listar cidades")
        print("4 - Listar conexôes")
        print("5 - Listar cidades vizinhas")
        print("6 - Carregar arquivo")
        print("7 - Atualizar arquivo")
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
        
        elif escolha == 5:
            Listar_Vizinhos(grafo)
        
        elif escolha == 6:
            # Apagando os dados do Grafo
            grafo = None
            # Criando um novo grafo, sem dados
            grafo = Grafo()

            Carregar_Arquivo(grafo)
        
        elif escolha == 7:
            if len(grafo.conexoes) <= 0:
                print("-"*30)
                print("O Grafo não possui nenhuma conexão cadastrada.")
                print("Não será possível atualizar o arquivo.")
                Continuar()
            else:
                Atualizar_Arquivo(grafo)
        
        else:
            print("-"*30)
            print("Opção inválida, tente novamente.")
            continue