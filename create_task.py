import json
import os

ALLOWED_STATES = ["Em andamento", "Parado", "Novo", "Em planejamento"]

def create_task(name, description, state="Novo"):
    # Verifica se o estado é válido
    if state not in ALLOWED_STATES:
        print(f"O estado '{state}' não é permitido. Estados permitidos: {', '.join(ALLOWED_STATES)}")
        return

    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
    else:
        tasks = []

    for task in tasks:
        if task['name'] == name:
            print(f"Já existe uma tarefa com o nome '{name}'. Escolha um nome diferente.")
            return

    new_task_index = len(tasks) + 1
    new_task = {"index": new_task_index, "name": name, "description": description, "state": state}
    tasks.append(new_task)

    # Salva as tarefas de volta no arquivo JSON
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

    print(f"Nova tarefa criada {new_task_index} - Nome: {name}, Descrição: {description}, Estado: {state}")