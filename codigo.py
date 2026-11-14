usuarios = {}
usuario_logado = None

escalas = []
mensagens = []
atestados = []

# cadastro e login do usuário

def cadastrar():

    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu e-mail: ")
    cargo = input("Digite seu cargo: ")
    senha = input("Crie uma senha: ")

    usuarios[email] = {
        "nome": nome,
        "cpf": cpf,
        "cargo": cargo,
        "senha": senha
    }

    print("Cadastro realizado com sucesso!")

def login():

    global usuario_logado

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if email in usuarios and usuarios[email]["senha"] == senha:
        usuario_logado = email
        print("Login realizado com sucesso!")
        return True

    print("Usuário ou senha incorretos.")
    return False

# funções do perfil do usuário

def ver_perfil():

    if usuario_logado is None:
        print("Nenhum usuário logado.")
        return

    usuario = usuarios[usuario_logado]

    print("\n--- INFORMAÇÕES DO PERFIL ---")
    print("Nome:", usuario["nome"])
    print("E-mail:", usuario_logado)
    print("CPF:", usuario["cpf"])
    print("Cargo:", usuario["cargo"])

# funções de escala

def criar_escala():

    participante = input("Nome do participante: ")

    data_inicio = input("Data de início da escala: ")
    data_fim = input("Data de fim da escala: ")

    escala = {
        "data inicio": data_inicio,
        "data fim": data_fim,
        "participante": participante
    }

    escalas.append(escala)

    print("Escala cadastrada com sucesso!")

def ver_escalas():

    if len(escalas) == 0:
        print("Nenhuma escala cadastrada.")
        return

    print("\n--- ESCALAS ---")

    for i, escala in enumerate(escalas):

        print(f"\nEscala {i}")

        print("Data de início:", escala["data inicio"])
        print("Data de fim:", escala["data fim"])
        print("Participante:", escala["participante"])

def alterar_escala():

    if len(escalas) == 0:
        print("Nenhuma escala cadastrada.")
        return

    ver_escalas()

    i = int(input("\nNúmero da escala: "))

    if 0 <= i < len(escalas):

        escalas[i]["participante"] = input(
            "Novo participante: "
        )

        escalas[i]["data inicio"] = input(
            "Nova data de início: "
        )

        escalas[i]["data fim"] = input(
            "Nova data de fim: "
        )

        print("Escala alterada com sucesso!")

    else:
        print("Escala não encontrada.")

def excluir_escala():

    if len(escalas) == 0:
        print("Nenhuma escala cadastrada.")
        return

    ver_escalas()

    i = int(input("\nNúmero da escala: "))

    if 0 <= i < len(escalas):

        escalas.pop(i)

        print("Escala excluída com sucesso!")

    else:
        print("Escala não encontrada.")

# funções do chat

def visualizar_chat():

    print("\n--- HISTÓRICO DO CHAT ---")

    if len(mensagens) == 0:
        print("Nenhuma mensagem enviada.")
        return

    for mensagem in mensagens:
        print(mensagem)

def enviar_mensagem():

    usuario = usuarios[usuario_logado]["nome"]

    mensagem = input("Digite sua mensagem: ")

    mensagens.append(usuario + ": " + mensagem)

    print("Mensagem enviada com sucesso!")

#funções pra exportar arquivo

def exportar_arquivo():

    if len(escalas) == 0:
        print("Nenhuma escala para exportar.")
        return

    with open(
        "relatorio_escalas.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "--- RELATÓRIO DE ESCALAS ---\n\n"
        )

        for escala in escalas:

            arquivo.write(
                "Data de início: "
                + escala["data inicio"]
                + "\n"
            )

            arquivo.write(
                "Data de fim: "
                + escala["data fim"]
                + "\n"
            )

            arquivo.write(
                "Participante: "
                + escala["participante"]
                + "\n\n"
            )

    print("Arquivo exportado com sucesso!")
    print("Nome do arquivo: relatorio_escalas.txt")

# funções de atestado ou declaração

def aplicar_atestado():

    tipo = input(
        "Tipo (Atestado ou Declaração): "
    )

    inicio = input(
        "Data de início: "
    )

    fim = input(
        "Data de término: "
    )

    documento = input(
        "Nome do arquivo digital: "
    )

    if tipo.lower() not in [
        "atestado",
        "declaração",
        "declaracao"
    ]:

        print("Tipo inválido.")
        return

    atestado = {
        "tipo": tipo,
        "inicio": inicio,
        "fim": fim,
        "documento": documento
    }

    atestados.append(atestado)

    print(
        "Atestado/declaração registrado com sucesso!"
    )

def visualizar_atestados():

    print("\n--- DOCUMENTOS REGISTRADOS ---")

    if len(atestados) == 0:
        print("Nenhum documento registrado.")
        return

    for atestado in atestados:

        print("\nTipo:", atestado["tipo"])
        print("Início:", atestado["inicio"])
        print("Fim:", atestado["fim"])
        print("Documento:", atestado["documento"])

# menu quando você já tá logado

def menu_principal():

    while True:

        print("\n========== MENU ==========")
        print("1 - Ver informações do perfil")
        print("2 - Criar escala")
        print("3 - Visualizar escalas")
        print("4 - Alterar escala")
        print("5 - Excluir escala")
        print("6 - Ver chat")
        print("7 - Enviar mensagem")
        print("8 - Exportar arquivo")
        print("9 - Aplicar atestado/declaração")
        print("10 - Visualizar documentos")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            ver_perfil()

        elif opcao == "2":
            criar_escala()

        elif opcao == "3":
            ver_escalas()

        elif opcao == "4":
            alterar_escala()

        elif opcao == "5":
            excluir_escala()

        elif opcao == "6":
            visualizar_chat()

        elif opcao == "7":
            enviar_mensagem()

        elif opcao == "8":
            exportar_arquivo()

        elif opcao == "9":
            aplicar_atestado()

        elif opcao == "10":
            visualizar_atestados()

        elif opcao == "0":

            print("Logout realizado.")
            break

        else:
            print("Opção inválida.")

# menu pra cadastrar ou logar

while True:

    print("\n===== ACESSO =====")
    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("0 - Encerrar sistema")

    opcao = input("Escolha: ")

    if opcao == "1":

        cadastrar()

    elif opcao == "2":

        if login():
            menu_principal()

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida.")