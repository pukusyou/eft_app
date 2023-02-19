import bs4
import csv


class bs:
    def __init__(self):
        soup = bs4.BeautifulSoup(
            open("ammo.html", "r", encoding="utf-8"), "html.parser"
        )
        self.elems = soup.select("tbody")

    # num:22まで
    def getList(self, num):
        all = []
        for amo in self.elems[num * 3]:
            info_one = []
            count = 0
            for syosai in amo:
                if count == 0:
                    info_one.append(syosai.find("img").get("src"))
                else:
                    info_one.append(syosai.get_text())
                count = count + 1
            all.append(info_one)
        return all

    def write_csv(self, list):
        with open("ammo.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list)


const = bs()
for i in range(1, 22):
    const.write_csv(const.getList(i))
