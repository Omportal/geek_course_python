import os

main_folder = "my_project"
templates = ["settings", "mainapp", "adminapp", "authapp", "scripts", "plugins"]
if not os.path.exists(main_folder):
    os.mkdir(main_folder)
for i in templates:
    new_fold = os.path.join(main_folder, i)
    if not os.path.exists(new_fold):
        os.makedirs(new_fold)
