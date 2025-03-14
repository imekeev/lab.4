import json
import os
file_path = os.path.join(os.path.dirname(__file__), "sample-data.json")
#os.path.dirname(__file__) — путь к текущей директории.
#os.path.join() — создаёт путь к файлу "sample-data.json".
#json.load(file) — загружает содержимое файла в переменную data.
with open(file_path) as file:
    data = json.load(file)

header = "Interface Status"
separator = "=" * 80
columns = f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}"
divider = "-" * 80

print(header)
print(separator)
print(columns)
print(divider)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    # "l1PhysIf" — это информация о физическом интерфейсе.
    # "attributes" — в нём находятся все нужные нам данные.
    dn = attributes["dn"]
    # получаем имя интерфейса 
    description = attributes["descr"] if attributes["descr"] else " " * 20
    #если есть deskr мы его берем если нет то ставим 20 пробелов чтобы не заполняять строку
    speed = attributes["speed"] #скорость
    mtu = attributes["mtu"] #размер
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
    #{dn:<50} — выводим имя интерфейса и выравниваем его по левому краю 50 символов.
    #{description:<20} — описание интерфейса 20 символов.
    #{speed:<7} — скорость интерфейса 7 символов.
    #{mtu:<6} — MTU 6 символов.
