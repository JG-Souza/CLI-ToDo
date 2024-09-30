lista_tarefas = []

def ver_tarefa():
    if len(lista_tarefas) == 0:
        print('=' * 32)
        print('Nenhuma tarefa adicionada ainda.')
        print('=' * 32)
    else:
        print('=' * 20)
        for tarefa in lista_tarefas:
            print(tarefa)
            print('*' * 20)
        print('=' * 20)


def add_tarefa():
    tarefa = str(input('Qual a tarefa? '))
    print('=' * 28)
    lista_tarefas.append(tarefa)


def edit_tarefa():
    print('=' * 20)
    print('Qual tarefa voce quer editar? ')
    for i, tarefa in enumerate(lista_tarefas):
        print(f'{i}: {tarefa}')
    escolha = int(input('->'))
    print('=' * 20)

    if 0 <= escolha <len(lista_tarefas):
        tarefa = lista_tarefas[escolha]
        acao = int(input(('''
    1. Marcar como concluída
    2. Excluir
    -> ''')))


        if acao == 1:
            if ' (Concluída)' in lista_tarefas[escolha]:
                print('A tarefa já está concluída.')
                print('=' * 20)
            else:
                lista_tarefas[escolha] = tarefa + ' (Concluída)'
                ver_tarefa()
        if acao == 2:
            lista_tarefas.remove(tarefa)
            if len(lista_tarefas) == 0:
                print('A lista agora está vazia.')
                print('=' * 20)
            else:
                ver_tarefa()
    else:
        print('Escolha inválida. Tente novamente.')
    
