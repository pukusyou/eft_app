import bs4
import deal_json
import urllib.request
import time
import deal_json as js
import os


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


def replace_str(prain, rep, filename):
    file_name = "json/" + filename

    with open(file_name, encoding="utf-8") as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace(prain, rep)

    # 同じファイル名で保存
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(data_lines)


def download_img(dealer, filename):
    js = deal_json.load_json(filename)
    img = []
    name = []
    for task in js.get_dealer_task_name_plain(dealer):
        img = img + js.get_task_item_img(dealer, task)
    for taska in js.get_dealer_task_name_plain(dealer):
        name = name + js.get_task_item_fullname(dealer, taska)
    name_ = []
    # os.mkdir('static/img/'+ dealer)
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
            replace_str(img[n], "../../" + save_path, "hideout.json")
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


# hideout_list = ['Bitcoin Farm','Booze Generator','Intelligence Center','Lavatory','Medstation','Nutrition Unit','Scav case','Water collector','Workbench'
#         ,'Air Filtering Unit','Generator','Heating','Illumination','Library','Rest Space','Security','Shooting range','Solar power',
#         'Stash','Vents']
download_img("Gym", "hideout.json")
# def write_txt(list):
#     f = open('item.txt', 'w')
#     for txt in list:
#         f.write(txt + '\n')
#     f.close

# json = js.load_json()
# remain_tasks = json.get_sa_hideout([])
# name = []
# for a in remain_tasks:
#     name = name + json.get_task_item_fullname(a[1], a[0])
# write_txt(name)
