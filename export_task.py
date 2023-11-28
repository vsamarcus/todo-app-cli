import json

def export_task(filename):
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada para exportação.")
        return

    if not tasks:
        print("Nenhuma tarefa encontrada para exportação.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as export_file:
            json.dump(tasks, export_file, ensure_ascii=False, indent=2)
        print(f"Tarefas exportadas com sucesso para o arquivo {filename}.")
    except Exception as e:
        print(f"Erro ao exportar tarefas: {e}")