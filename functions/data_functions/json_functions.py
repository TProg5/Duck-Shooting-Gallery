import json

def check_progress_level(path, file_name) -> bool:
    path = f"{path}/{file_name}" 

    with open(path, "r") as f:
        data = json.loads(f.read())
        
    return bool(data["progress"])


def check_admit(path, file_name) -> bool:
    path = f"{path}/{file_name}" 

    with open(path, "r") as f:
        data = json.loads(f.read())
        
    return bool(data["admit"])

def data_json(path, file_name):
    path = f"{path}/{file_name}"
    with open(path, "r") as f:
        data = json.loads(f.read())

    return data

def lvl_points(path, file_name):
    path = f"{path}/{file_name}"

    with open(path, "r") as f:
        data = json.loads(f.read())
        
    return int(data["points_for_ducks"])

def update_admit(path, file_name):
    path = f"{path}/{file_name}"

    # Читаем текущие данные
    with open(path, "r") as f:
        data = json.load(f)  # Используем json.load(), а не json.loads()

    # Обновляем значение
    data["admit"] = True

    # Записываем обратно
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Сохраняем форматирование


def update_progress(path, file_name):
    path = f"{path}/{file_name}"

    with open(path, "r") as f:
        data = json.load(f)

    data["progress"] = True

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# Пример вызова функции
update_admit("Levels", "hard.json")