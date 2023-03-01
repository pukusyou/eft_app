import bs4
import deal_json
import urllib.request
import time
import shutil
import csv


class script:
    def __init__(self, path):
        self.soup = bs4.BeautifulSoup(
            open(path, encoding="utf-8"), "html.parser"
        )

    def get_Task_name(self):
        list = []
        list = self.soup.find("ul", class_="list1").select("li>a")
        task_list = []
        for task in list:
            task_list.append(task.string)
        return task_list

    def get_task_url(self):
        list = []
        list = self.soup.find("ul", class_="list1").select("li>a")
        task_list = []
        for task in list:
            task_list.append(task.get("href"))
        return task_list

    def write_JSON(self):
        js = "{"
        for num in range(len(self.get_Task_name())):
            js = (
                js
                + '"'
                + self.get_Task_name()[num]
                + '":{"wiki_url":"'
                + self.get_task_url()[num]
                + '",\n'
            )
            js = (
                js
                + '"items":{"item1":{"full_name":"","name":"","num":0,"inRaid":true,"img":""}}},\n'
            )
        js = js + "}"

        print(js)
        f = open("test.json", "w", encoding="UTF-8")
        f.writelines(js)


def replace_str(prain, rep):
    file_name = "json/task.json"

    with open(file_name, encoding="utf-8") as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace(prain, rep)

    # 同じファイル名で保存
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(data_lines)


def download_img(dealer):
    js = deal_json.load_json()
    img = js.get_task_item_img(dealer, js.get_dealer_task_name_plain(dealer))
    name = js.get_task_item_fullname(
        dealer, js.get_dealer_task_name_plain(dealer)
    )
    name_ = []
    for p in name:
        name_.append(p.replace(" ", "_"))
    for n in range(len(img)):
        if img[n].find("http") != -1:
            save_path = "static/img/" + dealer + "/" + name_[n] + ".png"
            opener = urllib.request.build_opener()
            opener.addheaders = [
                (
                    "User-Agent",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
                )
            ]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(img[n], save_path)
            replace_str(img[n], "../../" + save_path)
            print(img[n] + " >>> " + save_path)
            time.sleep(2)


def add_str(path, yoso, yoso2, sinyoso):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            if yoso in line and (yoso2 not in line and "Key" not in line):
                file.write(line + ",")
                file.write(sinyoso + "\n")
            else:
                file.write(line)


def move_file():
    csvPath = "ammo.csv"
    rows = []
    with open(csvPath) as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    del rows[0]
    for url in rows:
        shutil.copy(url[0], r"ammo_img")


# move_file()
