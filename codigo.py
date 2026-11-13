#Fazer login/cadastrar

usuario = {}

def cadastar():
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu e-mail: ")
    senha = input("Crie uma senha: ")
    
    usuarios[email] = {
        "senha": senha,
        "cpf": cpf
    }
    
    print("cadastro realizado com sucesso!")
    
def login():
    email = input("Digite seu e-mail: ")
    senha = input ("Digite seu e-mail: ")

    if email in usuarios and usuarios[email]["senha"] == senha:
        print("Login realizado com sucesso!")
    else: 
        print("Usuário ou senha incorretos.") 
        
print("1 - Cadastrar")        
print("2 - Fazer login")

opcao = input("Escolha:")

if opcao == "1":
    cadastrar()
elif opcao == "2":
    login()

# Gerenciamento de informações de perfil

perfil = {}

def criar_perfil():
    perfil["nome"] = input("nome: ")
    perfil["cargo"] = input("cargo: ")
    print("Perfil criado!")

def consultar_perfil(): 
    print(perfil)

def alterar_perfil():
    campo = input("Qual informação deseja alterar? ")
    
    if campo in perfil:
        perfil[campo] = input("Digite o novo valor: ")
    else:
        print("Informação não encontrada. ")

def excluir_perfil():
    perfil.clear()
    print("Perfil excluído!")

print("""1 - Criar perfil
         2 - Consultar perfil
         3 - Alterar perfil
         4 - Excluir perfil""")

opcao = input("Escolha: ")

if opcao == "1":
    criar_perfil()
elif opcao == "2": 
    consultar_perfil()
elif opcao == "3":
    alterar_perfil()
elif opcao == "4":
    excluir_perfil()

# Ver informações de perfil 

perfil = {
    "nome" = "Patrícia B. Alves",
    "email" = "patriciatec123@gmail.com",
    "cpf" = "123-456-789-00",
    "cargo" = "Técnica em enfermagem"
}

def ver_perfil():
    print("\n--- INFORMAÇÕES DO PERFIL ---")
    print("Nome:", perfil["nome"])
    print("E-mail:", perfil["email"])
    print("CPF:", perfil["cpf"])
    print("Cargo:", perfil["cargo"])

ver_perfil()

# Gerenciar escalas(CRUD)

escalas = []

def criar_escala():
    data_inicio = input("Data do início da escala: ")
    data_fim = input("Data do fim da escala: ")
    participante = input("Participante: ")

    escala = {
        "data inicio": data_inicio,
        "data fim": data_fim,
        "participante": participante
    }
    
    escalas.append(escala)
    print("Escala cadastrada!")

def ver_escalas():
    for escala in escalas:
        print(escala)

def alterar_escala():
    i = int(input("Número da escala: "))
    
    if 0 <= i < len(escalas):
        escalas[i]["data inicio"] = input("Nova data do início da escala: ")
        escalas[i]["data fim"] = input("Nova data do fim da escala: ")
        print("Escala alterada!")
    else:
        print("Escala não encontrada.")

def excluir_escala():
    i = int(input("Número da escala: "))
    
    if 0 <= i < len(escalas):
        escalas.pop(i)
        print("Escala excluída!")
    else:
        print("Escala não encontrada. ")

print("""1 - Criar escala
         2 - Visualizar escalas
         3 - Alterar escala
         4 - Excluir escala""")

opcao = input("Escolha: ")

if opcao == "1": 
    criar_escala()
elif opcao == "2": 
    ver_escalas()
elif opcao == "3":
    alterar_escala()
elif opcao == "4":
    excluir_escala()
    
    
#Ver escalas
 
escalas = [
    {
        "data inicio": "27/04/2026"
        "data fim": "01/05/2026" 
        "participante": "Jorge"
    },
    {
        "data inicio": "04/05/2026"
        "data fim": "08/05/2026" 
        "participante": "Luna"
    },
    {
        "data inicio": "11/05/2026"
        "data fim": "15/05/2026" 
        "participante": "Patrícia"
    },
    {
        "data inicio": "18/05/2026"
        "data fim": "22/05/2026" 
        "participante": "Beto"
    },
    {
        "data inicio": "25/05/2026"
        "data fim": "29/05/2026" 
        "participante": "Jorge"
    },
    {
        "data inicio": "01/06/2026"
        "data fim": "05/06/2026" 
        "participante": "Luna"
    }
]

def ver_escala():
    print("n\--- ESCALA ---")
    
    for escala in escalas:
        print("Data de início:", escala["data inicio"])
        print("Data de fim:", escala["data fim"])
        print("Participante:", escala["participante"])
        
ver_escala()

# Ver/participar do chat 

mensagens = []

def visualizar_chat():
    print("\n--- HISTÓRICO DO CHAT ---")
    
    for mensagem in mensagens:
        print(mensagem)
        
def enviar_mensagem():
    usuario = input("Seu nome: ")
    mensagem = input("Digite sua mensagem: ")

    mensagens.append(usuario + ": " + mensagem)

    print("Mensagem enviada!")

while True:
    print("\n1 - Ver mensagens")
    print("2 - Enviar mensagem")
    print("3 - Sair")

    opcao = input("Escolha: ")
    
    if opcao == "1": 
        visualizar_chat()
    elif opcao == "2":
        enviar_mensagem()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")
        
#Exportat arquivo

escalas = [
    ["27/04/2026", "01/05/2026", "Jorge"]
    ["04/05/2026", "08/05/2026", "Luna"]
    ["11/05/2026", "15/05/2026", "Patrícia"]
    ["18/05/2026", "22/05/2026", "Beto"]
    ["25/05/2026", "29/05/2026", "Jorge"]
    ["01/06/2026", "05/06/2026", "Luna"]    
]

def exportar_arquivo():
    with open("--- RELATÓRIO DE ESCALAS ---\n\n")

        arquivo.writer("--- RELATÓRIO DE ESCALAS")
    
        for escala in esclas:
            arquivo.writer("Data de início: " + escala[0] + "\n")
            arquivo.writer("Data de fim: " + escala[1] + "\n") 
            arquivo.writer("Participante: " + escala[2] + "\n")
    
    print("Arquivo exportado com sucesso!")
    print("Nome do arquivo: relatorio_escalas.txt")
    
exportar_arquivo()    
    
# Aplicar atestado ou declaração 

atestados = []

def aplicar_atestado():
    tipo = input("Tipo (Atestado ou Declaração): ")
    inicio = input("Data de início: ")
    fim = input("Data de término: ")
    documento = input("Nome do arquivo digital: ")
    
    if tipo.lower() not in ["atestado", "declaração", "declaracao"]:
        print("Preencha todos os campos!")
        return
    
    atestado = {
        "tipo": tipo,
        "inicio": inicio,
        "fim": fim,
        "documento": documento
         }
    
    atestados.append(atestado)

    print("Atestado/declaração registrado com sucesso!")

def visualizar_atestados():
    print("\n--- DOCUMENTOS REGISTRADOS ---")
    
    for atestado in atestados:
        print(atestado)

print("1 - Aplicar atestado/declaração")
print("2 - Visualizar documentos")

opcao = input("Escolha: ")

if opcao == "1": 
    aplicar_atestado()
elif opcao == "2": 
    visualizar_atestados() 