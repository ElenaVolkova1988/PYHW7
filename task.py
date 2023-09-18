

import task.1 

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = task.group_rename_files("_fn_", ".txt", path="./data_files")
    print(f"Переименовано: {files_cnt}")