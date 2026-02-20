
"""
Crie um programa que:
    1. Comece com uma lista vazia chamada tarefas
    2. Permita adicionar 5 tarefas digitadas pelo usuário
    3. Mostre todas numeradas
    4. Permita marcar uma como concluída (remover da lista)
    5. Mostre a lista atualizada
💡 Extra intermediário:
    • Ordenar tarefas alfabeticamente
    • Mostrar quantidade restante
    • Permitir marcar mais de uma tarefa como concluída
    • Permitir adicionar mais tarefas depois de marcar como concluídas
"""

# Menu_inicial
print()
print("Bem-vindo ao Gerenciador de Tarefas!")
print()

opcao = 0
tarefas = []

while opcao != 4:
    print()
    print("***********************************")
    print("*1. Adicionar tarefas             *")
    print("*2. Mostrar tarefas               *")
    print("*3. Marcar tarefa como concluída  *")
    print("*4. Sair                          *")
    print("***********************************")
    print()

    opcao = int(input("Escolha uma opção: "))
    print()

    if opcao == 1:
        for i in range(5):
            tarefa = input(f"Digite a tarefa {i + 1}: ")
            tarefas.append(tarefa)
        print("Resultado: Tarefas adicionadas com sucesso!")
        print(f"Quantidade de tarefas: {len(tarefas)}")

    elif opcao == 2:
        if tarefas:
            print("Tarefas atuais:")
            print(f"Quantidade de tarefas: {len(tarefas)}")
            for idx, tarefa in enumerate(tarefas, start=1):
                print(f"{idx}. {tarefa}")
        else:
            print("Resultado: Nenhuma tarefa na lista.")
    elif opcao == 3:
        if tarefas:
            print(f"Quantidade de tarefas: {len(tarefas)}")
            print("Tarefas atuais:")
            for idx, tarefa in enumerate(tarefas, start=1):
                print(f"{idx}. {tarefa}")
            tarefa_concluida = 
            int(input("Digite o número da tarefa concluída: "))
            if 1 <= tarefa_concluida <= len(tarefas):
                tarefas.pop(tarefa_concluida - 1)
                print("Resultado: Tarefa marcada como concluída!")
                print(f"Quantidade de tarefas: {len(tarefas)}")
            else:
                print("Resultado: Número de tarefa inválido.")
        else:
            print("Resultado: Nenhuma tarefa para marcar como concluída.")
    elif opcao == 4:
        print("Resultado: Saindo do Gerenciador de Tarefas. Até mais!")
    else:     
        print("Resultado: Opção inválida. Por favor, escolha uma opção válida.")