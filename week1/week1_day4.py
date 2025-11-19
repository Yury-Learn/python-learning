"""
Week1 Day4
Цель:
- списки (list) и словари (dict) для инвентаря
- цикл for для обхода хостов
- аккуратный вывод + подготовка команд проверки доступности (без выполнения)

Словарь хоста:
- name : логическое имя
- ip   : IPv4-адрес
- role : роль/назначение
- spec : краткие характеристики (CPU/RAM/HDD)
"""

import platform  # чтобы подобрать правильный флаг ping под ОС

# 1) Инвентарь: список словарей (по одному словарю на хост)
servers = [
    {
        "name": "test-pvm1",
        "ip": "10.38.26.62",
        "role": "виртуализация / KVM host",
        "spec": "CPU 8, RAM 16G, HDD 100G",
    },
    {
        "name": "test-pvm2",
        "ip": "10.38.26.63",
        "role": "обычная ВМ для тестов",
        "spec": "CPU 2, RAM 4G, HDD 50G",
    },
    {
        "name": "test-pmon",
        "ip": "10.38.26.64",
        "role": "monitoring / prometheus / grafana (logger на этой же ВМ)",
        "spec": "CPU 4, RAM 8G, HDD 50G",
    },
]

# 2) Подбор флага ping: Windows -> -n 1, Linux/macOS -> -c 1
OS = platform.system().lower()
PING_ONE_FLAG = "-n 1" if OS.startswith("win") else "-c 1"

# 3) Красивый заголовок таблицы
print("".ljust(78, "-"))
print(f"{'HOST':<12} {'IP':<15} {'ROLE':<36} {'SPEC'}")
print("".ljust(78, "-"))

# 4) Основной цикл по серверам
for s in servers:
    name = s["name"]  # имя хоста (str)
    ip   = s["ip"]    # IPv4-адрес (str)
    role = s["role"]  # роль/назначение (str)
    spec = s["spec"]  # характеристики (str)

    # Строка-таблица
    print(f"{name:<12} {ip:<15} {role:<36} {spec}")

    # Шаблон команды ping (мы её пока НЕ запускаем)
    cmd_ping = f"ping {PING_ONE_FLAG} {ip}"
    print(f"  -> проверка доступности (пример): {cmd_ping}")

print("".ljust(78, "-"))
print("Готово. Инвентарь выведен, команды сформированы (не выполнялись).")
