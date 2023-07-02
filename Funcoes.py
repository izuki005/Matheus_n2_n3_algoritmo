def cadastrar_dados():  # função cadastrar dados irá pedir quais dados são necessário para o cadastro na escolinha do flamengo
    with open("Dados.txt", "a") as arquivo:
        print("\033[31m-=-\033[0m" * 20)
        print("\033[30mCADA\033[0m\033[31mSTRO\033[0m NA ESCOLINHA DO \033[30mC\033[0m.\033[31mR\033[0m. \033[31mFLAMENGO\033[0m")
        print("\033[31m-=-\033[0m" * 20)

        while True:
            try:
                id = input("Digite o id do jogador: ")
                if not id.replace(" ", "").isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI E NÃO DEIXA VAZIO!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                # abrir com with, abre e fecha o arquivo // "a" de append, se não tiver ou tiver um texto ele adiciona mais um
                nome = input("Digite o nome do jogador: ")
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                telefone = input("Digite seu número de telefone (**) ****-****: ")
                if telefone.replace(" ", '').isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO E COMECE DESSE JEITO: (**) ****-****!\033[0m\033[31m<------\033[0m")
                if "(" not in telefone or ")" not in telefone or "-" not in telefone:
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, SIGA A FORMATAÇÃO CORRETA EX: (*) **-**\033[0m \033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                e_mail = input("E-MAIL: ")
                if e_mail == "":
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                if "@" not in e_mail or "." not in e_mail:
                    raise ValueError(" ESCREVA UM EMAIL VÁLIDO COM: '@' e '.' ")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                sexo = input("Sexo:(MASCULINO/FEMININO) ").upper()
                if sexo not in ("MASCULINO", "M", "F", "FEMININO"):
                    raise ValueError("\033[31m------>\033[0m\033[33mOPÇÃO INVÁLIDA, DIGITE MASCULINO, OU FEMENINO!\033[0m\033[31m<------\033[0m")
                if not sexo.isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                if sexo == '':
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")

                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                cpf = input("IDENTIDADE: ")
                if not cpf.isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                if cpf == '':
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                if not cpf != 11:
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE OS 11 DIGITOS DA IDENTIDADE!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                data_nascimento = input("DATA DE NASCIMENTO: ")
                if not data_nascimento.replace('/', '').isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE APENAS NÚMEROS E BARRAS CORRETAMENTE DD/MM/YYYY\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                cep = input("CEP: ")
                if not cep.isdigit():
                    raise ValueError("POR FAVOR, APENAS NÚMEROS AQUI!")
                if cep == " ":
                    raise ValueError("POR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!")
                if len(cep) != 8:
                    raise ValueError("POR FAVOR, DIGITE UM CEP VÁLIDO COM 8 DÍGITOS!")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                nome_responsavel = input("NOME DO RESPONSÁVEL: ")
                if not nome_responsavel.replace(" ", '').isalpha():
                    raise ValueError("POR FAVOR, APENAS LETRAS AQUI!")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                identidade_responsavel = input("CPF DO RESPONSÁVEL: ")
                if not identidade_responsavel.isdigit():
                    raise ValueError("POR FAVOR, APENAS NÚMERO POR AQUI!")
                if identidade_responsavel == " ":
                    raise ValueError("POR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!")
                if not identidade_responsavel != 11:
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE OS 11 DIGITOS DA IDENTIDADE!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                nome_escola = input("NOME DA ESCOLA QUE FREQUENTA: ")
                if not nome_escola.replace(" ", '').isalpha():
                    raise ValueError("POR FAVOR, APENAS LETRAS AQUI!")
                if nome_escola == " ":
                    raise ValueError("POR FAVOR, SEM ESPAÇOS EM BRANCO!")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                serie_escola = input("SÉRIE NA ESCOLA: ")
                if not serie_escola.isalnum():
                    raise ValueError("POR FAVOR, APENAS LETRA POR AQUI!")
                if serie_escola == " ":
                    raise ValueError("POR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                posicao = input("QUAL A POSIÇÃO VOCÊ ATUA ?")
                if not posicao.replace(" ", '').isalpha():
                    raise ValueError("POR FAVOR, APENAS LETRAS AQUI!")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                idolo = input("QUAL SEU ÍDOLO NO FUTEBOL? ")
                if not idolo.replace(" ", '').isalpha():
                    raise ValueError("POR FAVOR, APENAS LETRAS POR AQUI!")
                if idolo == " ":
                    raise ValueError(" POR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!")
                break
            except ValueError as erro:
                print(str(erro))

        aluno = f"{id},{nome},{telefone},{e_mail},{sexo},{cpf},{data_nascimento},{cep},{nome_responsavel},{identidade_responsavel},{nome_escola},{serie_escola},{posicao},{idolo}\n"

        arquivo.write(aluno)

    print("\033[31m-=-\033[0m" * 20)
    print("\033[32mSEU CADASTRO FOI CONCLUIDO COM SUCESSO!\033[0m")
    print("\033[31m-=-\033[0m" * 20)


def listar():
    try:
        with open('Dados.txt', 'r') as arquivo:
            print("-=-" * 20)
            print("LISTAR DADOS")
            print("-=-" * 20)
            linhas = arquivo.readlines()
            if not linhas:
                print('NENHUM DADO DE CADASTRO ENCONTRADO')
            else:
                print('DADOS DE ALUNOS CADASTRADOS:')
                registros = [] 
                for linha in linhas:
                    dados = linha.strip().split(',')

                    id = int(dados[0])
                    nome = str(dados[1])
                    telefone = str(dados[2])
                    e_mail = str(dados[3])
                    sexo = str(dados[4])
                    cpf = dados[5]
                    data_nascimento = str(dados[6])
                    cep = dados[7]
                    nome_responsavel = str(dados[8])
                    identidade_responsavel = dados[9]
                    nome_escola = str(dados[10])
                    serie_escola = dados[11]
                    posicao = str(dados[12])
                    idolo = str(dados[13])

                    dados_cadastro = {
                        "Id:": id,
                        "Nome": nome,
                        "Telefone": telefone,
                        "E-mail": e_mail,
                        "Sexo": sexo,
                        "CPF": cpf,
                        "Data de Nascimento": data_nascimento,
                        "CEP": cep,
                        "Nome do Responsável": nome_responsavel,
                        "Identidade do Responsável": identidade_responsavel,
                        "Nome da Escola": nome_escola,
                        "Série da Escola": serie_escola,
                        "Posição": posicao,
                        "Ídolo do Futebol": idolo
                    }
                    registros.append(dados_cadastro)

                for dados_cadastro in registros:
                    print("-------------------------------------------")
                    for respositorio, valor in dados_cadastro.items():
                        print(respositorio + ":", valor)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print('Ocorreu um erro ao listar os dados:', str(e))


def alterar_dados():
    try:
        with open('Dados.txt', 'r+') as arquivo:
            print("-=-" * 20)
            print("ALTERAR DADOS")
            print("-=-" * 20)
            linhas = arquivo.readlines()
            if not linhas:
                print('NENHUM DADO DE CADASTRO ENCONTRADO')
                return

            id_aluno = int(input("Digite o ID do aluno que deseja alterar os dados: "))

            cadastro = False

            for i, linha in enumerate(linhas):
                dados = linha.strip().split(',')

                id = int(dados[0])
                if id == id_aluno:
                    cadastro = True

                    # Solicita os novos dados do aluno
                    nome = input("Digite o novo nome: ")
                    telefone = input("Digite o novo telefone: ")
                    e_mail = input("Digite o novo e-mail: ")
                    sexo = input("Digite o novo sexo: ")
                    cpf = input("Digite o novo CPF: ")
                    data_nascimento = input("Digite a nova data de nascimento: ")
                    cep = input("Digite o novo CEP: ")
                    nome_responsavel = input("Digite o novo nome do responsável: ")
                    identidade_responsavel = input("Digite a nova identidade do responsável: ")
                    nome_escola = input("Digite o novo nome da escola: ")
                    serie_escola = input("Digite a nova série da escola: ")
                    posicao = input("Digite a nova posição: ")
                    idolo = input("Digite o novo ídolo do futebol: ")

                    # Atualiza os dados do aluno na linha correspondente
                    dados_alterados = [
                        str(id),
                        nome,
                        telefone,
                        e_mail,
                        sexo,
                        cpf,
                        data_nascimento,
                        cep,
                        nome_responsavel,
                        identidade_responsavel,
                        nome_escola,
                        serie_escola,
                        posicao,
                        idolo
                    ]
                    linhas[i] = ','.join(dados_alterados) + '\n'

                    # Escreve as alterações novas no arquivo
                    arquivo.seek(0)
                    arquivo.writelines(linhas)
                    arquivo.truncate()

                    print("Dados alterados com sucesso!")
                    break

            if not cadastro:
                print("ID não encontrado.")
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print('Ocorreu um erro ao alterar os dados:', str(e))

def apagar_dados():
    try:
        with open('Dados.txt', 'r+') as arquivo:
            print("-=-" * 20)
            print("ALTERAR DADOS")
            print("-=-" * 20)
            linhas = arquivo.readlines()
            if not linhas:
                print('NENHUM DADO DE CADASTRO ENCONTRADO')
                return

            id_aluno = int(input("Digite o ID do aluno que deseja excluir os dados: "))

            excluido = False
            novas_linhas = []

            for linha in linhas:
                dados = linha.strip().split(',')

                id = int(dados[0])
                if id == id_aluno:
                    excluido = True
                else:
                    novas_linhas.append(linha)

            if excluido:
                arquivo.seek(0)
                arquivo.writelines(novas_linhas)
                arquivo.truncate()
                print("Dados excluídos com sucesso!")
            else:
                print("ID não encontrado.")

    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print('Ocorreu um erro ao excluir os dados:', str(e))

def backup():
    try:
        with open("Dados.txt", "r") as arquivo_original:
            # ler o conteúdo do arquivo original
            conteudo = arquivo_original.read()

        # criar um novo arquivo de backup
        with open("backup_Dados.txt", "a") as arquivo_backup:
            arquivo_backup.write(conteudo)

        print("-=-" * 20)
        print("BACKUP REALIZADO COM SUCESSO!")
        print("-=-" * 20)
    except FileNotFoundError:
        print("-=-" * 20)
        print("ARQUIVO NÃO ENCONTRADO!")
        print("-=-" * 20)


def menu():
    import os

    while True:

        print("ESCOLHA A OPÇÃO: \n [\033[32m1\033[0m] - \033[35mCadastrar Dados\033[0m\n"
              " [\033[32m2\033[0m] - \033[35mListar Dados\033[0m \n"
              " [\033[32m3\033[0m] - \033[35mAlterar Dados\033[0m \n"
              " [\033[32m4\033[0m] - \033[35mExcluir Dados\033[0m \n"
              " [\033[32m5\033[0m] - \033[35mBackup de Dados\033[0m \n"
              " [\033[32m0\033[0m] - \033[35mSair\033[0m")
        opcao = input("Digite sua opção: ")

        if opcao == "0":
            print("-=-" * 20)
            print("FINALIZADO!")
            print("-=-" * 20)
            break

        elif opcao == "1":
            cadastrar_dados()

        elif opcao == "2":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("AINDA NÃO HÁ CADASTRO")
                listar()
            except ValueError as error:
                print("-=-" * 20)
                print(str(error))
                print("-=-" * 20)

        elif opcao == "3":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError(" AINDA NÃO HÁ DADOS PARA ALTERAR ")
                alterar_dados()
            except ValueError as error:
                print("-=-" * 20)
                print(str(error))
                print("-=-" * 20)

        elif opcao == "4":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("AINDA NÃO HÁ DADOS PARA APAGAR")
                apagar_dados()
            except ValueError as error:
                print("-=-" * 20)
                print(str(error))
                print("-=-" * 20)

        elif opcao == "5":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("AINDA NÃO HÁ DADOS PARA FAZER BACKUP!")
                arquivo_aberto = open("Dados.txt", "r")
                backup()
                arquivo_aberto.close()
            except ValueError as error:
                print("-=-" * 20)
                print(str(error))
                print("-=-" * 20)
        else:
            print("OPÇÃO INVÁLIDA. DIGITE UM NÚMERO VÁLIDO.")
