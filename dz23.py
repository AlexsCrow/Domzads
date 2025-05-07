import os
import time

file_path = "Work/w.txt"
if os.path.exists(file_path):
    directory, name = os.path.split(file_path)
    print(directory, name)
    a_time = os.path.getatime(file_path)
    t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a_time))
    print(f"{name} ({directory}) - время последнего доступа ке файлу {t}")
else:
    print(f"Файл {file_path} не существует")

