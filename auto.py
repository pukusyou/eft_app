import configparser
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib.request
import deal_json, json
from PIL import Image
import os

DEALERS = [
    "Prapor",
    "Therapist",
    "Skier",
    "Peacekeeper",
    "Mechanic",
    "Ragman",
    "Jaeger",
]


def wiki_task_getter(dealer):
    ua = UserAgent()
    header = {"user-agent": ua.chrome}
    url = "https://wikiwiki.jp/eft/" + dealer
    response = requests.get(url, headers=header, timeout=2)
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.select("#content > ul:nth-child(3) > li > a")
    return elems


def json_task_getter(dealer):
    j = deal_json.load_json("task.json")
    return j.get_dealer_task_name_plain(dealer)


def sa_getter(dealer):
    wiki_sa_list = []
    result_list = []
    for wiki in wiki_task_getter(dealer):
        result = False
        for json in json_task_getter(dealer):
            if(wiki.contents[0]==json):
                result = True
        if(not result):
            wiki_sa_list.append(wiki)
    for tag in wiki_sa_list:
        molding = []
        molding.append(tag.contents[0])
        molding.append("https://wikiwiki.jp"+tag.get('href'))
        result_list.append(molding)
    return result_list

def send_discord(content, items):
    inifile = configparser.SafeConfigParser()
    inifile.read("setting.ini")
    webhook_url = inifile.get("MAIN", "Auto")
    items_detail = ""
    for item in items:
        items_detail = items_detail + "\nfullname: "+ item[0] + "\nnum: "+ item[2] + "\nimg: " + item[1] + "\n++++++++++++++"
    content_shaping = (
        "-----------------------------\n"+"タスク名:" + content[0] + "\nURL:" + content[1] + "\n=============" + items_detail
    )
    main_content = {"content": content_shaping}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        webhook_url, json.dumps(main_content), headers=headers
    )

def send_discord_only(content):
    inifile = configparser.SafeConfigParser()
    inifile.read("setting.ini")
    webhook_url = inifile.get("MAIN", "Auto")
    content_shaping = (
        "-----------------------------\n"+"タスク名:" + content[0] + "\nURL:" + content[1]
    )
    main_content = {"content": content_shaping}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        webhook_url, json.dumps(main_content), headers=headers
    )

def need_item(url):
    time.sleep(3)
    ua = UserAgent()
    header = {"user-agent": ua.chrome}
    response = requests.get(url, headers=header, timeout=2)
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.find_all("li")
    result = False
    for elem in elems:
        if("必要なアイテム" in elem.get_text()):
            result = True
            item_elem = elem
    if(not result):
        return []
    items=item_elem.find_all("tbody")
    items_details = []
    for item in items:
        item_name = item.select("tr > td")[0].get_text()
        item_img_url = item.find("img").get("src")
        item_quantity = item.select("tr > td")[1].get_text()
        items_details.append([item_name,item_img_url,item_quantity])
    return items_details

def check():
    for dealer in DEALERS:
        task_list = sa_getter(dealer)
        for info in task_list:
            need_items = need_item(info[1])
            if(len(need_items)==0):
                send_discord_only(info)
            else:
                for i in range(len(need_items)):
                    need_items[i][1] = download_img(dealer, need_items[i][0].replace(" ", "_"),need_items[i][1])
                time.sleep(1)
                send_discord(info,need_items)
        print("sleep:30s")
        time.sleep(5)

def download_img(dealer, name_, url):
    ua = UserAgent()
    save_path = "static/img/" + dealer + "/" + name_ + ".png"
    webp_save_path = "static/img/" + dealer + "/" + name_ + ".webp"
    opener = urllib.request.build_opener()
    opener.addheaders = [
        (
                    "User-Agent",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                )
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, save_path)
    imgfile = Image.open(save_path).convert('RGB')
    imgfile.save(webp_save_path,'webp')
    print(name_ + " >>> " + webp_save_path)
    os.remove(save_path)
    time.sleep(2)
    return save_path

check()
