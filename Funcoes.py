def cadastrar_dados():  # função cadastrar dados irá pedir quais dados são necessário para o cadastro na escolinha do flamengo
    with open("Dados.txt", "a") as arquivo:
        print("\033[31m-=-\033[0m" * 20)
        print("\033[30mCADA\033[0m\033[31mSTRO\033[0m NA ESCOLINHA DO \033[30mC\033[0m.\033[31mR\033[0m. \033[31mFLAMENGO\033[0m")
        print("\033[31m-=-\033[0m" * 20)
        while True:
            try:
                # abrir com with, abre e fecha o arquivo // "a" de append, se não tiver ou tiver um texto ele adiciona mais um
                id = input("Digite o id do jogador: ")
                if not id.replace(" ", "").isnumeric():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))
        while True:
            try:
                nome = input("Digite o nome do jogador: ")
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                telefone = input("Digite seu número de telefone (*) **-**: ")
                if telefone.replace(" ", '').isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO E COMECE DESSE JEITO: (*) **-**!\033[0m\033[31m<------\033[0m")
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
                sexo = input("Sexo:(M/F) ").upper()
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
                identidade = input("IDENTIDADE: ")
                if not identidade.isdigit():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS NÚMEROS AQUI!\033[0m\033[31m<------\033[0m")
                if identidade == '':
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                orgao_emissor = input("ORGÃO EMISSOR: ")
                if not orgao_emissor.replace(' ', '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS AQUI!\033[0m\033[31m<------\033[0m")
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
                endereco = input('ENDEREÇO: ')
                if not endereco.replace(" ", '').isalnum():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                bairro = input("BAIRRO: ")
                if not bairro.replace(" ", '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m \n"
                        "\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS POR AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                cidade = input("CIDADE: ")
                if not cidade.replace(" ", '').isalpha():
                    raise ValueError("\033[31m------>\033[0m\033[33mPOR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!\033[0m\033[31m<------\033[0m \n"
                        "\033[31m------>\033[0m\033[33mPOR FAVOR, APENAS LETRAS POR AQUI!\033[0m\033[31m<------\033[0m")
                break
            except ValueError as erro:
                print(str(erro))

        estados = {
            "AC": "Acre",
            "AL": "Alagoas",
            "AP": "Amapá",
            "AM": "Amazonas",
            "BA": "Bahia",
            "CE": "Ceará",
            "DF": "Distrito Federal",
            "ES": "Espírito Santo",
            "GO": "Goiás",
            "MA": "Maranhão",
            "MT": "Mato Grosso",
            "MS": "Mato Grosso do Sul",
            "MG": "Minas Gerais",
            "PA": "Pará",
            "PB": "Paraíba",
            "PR": "Paraná",
            "PE": "Pernambuco",
            "PI": "Piauí",
            "RJ": "Rio de Janeiro",
            "RN": "Rio Grande do Norte",
            "RS": "Rio Grande do Sul",
            "RO": "Rondônia",
            "RR": "Roraima",
            "SC": "Santa Catarina",
            "SP": "São Paulo",
            "SE": "Sergipe",
            "TO": "Tocantins"
        }

        while True:
            try:
                estado = input("ESTADO: ")
                estado_sigla = None
                estado_completo = None

                if len(estado) == 2:
                    # Se a entrada tem dois caracteres, assume-se que é a sigla do estado
                    estado_sigla = estado.upper()
                    estado_completo = estados.get(estado_sigla)
                else:
                    # Verifica se a entrada corresponde a um estado completo
                    for sigla, nome in estados.items():
                        if estado.lower() == nome.lower():
                            estado_sigla = sigla
                            estado_completo = nome
                            break
                if not estado_sigla or not estado_completo:
                    raise ValueError("SIGLA OU NOME DE ESTADO INVÁLIDO")
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
                break
            except ValueError as erro:
                print(str(erro))

        while True:
            try:
                orgao_emissor_responsavel = input("ORGÃO EMISSOR DO RESPONSÁVEL: ")
                if not orgao_emissor_responsavel.replace(" ", '').isalpha():
                    raise ValueError("POR FAVOR, APENAS LETRAS AQUI!")
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
                torcida = input("VOCÊ TORCE PARA O FLAMENGO? SIM OU NÃO:").upper()
                if not torcida.replace(" ", '').isalpha():
                    raise ValueError("POR FAVOR, APENAS LETRAS AQUI!")
                if torcida == "NÃO":
                    outra_torcida = input("QUAL TIME VOCÊ TORCE? ")
                    if outra_torcida == " ":
                        raise ValueError("POR FAVOR, NÃO DEIXE ESPAÇOS EM BRANCO!")
                break
            except ValueError as erro:
                print(str(erro))
        outra_torcida = ''

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

        aluno = f"Nome: {nome}\nNúmero: {telefone}\nE-mail: {e_mail}\nSexo: {sexo}\nIdentidade: {identidade}\nOrgão Emissor: {orgao_emissor}\nData de Nascimento: {data_nascimento}\nEndereço: {endereco}\nBairro: {bairro}\nCidade: {cidade}\n" \
                f"Estado: {estado}\nCEP: {cep}\nNome do responsável: {nome_responsavel}\nCPF do responsável: {identidade_responsavel}\nOrgão Emissor responsável: {orgao_emissor_responsavel}\nNome escola: {nome_escola}\nSérie escola: {serie_escola}\nTorcida: {torcida}\nOutra torcida: {outra_torcida}\nPosição: {posicao}\nÍdolo: {idolo}\n"

        arquivo.write(aluno)

    print("\033[31m-=-\033[0m" * 20)
    print("\033[32mSEU CADASTRO FOI CONCLUIDO COM SUCESSO!\033[0m")
    print("\033[31m-=-\033[0m" * 20)


def listar():
    try:
        with open('Dados.txt', 'r') as arquivo_dados:
            print("-=-" * 20)
            print("LISTAR DADOS")
            print("-=-" * 20)
            if not arquivo_dados:
                print("NENHUM DADO DE ALUNO CADASTRADO.")
            else:
                print('DADOS DOS ALUNOS CADASTRADOS:')
                cadastro = 1
                dados_cadastro = []
                for linha in arquivo_dados:
                    campos = linha.strip().split(":")
                    campo = campos[1] if len(campos) > 1 else ""
                    dados_cadastro.append(f"{campos[0]}:{campo}")
                    if len(dados_cadastro) == 22:  # Número total de campos
                        print(f"Cadastro {cadastro}")
                        print("\n".join(dados_cadastro))
                        print()
                        dados_cadastro = []
                        cadastro += 1
            print("-=-" * 20)

    except FileNotFoundError:
        print(f"O arquivo '{arquivo_dados}' não foi encontrado.")
    except IOError:
        print(f"Erro ao abrir o arquivo '{arquivo_dados}'. Verifique as permissões.")

def alterar_dados(arquivo):
    print('\033[33m-=-\033[0m' * 20)
    print('\033[36mALTERAR DADOS\033[0m')
    print('\033[33m-=-\033[0m' * 20)

    dados = arquivo.readlines()
    arquivo.seek(0)

    # Listar os cadastros disponíveis
    print("\033[33mCADASTROS DISPONIVEIS:\033[0m")
    contador = 1
    for linha in dados:
        if linha.startswith('Nome:'):
            print(contador)
            contador += 1

    # Solicitar ao usuário o número do cadastro a ser alterado
    num_cadastro = int(input("\033[36mDIGITE O NÚEMERO DO CADASTRO QUE DESEJA ALTERAR: \033[0m")) - 1

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
                          '4 - [ENDEREÇO]\n'
                          '5 - [BAIRRO]\n'
                          '6 - [CIDADE]\n'
                          '7 - [ESTADO]\n'
                          '8 - [NOME_RESPOSÁVEL]\n'
                          '9 - [NOME_ESCOLA]\n'
                          '10 - [SERIE_ESCOLA]\n'
                          '11 - [TORCIDA]\n'
                          '12 - [POSIÇÃO]\n'
                          '13 - [IDOLO]\n'
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
            novo_endereco = input('NOVO ENDEREÇO: ')
            dados[cadastro+6] = f"Endereço: {novo_endereco}\n"
        elif opcao == 5:
            novo_bairro = input('NOVO BAIRRO: ')
            dados[cadastro+7] = f"Bairro: {novo_bairro}\n"
        elif opcao == 6:
            nova_cidade = input('NOVA CIDADE: ')
            dados[cadastro+8] = f"Cidade: {nova_cidade}\n"
        elif opcao == 7:
            novo_estado = input('NOVO ESTADO: ')
            dados[cadastro+9] = f"Estado: {novo_estado}\n"
        elif opcao == 8:
            novo_nome_responsavel = input('NOME DO RESPONSÁVEL: ')
            dados[cadastro+10] = f"Nome do Responsável: {novo_nome_responsavel}\n"
        elif opcao == 9:
            novo_nome_escola = input('NOME DA NOVA ESCOLA: ')
            dados[cadastro+16] = f"Nome da Escola: {novo_nome_escola}\n"
        elif opcao == 10:
            nova_serie_escola = input('NOVA SÉRIE ESCOLAR: ')
            dados[cadastro+17] = f"Série Escolar: {nova_serie_escola}\n"
        elif opcao == 11:
            nova_torcida = input('NOVA TORCIDA: ')
            dados[cadastro+18] = f"Torcida: {nova_torcida}\n"
        elif opcao == 12:
            nova_posicao = input('NOVA POSIÇÃO: ')
            dados[cadastro+20] = f"Posição: {nova_posicao}\n"
        elif opcao == 13:
            novo_idolo = input('NOVO ÍDOLO: ')
            dados[cadastro+21] = f"Ídolo: {novo_idolo}\n"
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

    arquivo.seek(0)
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

    # Solicitar ao usuário o número do cadastro a ser alterado
    num_cadastro = int(input("DIGITE O NUMERO DO CADASTRO QUE VOCÊ DESEJA APAGAR: ")) - 1

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
                            '4 - [ENDEREÇO]\n'
                            '5 - [BAIRRO]\n'
                            '6 - [CIDADE]\n'
                            '7 - [ESTADO]\n'
                            '8 - [NOME_RESPOSÁVEL]\n'
                            '9 - [NOME_ESCOLA]\n'
                            '10 - [SERIE_ESCOLA]\n'
                            '11 - [TORCIDA]\n'
                            '12 - [POSIÇÃO]\n'
                            '13 - [IDOLO]\n'
                            'ESCOLHA UM DESSES: '))

        if opcao == 1:
            dados[inicio_cadastro] = 'Nome: \n'
        elif opcao == 2:
            dados[inicio_cadastro + 1] = 'Número: \n'
        elif opcao == 3:
            dados[inicio_cadastro + 2] = 'E-mail: \n'
        elif opcao == 4:
            dados[inicio_cadastro + 6] = 'Endereço: \n'
        elif opcao == 5:
            dados[inicio_cadastro + 7] = 'Bairro: \n'
        elif opcao == 6:
            dados[inicio_cadastro + 8] = 'Cidade: \n'
        elif opcao == 7:
            dados[inicio_cadastro + 9] = 'Estado: \n'
        elif opcao == 8:
            dados[inicio_cadastro + 10] = 'Nome do Responsável: \n'
        elif opcao == 9:
            dados[inicio_cadastro + 16] = 'Nome da Escola: \n'
        elif opcao == 10:
            dados[inicio_cadastro + 17] = 'Série na Escola: \n'
        elif opcao == 11:
            dados[inicio_cadastro + 18] = 'Torcida: \n'
        elif opcao == 12:
            dados[inicio_cadastro + 20] = 'Posição: \n'
        elif opcao == 13:
            dados[inicio_cadastro + 21] = 'Ídolo: \n'
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
    arquivo.truncate()  # remove as linhas remanescentes do conteúdo anterior, garantindo que apenas os dados atualizados permaneçam no arquivo.

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
    arquivo_aberto = None

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
            arquivo_aberto = open("Dados.txt", "w")
            cadastrar_dados()
            arquivo_aberto.close()

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
