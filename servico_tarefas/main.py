print("Sistema de Gestion de Tareas")


# tarefa = {
#     "id": 1,
#     "titulo": "Estudiar python",
#     "completada": False
# }


tarefas = [
    {
    "id": 1,
    "titulo": "Estudiar python",
    "completada": False
},
{
    "id": 2,
    "titulo": "Aprender SQL",
    "completada": False
},
{
    "id": 3,
    "titulo": "Estudiar sobre IA",
    "completada": False
}


]

# nova_tarefa = {
#     "id": 4,
#     "titulo": "Aprender funciones",
#     "completada": False
# }

# tarefas.append(nova_tarefa)
nova_t = None
while True :
    print("\n====== GESTOR DE TAREFAS ======")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print()
    print()
    print()


    opcao = int(input("Elige una opción: "))

    if opcao == 1:
        nome_t = input("Digite sua nova tarefa: ")
        nova_t = {
            "id": max((tarea["id"] for tarea in tarefas), default=0) + 1,
            "titulo": nome_t,
            "completada": False
        }
        tarefas.append(nova_t)
        print("Tarefa Salva com sucesso")
    elif opcao == 2:
        print(tarefas)
    elif opcao == 3:
        print(tarefas)
        id_tarefas = int(input("Digite o ID da tarefa que deseja marcar como terminada: "))
        encontrada = False

        for tarefa in tarefas:
            if tarefa["id"] == id_tarefas:
                tarefa["completada"] = True
                encontrada = True
                print("Tarefa marcada como completada.")
                break

        if not encontrada:
                print("Não existe tarefa com esse ID")

    elif opcao == 4:
        print(tarefas)
        id_tarefa = int(input("Digite o ID da tarefa que deseja eliminar: "))
        encontrada = False

        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefas.remove(tarefa)
                encontrada = True
                print("Tarefa eliminada com sucesso.")
                break

        if not encontrada:
            print("Nao existe tarefa com esse ID.")


    elif opcao == 5:
        print("Sistema finalizado!")
        break 
else:
    print("Ops! Algo deu errado")
        

    

