# -*- coding: utf-8 -*-
#Funçoes
#Mensagem de boas-vindas e Menu de opções
def menu():
    print('-'*40)
    print('LISTA DE TAREFAS'.center(40))
    print('-'*40)
    print('1 - Ver tarefas'.ljust(40))
    print('2 - Adicionar tarefa'.ljust(40))
    print('3 - Remover tarefa'.ljust(40))
    print('4 - Modificar tarefa'.ljust(40))
    print('5 - Sair'.ljust(40))
    print('-'*40)


#Recolher a escolha do usuário
def ver_tarefas():
    if len(tarefas) == 0:
        print('Nenhuma tarefa CADASTRADA')
    else:
        for i, tarefa in enumerate(tarefas):
            status = 'Concluida' if tarefa['Concluida'] else 'Pendente'
            print(f'{i+1} - {tarefa["Nome"]} - {status}')

def adicionar_tarefa():
    tarefa = input('Digite a tarefa: ').title().strip()
    if any(t['Nome'] == tarefa for t in tarefas):
        print('Tarefa duplicada. Por favor, escolha outra tarefa.')
        return
    tarefas.append({'Nome': tarefa, 'Concluida': False})
    print('({}) adicionada com sucesso!'.format(tarefa))
    
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
            print('Modificar tarefa')
        elif escolha == 5:
            print('Sair')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
    except ValueError:
        print('Opção inválida. Por favor, escolha uma opção válida.')


