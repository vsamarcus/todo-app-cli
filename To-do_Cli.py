import os
import shutil
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Colors:
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    RED = Fore.RED
    END = Style.RESET_ALL

    @staticmethod
    def blue(text):
        return f"{Colors.BLUE}{text}{Colors.END}"

    @staticmethod
    def green(text):
        return f"{Colors.GREEN}{text}{Colors.END}"

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar tela
    print(Colors.RED + "#" * 83 + Colors.END)
    print("\n")
    print(Colors.BLUE + "      ##############                            #########                      " + Colors.END)
    print(Colors.BLUE + "           ##          ###########             ##       ##      ###########   " + Colors.END)
    print(Colors.BLUE + "          ##         ##         ##            ##        ##    ##         ##  " + Colors.END)
    print(Colors.BLUE + "         ##         ##         ##   ######   ##        ##    ##         ##  " + Colors.END)
    print(Colors.BLUE + "        ##         ##         ##            ##        ##    ##         ##  " + Colors.END)
    print(Colors.BLUE + "       ##          ###########             ###########      ###########  " + Colors.END)
    print("\n")
    print(Colors.RED + "#" * 83 + Colors.END)

def get_valid_task_number(tasks):
    while True:
        try:
            task_num = int(input("Digite o número da tarefa: "))
            if 1 <= task_num <= len(tasks):
                return task_num
            else:
                print("Número de tarefa inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def export_tasks_to_file(directory, filename, tasks):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(os.path.join(directory, filename), 'w') as file:
            for task in tasks:
                status = Colors.green("[X]") if task["status"] == "[X]" else Colors.blue("[ ]")
                file.write(f"{status}  {task['title']}\n")

        print(f"Tarefas exportadas para o arquivo {filename} no diretório {directory}.")
    except Exception as e:
        print(f"Erro ao exportar tarefas: {e}")

def import_tasks_from_file(directory, filename):
    try:
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()
            tasks = []
            for line in lines:
                parts = line.strip().split('  ', 1)
                if len(parts) == 2:
                    status, title = parts[0], parts[1]
                    task = {"title": title, "status": status}
                    tasks.append(task)
        print(f"Tarefas importadas do arquivo {filename} no diretório {directory}.")
        return tasks
    except FileNotFoundError:
        print("Arquivo de importação não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao importar tarefas: {e}")
        return []

def list_tasks(tasks, list_name):
    if not tasks:
        print(f"Lista de Tarefas '{list_name}' Vazia.")
    else:
        print(f'TAREFA: "{list_name}"')
        print("")
        print("   Sub-Tarefas:")
        for i, task in enumerate(tasks, 1):
            status = "[X]" if task['status'] == "[X]" else "[ ]"
            print(f"{i:4}. {status} {task['title']}")

def toggle_task_status(tasks, task_num):
    if 1 <= task_num <= len(tasks):
        task = tasks[task_num - 1]
        if task['status'] == "[X]":
            task['status'] = "[ ]"
            print(f'Tarefa "{task["title"]}" desmarcada como concluída.')
        else:
            task['status'] = "[X]"
            print(f'Tarefa "{task["title"]}" marcada como concluída.')
    else:
        print("Número de tarefa inválido. Nenhuma tarefa foi marcada como concluída.")

def remove_task(tasks, task_num):
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f'Tarefa "{removed_task["title"]}" removida com sucesso.')
    else:
        print("Número de tarefa inválido. Nenhuma tarefa foi removida.")

def load_tasks_from_file(directory, filename):
    tasks = []
    try:
        with open(os.path.join(directory, filename), 'r') as file:
            for line in file:
                parts = line.strip().split('  ', 1)
                if len(parts) == 2:
                    status, title = parts[0], parts[1]
                    task = {"title": title, "status": status}
                    tasks.append(task)
    except FileNotFoundError:
        pass  # Arquivo inexistente, não há tarefas a carregar
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")
    return tasks

def save_tasks_to_file(directory, filename, tasks):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(os.path.join(directory, filename), 'w') as file:
            for task in tasks:
                status = "[X]" if task["status"] == "[X]" else "[ ]"
                file.write(f"{status}  {task['title']}\n")
        print(f"Tarefas salvas em {filename} no diretório {directory}.")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")
        time.sleep(2)

