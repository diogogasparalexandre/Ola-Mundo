# -*- coding: utf-8 -*-
import os
#Mensagem de boas-vindas e Menu de opções
<<<<<<< Updated upstream

#to do: carregar tarefas e adicionar tarefas
#Criar arquivo tarefas.txt
def criar_arquivo():
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
        temp=input('Indique o nome do arquivo: ').title()
        if not temp.endswith('.txt'):
            temp += '.txt'
        if not os.path.exists(temp):
            print("Arquivo não encontrado. Criando novo arquivo.")
            with open(temp, "w") as arquivo:
                pass
    return temp
    

def carregar_tarefas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            tarefas = []
            for linha in arquivo:
                if linha.strip():  # Ignora linhas vazias
                    nome, concluida = linha.strip().split('|')
                    tarefas.append({
                        'Nome': nome,
                        'Concluida': concluida == 'True'
                    })
        return tarefas
    except FileNotFoundError:
        return []

def salvar_tarefas(nome_arquivo, tarefas):
    with open(nome_arquivo, 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['Nome']}|{tarefa['Concluida']}\n")

# Modificar o programa principal para usar o arquivo
nome_arquivo = criar_arquivo()
tarefas = carregar_tarefas(nome_arquivo)

=======
# -*- coding: utf-8 -*-
>>>>>>> Stashed changes
def menu():
    print("=" * 40)
    print("SISTEMA DE GERENCIAMENTO DE TAREFAS".center(40))
    print("=" * 40)
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Modificar tarefa")
    print("5 - Sair")
    print("=" * 40)

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
    salvar_tarefas(nome_arquivo, tarefas)
    print('({}) adicionada com sucesso!'.format(tarefa))

#Rmover tarefa
def remover_tarefa():
    ver_tarefas()
    try:
        escolha = int(input('Escolha a tarefa que deseja remover: '))
        if escolha > 0 and escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            salvar_tarefas(nome_arquivo, tarefas)
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
            salvar_tarefas(nome_arquivo, tarefas)
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
