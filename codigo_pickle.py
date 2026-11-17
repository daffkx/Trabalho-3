import pickle
import os

class Usuario:
    def __init__(self, nome, cpf, email, cargo, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cargo = cargo
        self.senha = senha

class Escala:
    def __init__(self, participante, data_inicio, data_fim):
        self.participante = participante
        self.data_inicio = data_inicio
        self.data_fim = data_fim

class Mensagem:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto

    def exibir(self):
        return f"{self.autor}: {self.texto}"

class Atestado:
    def __init__(self, tipo, inicio, fim, documento):
        self.tipo = tipo
        self.inicio = inicio
        self.fim = fim
        self.documento = documento

class Sistema:
    def __init__(self):
        self.usuarios = {}
        self.usuario_logado = None
        self.escalas = []
        self.mensagens = []
        self.atestados = []

        self.carregar_dados()

# pickle

    def salvar_dados(self):
        print("Salvando...")

        dados = {
            "usuarios": self.usuarios,
            "escalas": self.escalas,
            "mensagens": self.mensagens,
            "atestados": self.atestados
        }

        with open("dados.pkl", "wb") as arquivo:
            pickle.dump(dados, arquivo)

        print(os.path.abspath("dados.pkl"))
        print("Salvo!")

    def carregar_dados(self):
        print("Carregando Dados...")

        if os.path.exists("dados.pkl"):
            print("Arquivo encontrado.")

            with open("dados.pkl", "rb") as arquivo:
                dados = pickle.load(arquivo)

            print("Dados carregados com sucesso!")

            self.usuarios = dados.get("usuarios", {})
            self.escalas = dados.get("escalas", [])
            self.mensagens = dados.get("mensagens", [])
            self.atestados = dados.get("atestados", [])

# cadastro e login

    def cadastrar(self):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        email = input("Digite seu e-mail: ")
        cargo = input("Digite seu cargo: ")
        senha = input("Crie uma senha: ")

        usuario = Usuario(nome, cpf, email, cargo, senha)

        self.usuarios[email] = usuario

        self.salvar_dados()

        print("Cadastro realizado com sucesso!")

    def login(self):
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        if email in self.usuarios and self.usuarios[email].senha == senha:
            self.usuario_logado = self.usuarios[email]
            print("Login realizado com sucesso!")
            return True

        print("Usuário ou senha incorretos.")
        return False

# perfil

    def ver_perfil(self):

        if self.usuario_logado is None:
            print("Nenhum usuário logado.")
            return

        usuario = self.usuario_logado

        print("\n--- INFORMAÇÕES DO PERFIL ---")
        print("Nome:", usuario.nome)
        print("E-mail:", usuario.email)
        print("CPF:", usuario.cpf)
        print("Cargo:", usuario.cargo)

# escalas

    def criar_escala(self):

        participante = input("Nome do participante: ")
        data_inicio = input("Data de início da escala: ")
        data_fim = input("Data de fim da escala: ")

        escala = Escala(
            participante,
            data_inicio,
            data_fim
        )

        self.escalas.append(escala)

        self.salvar_dados()

        print("Escala cadastrada com sucesso!")

    def ver_escalas(self):

        if len(self.escalas) == 0:
            print("Nenhuma escala cadastrada.")
            return

        print("\n--- ESCALAS ---")

        for i, escala in enumerate(self.escalas):

            print(f"\nEscala {i}")

            print("Data de início:", escala.data_inicio)
            print("Data de fim:", escala.data_fim)
            print("Participante:", escala.participante)

    def alterar_escala(self):

        if len(self.escalas) == 0:
            print("Nenhuma escala cadastrada.")
            return

        self.ver_escalas()

        try:
            i = int(input("\nNúmero da escala: "))

            if 0 <= i < len(self.escalas):

                self.escalas[i].participante = input(
                    "Novo participante: "
                )

                self.escalas[i].data_inicio = input(
                    "Nova data de início: "
                )

                self.escalas[i].data_fim = input(
                    "Nova data de fim: "
                )

                self.salvar_dados()

                print("Escala alterada com sucesso!")

            else:
                print("Escala não encontrada.")

        except ValueError:
            print("Digite um número válido.")

    def excluir_escala(self):

        if len(self.escalas) == 0:
            print("Nenhuma escala cadastrada.")
            return

        self.ver_escalas()

        try:
            i = int(input("\nNúmero da escala: "))

            if 0 <= i < len(self.escalas):

                self.escalas.pop(i)

                self.salvar_dados()

                print("Escala excluída com sucesso!")

            else:
                print("Escala não encontrada.")

        except ValueError:
            print("Digite um número válido.")

# chat

    def visualizar_chat(self):

        print("\n--- HISTÓRICO DO CHAT ---")

        if len(self.mensagens) == 0:
            print("Nenhuma mensagem enviada.")
            return

        for mensagem in self.mensagens:
            print(mensagem.exibir())

    def enviar_mensagem(self):

        if self.usuario_logado is None:
            print("Faça login primeiro.")
            return

        texto = input("Digite sua mensagem: ")

        mensagem = Mensagem(
            self.usuario_logado.nome,
            texto
        )

        self.mensagens.append(mensagem)

        self.salvar_dados()

        print("Mensagem enviada com sucesso!")

# exportar arquivo

    def exportar_arquivo(self):

        if len(self.escalas) == 0:
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

            for escala in self.escalas:

                arquivo.write(
                    f"Data de início: {escala.data_inicio}\n"
                )

                arquivo.write(
                    f"Data de fim: {escala.data_fim}\n"
                )

                arquivo.write(
                    f"Participante: {escala.participante}\n\n"
                )

        print("Arquivo exportado com sucesso!")
        print("Nome do arquivo: relatorio_escalas.txt")

# atestado ou declaração

    def aplicar_atestado(self):

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

        atestado = Atestado(
            tipo,
            inicio,
            fim,
            documento
        )

        self.atestados.append(atestado)

        self.salvar_dados()

        print(
            "Atestado/declaração registrado com sucesso!"
        )

    def visualizar_atestados(self):

        print("\n--- DOCUMENTOS REGISTRADOS ---")

        if len(self.atestados) == 0:
            print("Nenhum documento registrado.")
            return

        for atestado in self.atestados:

            print("\nTipo:", atestado.tipo)
            print("Início:", atestado.inicio)
            print("Fim:", atestado.fim)
            print("Documento:", atestado.documento)

# menu

    def menu_principal(self):

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
            print("0 - Logout")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.ver_perfil()

            elif opcao == "2":
                self.criar_escala()

            elif opcao == "3":
                self.ver_escalas()

            elif opcao == "4":
                self.alterar_escala()

            elif opcao == "5":
                self.excluir_escala()

            elif opcao == "6":
                self.visualizar_chat()

            elif opcao == "7":
                self.enviar_mensagem()

            elif opcao == "8":
                self.exportar_arquivo()

            elif opcao == "9":
                self.aplicar_atestado()

            elif opcao == "10":
                self.visualizar_atestados()

            elif opcao == "0":
                print("Logout realizado.")
                self.usuario_logado = None
                break

            else:
                print("Opção inválida.")

    def executar(self):

        while True:

            print("\n===== ACESSO =====")
            print("1 - Cadastrar")
            print("2 - Fazer login")
            print("0 - Encerrar sistema")

            opcao = input("Escolha: ")

            if opcao == "1":

                self.cadastrar()

            elif opcao == "2":

                if self.login():
                    self.menu_principal()

            elif opcao == "0":

                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida.")


# iniciar

if __name__ == "__main__":
    sistema = Sistema()
    sistema.executar()