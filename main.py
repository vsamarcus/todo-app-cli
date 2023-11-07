import argparse
import json

ALLOWED_STATES = ["Concluído", "Removido", "Em andamento", "Parado", "Novo", "Em planejamento"]

def create_task(name, description, state="Novo"):
    # Verifica se o estado é válido
    if state not in ALLOWED_STATES:
        print(f"O estado '{state}' não é permitido. Estados permitidos: {', '.join(ALLOWED_STATES)}")
        return
    
    if state == "Removido":
        print("Não é permitido definir uma tarefa como 'Removida' ou 'Concluída' durante a criação.")
        return

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    # Cria a nova tarefa
    new_task = {"name": name, "description": description, "state": state}

    # Adiciona a nova tarefa à lista de tarefas
    tasks.append(new_task)

    # Salva as tarefas de volta no arquivo JSON
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"Nova tarefa criada - Nome: {name}, Descrição: {description}, Estado: {state}")

def list_tasks(all_tasks, task_name):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        if not tasks:
            print("Nenhuma tarefa encontrada.")
        else:
            if all_tasks:
                # Listar todas as tarefas
                for i, task in enumerate(tasks):
                    print(f"Tarefa {i + 1} - Nome: {task['name']}, Descrição: {task['description']}")
            elif task_name:
                # Filtrar por nome da tarefa
                found = False
                for i, task in enumerate(tasks):
                    if task['name'] == task_name:
                        print(f"Tarefa {i + 1} - Nome: {task['name']}, Descrição: {task['description']}")
                        found = True
                        break
                if not found:
                    print(f"Nenhuma tarefa com o nome '{task_name}' encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description="Gerenciador de tarefas")
subparsers = parser.add_subparsers(dest="command")

# Subcomando para criar uma nova tarefa
create_parser = subparsers.add_parser("create")
create_parser.add_argument("--name", required=True, help="Nome da tarefa")
create_parser.add_argument("--description", required=True, help="Descrição da tarefa")
create_parser.add_argument("--state", choices=ALLOWED_STATES, default="Novo", help="Estado da tarefa")

list_parser = subparsers.add_parser("list")
list_parser.add_argument("--all", action="store_true", help="Listar todas as tarefas")
list_parser.add_argument("--name", help="Filtrar tarefas pelo nome")

# Analisa os argumentos da linha de comando
args = parser.parse_args()

if args.command == "create":
    create_task(args.name, args.description, args.state)
elif args.command == "list":
    list_tasks(args.all, args.name)
else:
    print("Comando não reconhecido. Use 'create' para criar uma nova tarefa.")
