import shutil
import os

users_path = os.path.expanduser('c:/users')
folders = os.listdir(users_path)
remove = ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public', 'Todos os Usuários', 'Usuário Padrão']

for item in remove:
    if item in folders:
        folders.remove(item)

for folder_name in folders:
    source_folder = "d://system_x"
    destination_folder = f"c://users/{folder_name}/system_x"
    print(destination_folder)

    def delete_folder(folder):
        try:
            shutil.rmtree(folder)
            print(f'A pasta {folder} foi apagada com sucesso.')
        except Exception as e:
            print(f'Erro ao apagar a pasta {folder}: {e}')
        
    delete_folder(destination_folder)

    def copy_folder(source, destination):
        shutil.copytree(source, destination)

    copy_folder(source_folder, destination_folder)