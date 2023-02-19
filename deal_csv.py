import csv


def get_ammo_list():
    with open("json/ammo.csv", "r", encoding="utf-8") as f:
        ammo_list = []
        reader = csv.reader(f)
        for line in reader:
            ammo_list.append(line)
    return ammo_list
