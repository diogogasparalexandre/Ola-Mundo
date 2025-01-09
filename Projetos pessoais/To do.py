# -*- coding: utf-8 -*-
import os
#Mensagem de boas-vindas e Menu de opções

#to do: carregar tarefas e adicionar tarefas
#Criar arquivo tarefas.txt
pergunta = input("Deseja criar um arquivo? (S/N): ").upper()
if pergunta == "S":
    temp = input("Please Enter File Name to create: ")
    if not temp.endswith(".txt"):
        temp += ".txt"
    if os.path.exists(temp):
        print("File already exists!")
    else:
        with open(temp, "w") as FileName:
            print("File Created!"+"\n")
else:
    pass


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

#carregar tarefas



#Recolher a escolha do usuário
def ver_tarefas():
    if len(tarefas) == 0:
        print('Nenhuma tarefa CADASTRADA')
    else:
        for i, tarefa in enumerate(tarefas):
            status = 'Concluida' if tarefa['Concluida'] else 'Pendente'
            print(f'{i+1} - {tarefa["Nome"]} - {status}')

#Adicionar tarefa
def adicionar_tarefa():
    tarefa = input('Digite a tarefa: ').title().strip()
    if any(t['Nome'] == tarefa for t in tarefas):
        print('Tarefa duplicada. Por favor, escolha outra tarefa.')
        return
    tarefas.append({'Nome': tarefa, 'Concluida': False})
    print('({}) adicionada com sucesso!'.format(tarefa))

#Rmover tarefa
def remover_tarefa():
    ver_tarefas()
    try:
        escolha = int(input('Escolha a tarefa que deseja remover: '))
        if escolha > 0 and escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            print('({}) removida com sucesso!'.format(tarefa_removida['Nome']))
        else:
            print('Tarefa inválida. Por favor, escolha uma tarefa válida.')
    except ValueError:
        print('Opção inválida. Por favor, escolha uma opção válida.')

#Modificar tarefa
def modificar_tarefa():
    ver_tarefas()
    try:
        escolha = int(input('Escolha a tarefa que deseja modificar: '))
        if escolha > 0 and escolha <= len(tarefas):
            tarefa_modificada = tarefas[escolha - 1]
            tarefa_modificada['Concluida'] = not tarefa_modificada['Concluida']
            print('Tarefa modificada com sucesso!')
        else:
            print('Tarefa inválida. Por favor, escolha uma tarefa válida.')
    except ValueError:
        print('Opção inválida. Por favor, escolha uma opção válida.')

#Programa principal
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
            remover_tarefa()
        elif escolha == 4:
            modificar_tarefa()
        elif escolha == 5:
            print('Sair')
            print('Obrigado por usar o programa!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
    except ValueError:
        print('Opção inválida. Por favor, escolha uma opção válida.')
