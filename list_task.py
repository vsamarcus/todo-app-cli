import json

def list_tasks(allowed_states=None, task_name=None):
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")
        return

    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    if allowed_states:
        # Filtra tarefas com base nos estados permitidos
        filtered_tasks = [task for task in tasks if task['state'] in allowed_states]
    else:
        filtered_tasks = tasks

    if task_name:
        # Filtra por nome da tarefa
        filtered_tasks = [task for task in filtered_tasks if task['name'] == task_name]

    if not filtered_tasks:
        print("Nenhuma tarefa encontrada com os critérios fornecidos.")
        return

    # Lista as tarefas filtradas
    for task in filtered_tasks:
        print(f"Índice: {task['index']}, Nome: {task['name']}, Descrição: {task['description']}, Estado: {task['state']}")
