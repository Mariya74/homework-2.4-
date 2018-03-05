import os
import chardet

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def all_file_list():
    migrations_dir = os.path.join(current_dir, migrations)
    file_list = os.listdir(path=migrations_dir)
    return file_list


def sql_list(all_file_list):
    sql_file_list = list()
    for i in all_file_list:
        if i.endswith('.sql'):
            sql_file_list.append(i)
    return sql_file_list


def decode(file_name):
    with open(os.path.join(current_dir, migrations, file_name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data.lower()
    return data


def search(sql_list):
    file_list = sql_list
    while True:
        search_string = input('Введите строку : ')
        search_string = search_string.lower()
        containing_files = list()
        for file_name in file_list:
            if search_string in decode(file_name):
                containing_files.append(file_name)
                print(file_name)
        print('Всего: {}'.format(len(containing_files)))
        file_list = containing_files


if __name__ == '__main__':
    search(sql_list(all_file_list()))