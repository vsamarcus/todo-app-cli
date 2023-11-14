import json

ALLOWED_STATES = ["Concluído", "Cancelado", "Em andamento", "Parado", "Novo", "Em planejamento"]

def update_task(task_index, new_state):
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
        # Verifica se o novo estado é válido
        if new_state not in ALLOWED_STATES:
            print(f"O estado '{new_state}' não é permitido. Estados permitidos: {', '.join(ALLOWED_STATES)}")
            return

        found_task['state'] = new_state
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        print(f"Estado da tarefa atualizado - Índice: {found_task['index']}, Nome: {found_task['name']}, Novo Estado: {new_state}")
    else:
        print(f"Nenhuma tarefa com o índice '{task_index}' encontrada.")
