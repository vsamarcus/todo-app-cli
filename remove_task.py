import json

def remove_task(task_index):
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")
        return

    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    # Encontra a tarefa pelo campo 'index'
    found_task = None
    for task in tasks:
        if task['index'] == task_index:
            found_task = task
            break

    if found_task:
        tasks.remove(found_task)
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2, ensure_ascii=False)
        print(f"Tarefa removida - Índice: {found_task['index']}, Nome: {found_task['name']}, Descrição: {found_task['description']}")
    else:
        print(f"Nenhuma tarefa com o índice '{task_index}' encontrada.")