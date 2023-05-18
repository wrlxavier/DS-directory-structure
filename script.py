import os


def create_dir(path, folder_name):
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path, exist_ok=True)


print('\n\nThis is a project environment configuration script.')
print('\nRepository "DS-directory-structure" https://github.com/wrlxavier/DS-directory-structure \n')

project_name = input('Project name: ')

if project_name != '':

    dir_config = {
        'data': ['row', 'interim', 'processed', 'external'],
        'models': [],
        'notebooks': [],
        'src': ['data', 'features', 'models', 'visualization'],
        'reports': ['figures']
    }

    
    root_path = os.getcwd()
    create_dir(root_path, project_name)
    project_path = os.path.join(root_path, project_name)

    count = 0
    for dir_name in dir_config.keys():
        count += 1
        print(f"[{count}] creating ./{project_name}/{dir_name}")
        create_dir(project_name, dir_name)
        dir_path = os.path.join(project_path, dir_name)
        for sub_dir_name in dir_config[dir_name]:
            count += 1
            print(f"[{count}] creating ./{project_name}/{dir_name}/{sub_dir_name}")
            create_dir(dir_path, sub_dir_name)