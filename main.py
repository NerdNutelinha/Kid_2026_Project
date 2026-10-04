Clinica_Cores

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"

Clinica_Cadastro de Pacientes

pacientes = []

def cadastrar_paciente():
    print( f"\n{CYAN}{BOLD}--- CADASTRO DE PACIENTE ---{RESET}" )
    nome = input("Nome do paciente: ").strip()

while True:
    try: 
        idade = int(input("Idade: "))
        if idade < 0:
            print( f"{RED}A idade não pode ser negativa. Tente novamente.{RESET}" )
            continue
        break
    except ValueError:
        print( f"{RED}Por favor, digite um número válido para a idade.{RESET}" )
    telefone = input("Telefone: ").strip()
    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    pacientes.append(paciente)
    print( f"\n{GREEN}✔ Paciente '{nome}' cadastrado com sucesso!{RESET}" )

Clinica_Ver Estatísticas

def ver_estatisticas():
    print( f"\n{MAGENTA}{BOLD}--- ESTATÍSTICAS DA CLÍNICA ---{RESET}" )

    if len(pacientes) == 0:
        print( f"{YELLOW}Nenhum paciente cadastrado até o momento.{RESET}" )
        return

    total = len(pacientes)
    soma_idades = sum( p["idade"] for p in pacientes )
    media_idade = soma_idades / total

    paciente_mais_novo = min( pacientes, key=lambda p: p["idade"] )
    paciente_mais_velho = max( pacientes, key=lambda p: p["idade"] )

    print( f"Total de pacientes cadastrados: {BOLD}{total}{RESET}" )
    print( f"Idade média dos pacientes: {BOLD}{media_idade:.1f} anos{RESET}" )
    print( f"Paciente mais novo: {BLUE}{paciente_mais_novo['nome']}{RESET} ({paciente_mais_novo['idade']} anos)" )
    print( f"Paciente mais velho: {BLUE}{paciente_mais_velho['nome']}{RESET} ({paciente_mais_velho['idade']} anos)" )

Clinica_Buscar Pacientes

def buscar_paciente():
    print( f"\n{CYAN}{BOLD}--- BUSCAR PACIENTE ---{RESET}" )
    if len(pacientes) == 0:
        print( f"{YELLOW}Nenhum paciente cadastrado.{RESET}" )
        return

    nome_busca = input( "Digite o nome do paciente que deseja buscar: " ).strip()
    encontrados = [p for p in pacientes if nome_busca.lower() in p["nome"].lower()]

    if encontrados:
        print( f"\n{GREEN}Paciente(s) encontrado(s):{RESET}" )
        for p in encontrados:
            print( f"- Nome: {BOLD}{p['nome']}{RESET} | Idade: {p['idade']} | Telefone: {p['telefone']}" )
    else:
        print( f"{RED}Nenhum paciente encontrado com o nome '{nome_busca}'.{RESET}" )

Clinica_Listar Pacientes

def listar_pacientes():
    print( f"\n{BLUE}{BOLD}--- LISTA DE PACIENTES REGISTRADOS ---{RESET}" )
    if len(pacientes) == 0:
        print( f"{YELLOW}Nenhum paciente cadastrado.{RESET}" )
        return

    for idx, p in enumerate(pacientes, start=1):
        print( f"{BOLD}{idx}.{RESET} Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}" )

def main():
    while True:
        print( f"\n{BOLD}{CYAN}=== SISTEMA CLÍNICA VIDA+ ==={RESET}" )
        print( f"{GREEN}1.{RESET} Cadastrar paciente" )
        print( f"{GREEN}2.{RESET} Ver estatísticas" )
        print( f"{GREEN}3.{RESET} Buscar paciente" )
        print( f"{GREEN}4.{RESET} Listar todos os pacientes" )
        print( f"{RED}5.{RESET} Sair" )

        opcao = input( "\nEscolha uma opção: " ).strip()

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print( f"\n{YELLOW}Saindo do sistema... Até logo!{RESET}\n" )
            break
        else:
            print( f"{RED}Opção inválida! Por favor, escolha um número de 1 a 5.{RESET}" )

if __name__ == "__main__":
    main()
