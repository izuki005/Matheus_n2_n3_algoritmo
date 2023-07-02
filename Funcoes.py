def cadastrar_dados():  # função cadastrar dados irá pedir quais dados são necessário para o cadastro na escolinha do flamengo
    with open("Dados.txt", "a") as arquivo:
        print("\033[31m-=-\033[0m" * 20)
        print("        \u26BD CADA\033[31mSTRO NA\033[0m ESCOLINHA DO \033[31mC.R\033[0m. \033[31mFLAMENGO\033[0m \u26BD")
        print("\033[31m-=-\033[0m" * 20)
        print("")

        while True:
            try:
                id = input("\033[32m->\033[0m Digite o id do jogador: ")
                if not id.replace(" ", "").isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI E NÃO DEIXE VAZIO!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                # abrir com with, abre e fecha o arquivo // "a" de append, se não tiver ou tiver um texto ele adiciona mais um
                nome = input("\033[32m->\033[0m Digite o nome do jogador: ")
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                telefone = input("\033[32m->\033[0m Digite seu número de telefone (*) **-**: ")
                if telefone.replace(" ", '').isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO E COMECE DESSE JEITO: (*) **-**\033[0m\033[31m<------\033[0m")
                if "(" not in telefone or ")" not in telefone or "-" not in telefone:
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, SIGA A FORMATAÇÃO CORRETA EX: (*) **-**\033[0m \033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                e_mail = input("\033[32m->\033[0m E-MAIL: ")
                if e_mail == "":
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                if "@" not in e_mail or "." not in e_mail:
                    raise ValueError("\033[31m------>\033[0m\033[33mESCREVA UM EMAIL VÁLIDO COM: '@' e '.' \033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                sexo = input("\033[32m->\033[0m Sexo:(MASCULINO/FEMININO) ").upper()
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
                cpf = input("\033[32m->\033[0m CPF: ")
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
                data_nascimento = input("\033[32m->\033[0m DATA DE NASCIMENTO: ")
                if not data_nascimento.replace('/', '').isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE APENAS NÚMEROS E BARRAS CORRETAMENTE DD/MM/YYYY\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                cep = input("\033[32m->\033[0m CEP: ")
                if not cep.isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                if cep == " ":
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                if len(cep) != 8:
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, DIGITE UM CEP VÁLIDO COM 8 DÍGITOS!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                nome_responsavel = input("\033[32m->\033[0m NOME DO RESPONSÁVEL: ")
                if not nome_responsavel.replace(" ", '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                identidade_responsavel = input("\033[32m->\033[0m CPF DO RESPONSÁVEL: ")
                if not identidade_responsavel.isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                if identidade_responsavel == " ":
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                if not identidade_responsavel != 11:
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE OS 11 DIGITOS DA IDENTIDADE!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                nome_escola = input("\033[32m->\033[0m NOME DA ESCOLA QUE FREQUENTA: ")
                if not nome_escola.replace(" ", '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                if nome_escola == " ":
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                serie_escola = input("\033[32m->\033[0m SÉRIE NA ESCOLA: ")
                if not serie_escola.replace(" ", '').isalnum():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                posicao = input("\033[32m->\033[0m QUAL A POSIÇÃO VOCÊ ATUA ?")
                if not posicao.replace(" ", '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                idolo = input("\033[32m->\033[0m QUAL SEU ÍDOLO NO FUTEBOL? ")
                if not idolo.replace(" ", '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                if idolo == " ":
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        aluno = f"{id},{nome},{telefone},{e_mail},{sexo},{cpf},{data_nascimento},{cep},{nome_responsavel},{identidade_responsavel},{nome_escola},{serie_escola},{posicao},{idolo}\n"

        arquivo.write(aluno)

    print("\033[31m-=-\033[0m" * 20)
    print("\033[32m        \U0001F3C6 SEU CADASTRO FOI CONCLUIDO COM SUCESSO!\033[0m \U0001F3C6")
    print("\033[31m-=-\033[0m" * 20)


def listar():
    try:
        with open('Dados.txt', 'r') as arquivo:
            print("\033[31m-=-\033[0m" * 15)
            print("        \u26BD LISTAR DADOS \u26BD")
            print("\033[31m-=-\033[0m" * 15)
            print("")
            linhas = arquivo.readlines()
            if not linhas:
                print('\033[31m------>\033[0m\033[33mNENHUM DADO DE CADASTRO ENCONTRADO!\033[0m\033[31m<------\033[0m')
            else:
                print(' \U0001F3C6 DADOS DE ALUNOS CADASTRADOS \U0001F3C6')
                registros = []  # Lista para armazenar todos os registros
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
                        "Id": id,
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
                    print("\033[33m-------------------------------------------\033[0m")
                    for respositorio, valor in dados_cadastro.items():
                        print(respositorio + ":", valor)
    except FileNotFoundError:
        print('\033[31m------>\033[0m\033[33mARQUIVO NÃO ENCONTRADO!\033[0m\033[31m<------\033[0m')
    except Exception as e:
        print('\033[31m------>\033[0m\033[33mOCORREU UM ERRO AO LISTAR DADOS!\033[0m\033[31m<------\033[0m', str(e))


def alterar_dados():
    try:
        with open('Dados.txt', 'r+') as arquivo:
            print("\033[31m-=-\033[0m" * 20)
            print("                \U0001F45F ALTERAR DADOS \U0001F45F")
            print("\033[31m-=-\033[0m" * 20)
            print("")
            linhas = arquivo.readlines()
            if not linhas:
                print('\033[31m------>\033[0m\033[33mNENHUM DADO DE CADASTRO ENCONTRADO!\033[0m\033[31m<------\033[0m')
                return

            id_aluno = int(input("\033[32m->\033[0m Digite o ID do aluno que deseja alterar os dados: "))

            cadastro = False

            for i, linha in enumerate(linhas):
                dados = linha.strip().split(',')

                id = int(dados[0])
                if id == id_aluno:
                    cadastro = True

                    # Solicita os novos dados do aluno
                    while True:
                        try:
                            nome = input("\033[32m->\033[0m Digite o novo nome do jogador: ")
                            if not nome.replace(" ", "").isalpha():
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            telefone = input("\033[32m->\033[0m Digite o novo telefone (*) **-**: ")
                            if telefone.replace(" ", '').isdigit():
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO E COMECE DESSE JEITO: () *-*!\033[0m\033[31m<------\033[0m")
                            if "(" not in telefone or ")" not in telefone or "-" not in telefone:
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, SIGA A FORMATAÇÃO CORRETA EX: () -*\033[0m \033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            e_mail = input("\033[32m->\033[0m Digite o novo e-mail: ")
                            if e_mail == "":
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                            if "@" not in e_mail or "." not in e_mail:
                                raise ValueError("\033[31m------>\033[0m\033[33mESCREVA UM EMAIL VÁLIDO COM: '@' e '.'\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            sexo = input("\033[32m->\033[0m Digite o novo sexo (MASCULINO/FEMININO): ").upper()
                            if sexo not in ("MASCULINO", "M", "F", "FEMININO"):
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mOPÇÃO INVÁLIDA, DIGITE MASCULINO OU FEMININO!\033[0m\033[31m<------\033[0m")
                            if not sexo.isalpha():
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            if sexo == '':
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")

                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            cpf = input("\033[32m->\033[0m Digite o novo CPF: ")
                            if not cpf.isdigit():
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                            if cpf == '':
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                            if len(cpf) != 11:
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE OS 11 DÍGITOS DO CPF!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            data_nascimento = input("\033[32m->\033[0m Digite a nova data de nascimento: ")
                            if not data_nascimento.replace('/', '').isdigit():
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE APENAS NÚMEROS E BARRAS CORRETAMENTE DD/MM/YYYY\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            cep = input("\033[32m->\033[0m Digite o novo CEP: ")
                            if not cep.isdigit():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                            if cep == " ":
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                            if len(cep) != 8:
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, DIGITE UM CEP VÁLIDO COM 8 DÍGITOS!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            nome_responsavel = input("\033[32m->\033[0m Digite o novo nome do responsável: ")
                            if not nome_responsavel.replace(" ", '').isalpha():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            identidade_responsavel = input("\033[32m->\033[0m Digite o novo CPF do responsável: ")
                            if not identidade_responsavel.isdigit():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMERO POR AQUI!\033[0m\033[31m<------\033[0m")
                            if identidade_responsavel == " ":
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                            if len(identidade_responsavel) != 11:
                                raise ValueError(
                                    "\033[31m------>\033[0m\033[33mPOR FAVOR, COLOQUE OS 11 DÍGITOS DA IDENTIDADE!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            nome_escola = input("\033[32m->\033[0m Digite o novo nome da escola que frequenta: ")
                            if not nome_escola.replace(" ", '').isalpha():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            if nome_escola == " ":
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            serie_escola = input("\033[32m->\033[0m Digite a nova série na escola: ")
                            if not serie_escola.replace(" ", '').isalnum():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            posicao = input("\033[32m->\033[0m Digite a nova posição em que atua: ")
                            if not posicao.replace(" ", '').isalpha():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    while True:
                        try:
                            idolo = input("\033[32m->\033[0m Digite o novo ídolo no futebol: ")
                            if not idolo.replace(" ", '').isalpha():
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                            if idolo == " ":
                                raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÂO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                            break
                        except ValueError as erro:
                            print(str(erro))

                    # Atualiza os dados do aluno na linha correspondente
                    dados_alterados = [
                        str(id),
                        str(nome),
                        str(telefone),
                        str(e_mail),
                        str(sexo),
                        str(cpf),
                        str(data_nascimento),
                        str(cep),
                        str(nome_responsavel),
                        str(identidade_responsavel),
                        str(nome_escola),
                        str(serie_escola),
                        str(posicao),
                        str(idolo)
                    ]
                    linhas[i] = ','.join(dados_alterados) + '\n'

                    # Escreve as alterações novas no arquivo
                    arquivo.seek(0)
                    arquivo.writelines(linhas)
                    arquivo.truncate()
                    print("\033[31m-=-\033[0m"*20)
                    print("        \U0001F45F Dados alterados com sucesso! \U0001F45F")
                    print("\033[31m-=-\033[0m"*20)
                    break

            if not cadastro:
                print("\033[31m------>\033[0m\033[33mID NÃO ENCONTRADO!\033[0m\033[31m<------\033[0m")
    except FileNotFoundError:
        print('\033[31m------>\033[0m\033[33mARQUIVO NÃO ENCONTRADO!\033[0m\033[31m<------\033[0m')
    except Exception as e:
        print('\033[31m------>\033[0m\033[33mOCORREU UM ERRO AO ALTERAR DADOS!\033[0m\033[31m<------\033[0m', str(e))

def apagar_dados():
    try:
        with open('Dados.txt', 'r+') as arquivo:
            print("\033[31m-=-\033[0m" * 20)
            print("        \U0001F5D1 APAGAR DADOS \U0001F5D1") # TENHO MINHAS DÚVIDAS KK
            print("\033[31m-=-\033[0m" * 20)
            linhas = arquivo.readlines()
            if not linhas:
                print('\033[31m------>\033[0m\033[33mNENHUM DADO DE CADASTRO ENCONTRADO!\033[0m\033[31m<------\033[0m')
                return

            id_aluno = int(input("\033[32m->\033[0m DIGITE O ID DO ALUNO QUE DESEJA EXCLUIR OS DADOS: "))

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
                print("\033[31m-=-\033[0m"*20)
                print("\033[32m        \U0001F5D1 Dados excluídos com sucesso!\033[0m \U0001F5D1")
                print("\033[31m-=-\033[0m"*20)
            else:
                print("\033[31m------>\033[0m\033[33mID NÃO ENCONTRADO!\033[0m\033[31m<------\033[0m")

    except FileNotFoundError:
        print('\033[31m------>\033[0m\033[33mARQUIVO NÃO ENCONTRADO!\033[0m\033[31m<------\033[0m')
    except Exception as e:
        print('\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m', str(e))

def backup():
    try:
        with open("Dados.txt", "r") as arquivo_original:
            # ler o conteúdo do arquivo original
            conteudo = arquivo_original.read()

        # criar um novo arquivo de backup
        with open("backup_Dados.txt", "a") as arquivo_backup:
            arquivo_backup.write(conteudo)

        print("\033[31m-=-\033[0m" * 20)
        print("        \U0001F4C2 BACKUP REALIZADO COM SUCESSO! \U0001F4C2")
        print("\033[31m-=-\033[0m" * 20)
    except FileNotFoundError:
        print("\033[31m-=-\033[0m" * 20)
        print("\033[31m------>\033[0m\033[33mARQUIVO NÃO ENCONTRADO!\033[0m\033[31m<------\033[0m")
        print("\033[31m-=-\033[0m" * 20)


def menu():
    import os

    while True:

        print("\033[35m-----------------------\033[0m\n   ESCOLHA A OPÇÃO \n\033[35m-----------------------\033[0m\n \n [\033[32m1\033[0m] - \033[35mCadastrar Dados\033[0m\n"
              " [\033[32m2\033[0m] - \033[35mListar Dados\033[0m \n"
              " [\033[32m3\033[0m] - \033[35mAlterar Dados\033[0m \n"
              " [\033[32m4\033[0m] - \033[35mExcluir Dados\033[0m \n"
              " [\033[32m5\033[0m] - \033[35mBackup de Dados\033[0m \n"
              " [\033[32m0\033[0m] - \033[35mSair\033[0m")
        print("")
        opcao = input("\033[31m->\033[0m Digite sua opção: ")



        if opcao == "0":
            print("\033[35m-=-\033[0m" * 20)
            print("        \u2705 FINALIZADO! \u2705")
            print("\033[35m-=-\033[0m" * 20)
            break

        elif opcao == "1":
            cadastrar_dados()

        elif opcao == "2":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("\033[31m------>\033[0m\033[33mAINDA NÃO HÁ CADASTRO\033[0m\033[31m<------\033[0m")
                listar()
            except ValueError as error:
                print(str(error))
                

        elif opcao == "3":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("\033[31m------>\033[0m\033[33mAINDA NÃO HÁ DADOS PARA ALTERAR\033[0m\033[31m<------\033[0m")
                alterar_dados()
            except ValueError as error:
                print(str(error))
                

        elif opcao == "4":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("\033[31m------>\033[0m\033[33mAINDA NÃO HÁ DADOS PARA APAGAR\033[0m\033[31m<------\033[0m")
                apagar_dados()
            except ValueError as error:
                print(str(error))

        elif opcao == "5":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("\033[31m------>\033[0m\033[33mAINDA NÃO HÁ DADOS PARA FAZER BACKUP!\033[0m\033[31m<------\033[0m")
                arquivo_aberto = open("Dados.txt", "r")
                backup()
                arquivo_aberto.close()
            except ValueError as error:
                print(str(error))
        else:
            print("\033[31m------>\033[0m\033[33mOPÇÃO INVÁLIDA. DIGITE UM NÚMERO VÁLIDO.\033[0m\033[31m<------\033[0m")