def list_all_tasks_in_directory(directory):
    tasks = []
    try:
        files = os.listdir(directory)
        task_files = [file for file in files if file.endswith('.txt')]

        if not task_files:
            print(Colors.GREEN + "Nenhum arquivo de tarefas encontrado no diretório." + Colors.END)
            time.sleep(3)
            return
        print(Colors.RED + "-" * 28 + Colors.END)
        print(Colors.BLUE + "   Diretórios disponíveis:" + Colors.END)
        print(Colors.RED + "-" * 28 + Colors.END)
        for i, task_file in enumerate(task_files, 1):
            print(f"{i:4}. {task_file}")
        print(Colors.RED + "-" * 28 + Colors.END)
        print(Colors.BLUE + "|       ** MENU **         |" + Colors.END)
        print(Colors.BLUE + "|                          |" + Colors.END)
        print(Colors.BLUE + "|   E. Exportar Tarefas    |" + Colors.END)
        print(Colors.BLUE + "|   0. VOLTAR              |" + Colors.END)
        print(Colors.BLUE + "|                          |" + Colors.END)
        print(Colors.RED + "-" * 28 + Colors.END)
        choice = input(Colors.BLUE + "   Escolha o Diretório:" + Colors.END)
        print("-" * 53)
        if choice == "0":
            return  # Volta ao menu principal
        if choice.upper() == "E":
            filename = input("Digite o nome do arquivo para exportar as tarefas (inclua a extensão .txt): ")
            export_tasks_to_file(directory, filename, tasks)
            return

        try:
            selected_file = task_files[int(choice) - 1]
            tasks = load_tasks_from_file(directory, selected_file)

            while True:
                print_banner()

                print("")
                list_tasks(tasks, selected_file.split(".")[0])
                print("\nOpções:")
                print(Colors.GREEN + "-" * 34 + Colors.END)
                print(Colors.GREEN + "|   1. Adicionar Tarefa          |" + Colors.END)
                print(Colors.GREEN + "|   2. Marcar/Desmarcar Tarefa   |" + Colors.END)
                print(Colors.GREEN + "|   3. Remover Tarefa            |" + Colors.END)
                print(Colors.GREEN + "|   0. Voltar                    |" + Colors.END)
                print(Colors.GREEN + "|   99. Excluir arquivo          |" + Colors.END)
                print(Colors.GREEN + "-" * 34 + Colors.END)

                sub_choice = input("\nEscolha uma opção: ")

                if sub_choice == "0":
                    break  # Volta ao menu anterior

                elif sub_choice == "1":
                    new_task_name = input("Digite o título da nova tarefa: ")
                    if not any(task['title'] == new_task_name for task in tasks):
                        tasks.append({'status': '[ ]', 'title': new_task_name})
                        save_tasks_to_file(directory, selected_file, tasks)
                        print(f'Tarefa "{new_task_name}" adicionada com sucesso em {selected_file}.')
                        time.sleep(2)
                    else:
                        print(f'A tarefa "{new_task_name}" já existe. Escolha um nome diferente. Aguarde...')
                        time.sleep(3)

                elif sub_choice == "2":
                    list_tasks(tasks, selected_file.split(".")[0])  
                    task_num = get_valid_task_number(tasks)
                    toggle_task_status(tasks, task_num)
                    save_tasks_to_file(directory, selected_file, tasks)

                elif sub_choice == "3":
                    list_tasks(tasks, selected_file.split(".")[0])  
                    task_num = get_valid_task_number(tasks)
                    remove_task(tasks, task_num)
                    save_tasks_to_file(directory, selected_file, tasks)

                elif sub_choice == "99":
                    confirm = input(f"Tem certeza de que deseja excluir o arquivo {selected_file}? (s/n): ")
                    if confirm.lower() == 's':
                        os.remove(os.path.join(directory, selected_file))
                        print(f"Arquivo {selected_file} excluído.")
                    return

                else:
                    print("Opção inválida. Tente novamente.")
                    time.sleep(2)

        except (ValueError, IndexError):
            print("Opção inválida.")
            time.sleep(2)
    except FileNotFoundError:
        print("O diretório especificado não foi encontrado.")
        time.sleep(2)

def import_menu(directory):
    try:
        files = os.listdir(directory)
        task_files = [file for file in files if file.endswith('.txt')]

        if not task_files:
            print("Nenhum arquivo de tarefas encontrado no diretório.")
            time.sleep(3)
            return

        print("Listas de tarefas disponíveis para importação:")
        for i, task_file in enumerate(task_files, 1):
            print(f"{i:4}. {task_file}")

        print("0. Voltar")

        choice = input("Escolha o número do arquivo para importar as tarefas (ou 0 para voltar): ")

        if choice == "0":
            return  # Volta ao menu anterior

        try:
            selected_file = task_files[int(choice) - 1]
            tasks_to_import = import_tasks_from_file(directory, selected_file)
            list_tasks(tasks_to_import, selected_file.split(".")[0])

        except (ValueError, IndexError):
            print("Opção inválida.")
            time.sleep(2)
    except FileNotFoundError:
        print("O diretório especificado não foi encontrado.")
        time.sleep(2)

def main():
    directory = r'C:\Users\valdo\OneDrive\Documentos\To-Do\cli'  # Caminho do diretório onde serão salva as classes

    if not os.path.exists(directory):
        os.makedirs(directory)

    while True:
        print_banner()  # Exibir banner antes de mostrar o menu

        print("\nMENU:")
        print(Colors.GREEN + "-" * 30 + Colors.END)
        print(Colors.GREEN + "  1. Adicionar Tarefa          " + Colors.END)
        print(Colors.GREEN + "  2. Listar Todas as Tarefas   " + Colors.END)
        print(Colors.GREEN + "  3. Importar Tarefas          " + Colors.END)
        print(Colors.GREEN + "  4. Sair                      " + Colors.END)
        print(Colors.GREEN + "-" * 30 + Colors.END)
        print("")
        choice = input("Escolha uma opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar tela

        if choice == "1":
            print_banner()  # Mantém o banner na parte superior
            print("\nDigite o nome do Arquivo para incluir a tarefa (inclua a extensão .txt):")
            filename = input()

            if not filename:
                print("Nome de arquivo inválido. Tente novamente.")
                time.sleep(2)
                continue  # Continue dentro do loop while

            new_task = input("Digite o título da tarefa: ")

            if not os.path.isfile(os.path.join(directory, filename)):
                with open(os.path.join(directory, filename), 'w') as file:
                    pass

            tasks = load_tasks_from_file(directory, filename)
            tasks.append({'status': '[ ]', 'title': new_task})

            save_tasks_to_file(directory, filename, tasks)
            print(f'Tarefa "{new_task}" adicionada com sucesso em {filename}.')

        elif choice == "2":
            list_all_tasks_in_directory(directory)

        elif choice == "3":
            import_menu(directory)

        elif choice == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()