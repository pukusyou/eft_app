import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import deal_json

DEALERS = [
    "Prapor",
    "Therapist",
    "Skier",
    "Peacekeeper",
    "Mechanic",
    "Ragman",
    "Jaeger",
]


def task_getter(dealer):
    task_list = []
    ua = UserAgent()
    header = {"user-agent": ua.chrome}
    url = "https://wikiwiki.jp/eft/" + dealer
    response = requests.get(url, headers=header, timeout=2)
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.select("#content > ul:nth-child(3) > li > a")
    return elems


def json_task_getter(dealer):
    dealer = dealer.lower()
    j = deal_json.load_json("task.json")
    return j.get_dealer_task_name_plain(dealer)


def sa_getter(dealer):
    wiki_task_list = []
    for elem in task_getter(dealer):
        wiki_task_list = wiki_task_list + elem.contents
    json_task_list = json_task_getter(dealer)
    result = list(set(wiki_task_list) - set(json_task_list))
    return result


print(sa_getter(DEALERS[0]))
