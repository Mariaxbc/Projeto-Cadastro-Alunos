from datetime import date

codigo = 1 #base do codigo
alunos = []

# CRIAÇÃO DA FUNÇÃO PARA REALIZAR O CÁLCULO DA IDADE --------------------------------

def Calcular_idade():

    while True: 
        dataNascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        dados = dataNascimento.split("/")

        while len(dados) != 3:
            print("Digite a data no formato DD/MM/AAAA!")
            dataNascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            dados = dataNascimento.split("/")

        while not dados[0].isdigit() or not dados[1].isdigit() or not dados[2].isdigit():
            print("Digite apenas números na data!")
            dataNascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            dados = dataNascimento.split("/")

        hoje = date.today()
        idade = hoje.year - int(dados[2])

        if int(dados[1]) > hoje.month:
            idade -= 1

        elif int(dados[1]) == hoje.month:
            if int(dados[0]) > hoje.day:
                idade -= 1

        if idade > 0:
            return idade

        print("\n-> Erro: Idade não pode ser menor que zero!")

#------ CRIAÇÃO DA FUNÇÃO DE CADASTRAR ALUNOS --------------------------------------

def Cadastrar_aluno(): #funcao para cadastrar aluno
    global codigo
    resposta = "N"

    print("Pronto para realizar seu cadastro? Preencha as informacoes a seguir!")

    while resposta == "N": 

        nomeAluno = input("\nDigite seu nome: ").title()
        idade = Calcular_idade()
        curso = input("Está matriculado em qual curso?: ")


#------VERIFICAÇÃO DE ERROS --------------------------------------------------------

        while nomeAluno.strip() == "":
            print("\n-> Erro: Nome obrigatório!")
            nomeAluno = input("\nDigite seu nome: ").title()

        while curso.strip() == "":
            print("\n-> Erro: Para se cadastrar é obrigatório estar matriculado em um curso!")
            curso = input("\nEstá matriculado em qual curso?: ")

#------CONFIRMAÇÃO DAS INFORMAÇÕES PARA SALVAR -------------------------------------

        print("\n\nConfirme as informações a seguir para salvar seu cadastro:")
        print(nomeAluno, "\n",idade, "\n",curso)
        print("As informações estão corretas?")
        resposta = input("Digite 'S' para sim e 'N' para não!").upper()

        while resposta.strip() != "S" and resposta.strip() != "N":
            print("\nResponda corretamente para que o cadastro seja efetuado!")
            resposta = input("\nDigite 'S' para sim e 'N' para não!").upper()

#------SALVA AS INFORMAÇÕES DOS ALUNOS NA MEMÓRIA ---------------------------------

    aluno = [codigo,nomeAluno, idade, curso] #quais dados a lista alunos vai guardar
    alunos.append(aluno) #organiza os dados em um tipo de lista
    codigo += 1

Cadastrar_aluno()        