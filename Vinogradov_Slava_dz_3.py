import os
from shutil import copytree, copy2

my_project_path = r"C:\Users\Omportal\Desktop\geek_python\lesson_7\my_project"
for root, dirs, files in os.walk(my_project_path):
    if root.split("\\")[-1] == "templates":
        if root.split("\\")[-2] == "mainapp":
            dst = root
        if root.split("\\")[-2] == "authapp":
            src = root

copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=True)
