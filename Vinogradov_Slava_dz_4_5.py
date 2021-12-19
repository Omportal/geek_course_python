import os

path_geek = input("Введите полный путь до папки:")


def stat_folder(path, threshold=100):
    """"Функция подсчёта размера,расширения и кол-ва файлов,введите корневой путь и верхнюю границу размера файла """
    dict_files = {}
    tmp_name = []
    tmp_size = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if len(file.split(".")) > 1:
                if threshold / 10 < os.stat(os.path.join(root, file)).st_size <= threshold:
                    tmp_name.append(file.split(".")[-1])
                    tmp_size.append(os.stat(os.path.join(root, file)).st_size)
                    dict_files[threshold] = len(tmp_size), list(set(tmp_name))
                if os.stat(os.path.join(root, file)).st_size == 0 and threshold <= 100:
                    tmp_name.append(file.split(".")[-1])
                    tmp_size.append(os.stat(os.path.join(root, file)).st_size)
                    dict_files[threshold] = len(tmp_size), list(set(tmp_name))

    print(dict_files)


stat_folder(path_geek, threshold=100)
stat_folder(path_geek, threshold=1000)
stat_folder(path_geek, threshold=10000)
stat_folder(path_geek, threshold=100000)
