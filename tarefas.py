#Lista de tarefas
tarefas = [
    {"Título": "varrer", "Concluido": "sim", "Prioridade": "baixa"},
    {"Título": "lavar a louça", "Concluido": "não", "Prioridade": "alta"},
    {"Título": "passar pano", "Concluido": "não", "Prioridade": "baixa"},
    {"Título": "consertar a tv", "Concluido": "sim", "Prioridade": "alta"}
]
#Resoluções
def todas ():
    print(tarefas)


def concluido ():
    for tarefa in tarefas:
        if tarefa["Concluido"] == "sim":
            print(tarefa)

def pendentes ():
    for tarefa in tarefas:
        if tarefa["Concluido"] == "não":
            print(tarefa)

def prioridades ():
    pergunta = input("Prioridade alta ou baixa? ")
    for tarefa in tarefas:
        if tarefa["Prioridade"] == pergunta:
            print(tarefa)

def add ():
    print ("Adicione nova tarefa: ")
    nome_da_tarefa = input("Qual tarefa deseja adicionar? ")
    conclusão_da_tarefa = input("Você ja finalizou a tarefa? ")
    prioridade_da_tarefa = input("A prioridade da tarefa é alta ou baixa? ")

    nova_tarefa = {
        "nome": nome_da_tarefa,
        "conclusão": conclusão_da_tarefa,
        "prioridade": prioridade_da_tarefa
        }
    tarefas.append (nova_tarefa)
    print(tarefas)

def finalizar ():
    pendentes() 
    finalizar_tarefa = input("Digite a tarefa finalizada: ")
    for tarefa in tarefas:
        if  tarefa["Título"] == finalizar_tarefa:
            tarefa["Concluído"] = "sim"
            print(f"{tarefa["Título"]} - Concluída")

def Remover ():
    print(tarefas)
    remover_tarefa = input("Digite a tarefa que quer excluir ")
    for tarefa in tarefas:
        if tarefa["Título"] == remover_tarefa:
            tarefas.remove (tarefa)
            print(tarefas)


def sair ():
    print("Saindo do sistema...")

#Opções

while True:
    print("TAREFAS")
    print("1 - Mostrar Todas")
    print("2 - Mostrar Tarefas Concluídas")
    print("3 - Mostrar as Pendentes")
    print("4 - Mostrar Por Prioridades")
    print("5 - Adicionar Nova Tarefa")
    print("6 - Finalizar Tarefa")
    print("7 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        todas()

    elif opcao == "2":
        concluido()

    elif opcao == "3":
        pendentes()

    elif opcao == "4":
        prioridades()

    elif opcao == "5":
        add()

    elif opcao == "6":
        finalizar()

    elif opcao == "7":
        Remover()

    elif opcao == "0":
        sair()


