from create_task import create_task
from remove_task import remove_task
from list_task import list_tasks
from update_task import update_task, ALLOWED_STATES

import argparse

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description="Gerenciador de tarefas")
subparsers = parser.add_subparsers(dest="command")

# Subcomando para criar uma nova tarefa
create_parser = subparsers.add_parser("create")
create_parser.add_argument("--name", required=True, help="Nome da tarefa")
create_parser.add_argument("--description", required=True, help="Descrição da tarefa")
create_parser.add_argument("--state", choices=ALLOWED_STATES, default="Novo", help="Estado da tarefa")

# Subcomando para remover uma tarefa
remove_parser = subparsers.add_parser("remove")
remove_parser.add_argument("--index", type=int, required=True, help="Índice da tarefa a ser removida")

# Subcomando para listar tarefas
list_parser = subparsers.add_parser("list")
list_parser.add_argument("--all", action="store_true", help="Listar todas as tarefas")
list_parser.add_argument("--name", help="Filtrar tarefas pelo nome")
list_parser.add_argument("--status", choices=ALLOWED_STATES, nargs='+', help="Listar tarefas com o(s) estado(s) específico(s)")

# Configuração dos argumentos da linha de comando para o novo subcomando "update"
update_parser = subparsers.add_parser("update")
update_parser.add_argument("--index", type=int, required=True, help="Índice da tarefa a ser atualizada")
update_parser.add_argument("--state", choices=ALLOWED_STATES, required=True, help="Novo estado da tarefa")


# Analisa os argumentos da linha de comando
args = parser.parse_args()

if args.command == "create":
    create_task(args.name, args.description, args.state)
elif args.command == "list":
    list_tasks(args.all, args.name)
elif args.command == "remove":
    remove_task(args.index)
elif args.command == "update":
    update_task(args.index, args.state)
else:
    print("Comando não reconhecido. Use 'create' para criar uma nova tarefa.")
