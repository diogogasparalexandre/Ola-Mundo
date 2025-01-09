#Funçoes
#Mensagem de boas-vindas e Menu de opções
def menu():
    print('-'*40)
    print('LISTA DE TAREFAS'.center(40))
    print('-'*40)
    print('1 - Ver tarefas'.ljust(40))
    print('2 - Adicionar tarefa'.ljust(40))
    print('3 - Remover tarefa'.ljust(40))
    print('4 - Sair'.ljust(40))
    print('-'*40)

#Recolher a escolha do usuário

def ver_tarefas():
    if len(tarefas) == 0:
        print('Nenhuma tarefa CADASTRADA')
    else:
        for tarefa in tarefas:
            print(tarefa)

#Menu principal
tarefas = []
while True:
    menu()
    try:
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            print('Ver tarefas')
            ver_tarefas()
        elif escolha == 2:
            adicionar_tarefa()
        elif escolha == 3:
            print('Remover tarefa')
        elif escolha == 4:
            print('Sair')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
    except ValueError:
        print('Opção inválida. Por favor, escolha uma opção válida.')



