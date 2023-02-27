import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def task_getter(dealer):
    ua = UserAgent()
    header = {"user-agent": ua.chrome}
    url = "https://wikiwiki.jp/eft/" + dealer
    response = requests.get(url, headers=header, timeout=2)
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.select("#content > ul:nth-child(3) > li > a")
    print(elems[0].contents)


task_getter("Prapor")
