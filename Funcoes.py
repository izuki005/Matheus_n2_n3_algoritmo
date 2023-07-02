def cadastrar_dados():  # função cadastrar dados irá pedir quais dados são necessário para o cadastro na escolinha do flamengo
    with open("Dados.txt", "a") as arquivo:
        print("\033[31m-=-\033[0m" * 20)
        print("\033[30mCADA\033[0m\033[31mSTRO\033[0m NA ESCOLINHA DO \033[30mC\033[0m.\033[31mR\033[0m. \033[31mFLAMENGO\033[0m")
        print("\033[31m-=-\033[0m" * 20)

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

        aluno = f"Nome: {nome}\nNúmero: {telefone}\nE-mail: {e_mail}\nSexo: {sexo}\nCpf: {cpf}\nData de Nascimento: {data_nascimento}\n" \
                f"CEP: {cep}\nNome do responsável: {nome_responsavel}\nCPF do responsável: {identidade_responsavel}\nNome escola: {nome_escola}\nSérie escola: {serie_escola}\nPosição: {posicao}\nÍdolo: {idolo}\n"

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
                contador = 1
                cadastro = [] 
                for linha in linhas:
                    if linha.startswith("Nome:"):
                        if cadastro:
                            print(f"\nCADASTRO {contador}:")
                            for linha in cadastro:
                                campo_valor, valor_campo = linha.split(': ')
                                print(f"{campo_valor}: {valor_campo}")
                            contador += 1
                            cadastro = []
                    cadastro.append(linha.strip())
                if cadastro:
                    print(f"\nCADASTRO {contador}:")
                    for linha_detalhe in cadastro:
                        campo_valor, valor_campo = linha_detalhe.split(': ')
                        print(f"{campo_valor}: {valor_campo}")
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print('Ocorreu um erro ao listar os dados:', str(e))

def alterar_dados(arquivo):
    print('\033[33m-=-\033[0m' * 20)
    print('\033[36mALTERAR DADOS\033[0m')
    print('\033[33m-=-\033[0m' * 20)
    
    dados = arquivo.readlines()
    arquivo.seek(0)
    
    print("\033[33mCADASTROS DISPONIVEIS:\033[0m")
    contador = 1
    for linha in dados:
        if linha.startswith('Nome:'):
            print(contador)
            contador += 1

    # Solicitar ao usuário o número do cadastro a ser alterado
    num_cadastro = int(input("\033[36mDIGITE O NÚMERO DO CADASTRO QUE DESEJA ALTERAR: \033[0m")) - 1

    if num_cadastro < 0 or num_cadastro >= contador-1:
        print('\033[31mNÚMERO DE CADASTRO INVÁLIDO!\033[0m')
        arquivo.close()
        return

    # Encontrar a posição inicial dos dados do cadastro escolhido
    cadastro = None
    cadastro_atual = 0

    for i, linha in enumerate(dados):
        if linha.startswith('Nome:'):
            if cadastro_atual == num_cadastro:
                cadastro = i
                break
            cadastro_atual += 1

    if cadastro is None:
        print('\033[31mNão foi possível encontrar o cadastro solicitado!\033[0m')
        arquivo.close()
        return

    while True:
        opcao = int(input('QUAL DESSES VOCÊ QUER MUDAR? \n1 - [NOME]\n'
                          '2 - [NUMERO]\n'
                          '3 - [E-MAIL]\n'
                          '4 - [NOME_RESPOSÁVEL]\n'
                          '5 - [NOME_ESCOLA]\n'
                          '6 - [SERIE_ESCOLA]\n'
                          '7 - [TORCIDA]\n'
                          '8 - [POSIÇÃO]\n'
                          '9 - [IDOLO]\n'
                          'ESCOLHA UM DESSES: '))

        if opcao == 1:
            novo_nome = input('NOVO NOME: ')
            dados[cadastro] = f"Nome: {novo_nome}\n"
        elif opcao == 2:
            novo_numero = input('NOVO NÚMERO: ')
            dados[cadastro+1] = f"Número: {novo_numero}\n"
        elif opcao == 3:
            novo_email = input('NOVO E-MAIL: ')
            dados[cadastro+2] = f"E-mail: {novo_email}\n"
        elif opcao == 4:
            novo_nome_responsavel = input('NOME DO RESPONSÁVEL: ')
            dados[cadastro+3] = f"Nome do Responsável: {novo_nome_responsavel}\n"
        elif opcao == 5:
            novo_nome_escola = input('NOME DA NOVA ESCOLA: ')
            dados[cadastro+4] = f"Nome da Escola: {novo_nome_escola}\n"
        elif opcao == 6:
            nova_serie_escola = input('NOVA SÉRIE ESCOLAR: ')
            dados[cadastro+5] = f"Série Escolar: {nova_serie_escola}\n"
        elif opcao == 7:
            nova_torcida = input('NOVA TORCIDA: ')
            dados[cadastro+6] = f"Torcida: {nova_torcida}\n"
        elif opcao == 8:
            nova_posicao = input('NOVA POSIÇÃO: ')
            dados[cadastro+7] = f"Posição: {nova_posicao}\n"
        elif opcao == 9:
            novo_idolo = input('NOVO ÍDOLO: ')
            dados[cadastro+8] = f"Ídolo: {novo_idolo}\n"
        else:
            print('\033[31mOPÇÃO INVÁLIDA\033[0m')
            print('\033[33m-=-\033[0m' * 20)
            continue

        opcao2 = input('MAIS ALGUMA COISA QUE QUEIRA ALTERAR? SIM OU NÃO: ').upper()
        while opcao2 != 'SIM' and opcao2 != 'S' and opcao2 != 'NÃO' and opcao2 != 'N':
            print('OPÇÃO INVÁLIDA! APENAS SIM OU NÃO!')
            opcao2 = input('MAIS ALGUMA COISA QUE QUEIRA ALTERAR? SIM OU NÃO: ').upper()

        if opcao2 == 'NÃO' or opcao2 == 'N':
            break

    arquivo.writelines(dados)  # Escreve as alterações no arquivo
    arquivo.truncate()
    arquivo.close()

def apagar_dados(arquivo):
    print('\033[33m-=-\033[0m' * 20)
    print('\033[36mAPAGAR DADOS\033[0m')
    print('\033[33m-=-\033[0m' * 20)

    dados = arquivo.readlines()
    arquivo.seek(0)

    # Listar os cadastros disponíveis
    print("Cadastros disponíveis:")
    contador = 1
    for linha in dados:
        if linha.startswith('Nome:'):
            print(contador)
            contador += 1

    # Solicitar ao usuário o número do cadastro a ser apagado
    num_cadastro = int(input("DIGITE O NÚMERO DO CADASTRO QUE DESEJA APAGAR: ")) - 1

    if num_cadastro < 0 or num_cadastro >= contador - 1:
        print('\033[31mNúmero de cadastro inválido!\033[0m')
        return

    # Encontrar a posição inicial dos dados do cadastro escolhido
    inicio_cadastro = None
    cadastro_atual = 0

    for i, linha in enumerate(dados):
        if linha.startswith('Nome:'):
            if cadastro_atual == num_cadastro:
                inicio_cadastro = i
                break
            cadastro_atual += 1

    if inicio_cadastro is None:
        print('\033[31mNão foi possível encontrar o cadastro solicitado!\033[0m')
        return

    while True:
        opcao = int(input('QUAL DESSES VOCÊ QUER APAGAR? \n1 - [NOME]\n'
                          '2 - [NUMERO]\n'
                          '3 - [E-MAIL]\n'
                          '4 - [NOME_RESPOSÁVEL]\n'
                          '5 - [NOME_ESCOLA]\n'
                          '6 - [SERIE_ESCOLA]\n'
                          '7 - [TORCIDA]\n'
                          '8 - [POSIÇÃO]\n'
                          '9 - [IDOLO]\n'
                          'ESCOLHA UM DESSES: '))

        if opcao == 1:
            dados[inicio_cadastro] = 'Nome: \n'
        elif opcao == 2:
            dados[inicio_cadastro + 1] = 'Número: \n'
        elif opcao == 3:
            dados[inicio_cadastro + 2] = 'E-mail: \n'
        elif opcao == 4:
            dados[inicio_cadastro + 3] = 'Nome do Responsável: \n'
        elif opcao == 5:
            dados[inicio_cadastro + 4] = 'Nome da Escola: \n'
        elif opcao == 6:
            dados[inicio_cadastro + 5] = 'Série Escolar: \n'
        elif opcao == 7:
            dados[inicio_cadastro + 6] = 'Torcida: \n'
        elif opcao == 8:
            dados[inicio_cadastro + 7] = 'Posição: \n'
        elif opcao == 9:
            dados[inicio_cadastro + 8] = 'Ídolo: \n'
        else:
            print('\033[31mOPÇÃO INVÁLIDA\033[0m')
            print('\033[33m-=-\033[0m' * 20)
            continue

        opcao2 = input('MAIS ALGUMA COISA QUE QUEIRA APAGAR? SIM OU NÃO: ').upper()
        while opcao2 != 'SIM' and opcao2 != 'S' and opcao2 != 'NÃO' and opcao2 != 'N':
            print('OPÇÃO INVÁLIDA! APENAS SIM OU NÃO!')
            opcao2 = input('MAIS ALGUMA COISA QUE QUEIRA APAGAR? SIM OU NÃO: ').upper()

        if opcao2 == 'NÃO' or opcao2 == 'N':
            break

    arquivo.writelines(dados)  # Escreve as alterações no arquivo
    arquivo.truncate()  # Remove as linhas remanescentes do conteúdo anterior, garantindo que apenas os dados atualizados permaneçam no arquivo.

def backup():
    try:
        with open("Dados.txt", "r") as arquivo_original:
            # ler o conteúdo do arquivo original
            conteudo = arquivo_original.read()

        # criar um novo arquivo de backup
        with open("backup_Dados.txt", "w") as arquivo_backup:
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
                arquivo_aberto = open("Dados.txt", "r+")
                alterar_dados(arquivo_aberto)  # Passa o arquivo_aberto como argumento
                arquivo_aberto.close()
            except ValueError as error:
                print("-=-" * 20)
                print(str(error))
                print("-=-" * 20)

        elif opcao == "4":
            try:
                if not os.path.exists("Dados.txt") or os.path.getsize("Dados.txt") == 0:
                    raise ValueError("AINDA NÃO HÁ DADOS PARA APAGAR")
                arquivo_aberto = open("Dados.txt", "r+")
                apagar_dados(arquivo_aberto)
                arquivo_aberto.close()
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
