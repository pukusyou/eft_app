import json


class load_json:
    def __init__(self, filename):
        json_open = open("json/" + filename, "r", encoding="utf-8")
        self.dealer_list = [
            "prapor",
            "Therapist",
            "Skier",
            "Peacekeeper",
            "Mechanic",
            "Ragman",
            "Jaeger",
        ]
        self.hideout_list = [
            "Bitcoin Farm",
            "Booze Generator",
            "Intelligence Center",
            "Lavatory",
            "Medstation",
            "Nutrition Unit",
            "Scav case",
            "Water collector",
            "Workbench",
            "Air Filtering Unit",
            "Generator",
            "Heating",
            "Illumination",
            "Library",
            "Rest Space",
            "Security",
            "Shooting range",
            "Solar power",
            "Stash",
            "Vents",
            "Defective wall",
            "Gym",
        ]
        self.jsn = json.load(json_open)

    # dealerの持っているすべてのタスク名を返す。(空白を'_'に置き換えたものも返す)
    def get_dealer_task_name(self, dealer):
        task_list = []
        task_list_ = []
        for key in self.jsn[dealer]:
            task_list.append(key)
        for task in task_list:
            task_list_.append(task.replace(" ", "_"))
        return list(zip(task_list, task_list_))

    # dealerの持っているすべてのタスク名を返す。
    def get_dealer_task_name_plain(self, dealer):
        task_list = []
        for key in self.jsn[dealer]:
            task_list.append(key)
        return task_list

    # すべてのタスク名を返す。
    def get_all_task_name_plain(self, list):
        task_list = []
        for dealer in list:
            task_list = task_list + self.get_dealer_task_name_plain(dealer)
        return task_list

    # 引数のタスクを持っているdealerを返す
    def get_task_dealer(self, tasks, list):
        dealer_list = []
        for task in tasks:
            for dealer in list:
                for dealer_task in self.get_dealer_task_name_plain(dealer):
                    if task == dealer_task:
                        dealer_list.append(dealer)
        return dealer_list

    # 全ての中から残っているタスクを返す
    def get_sa_tasks(self, tasks):
        tasks_name_list = [
            i
            for i in self.get_all_task_name_plain(self.dealer_list)
            if i not in tasks
        ]
        return [
            list(e)
            for e in zip(
                tasks_name_list,
                self.get_task_dealer(tasks_name_list, self.dealer_list),
            )
        ]

    def get_sa_hideout(self, tasks):
        tasks_name_list = [
            i
            for i in self.get_all_task_name_plain(self.hideout_list)
            if i not in tasks
        ]
        return [
            list(e)
            for e in zip(
                tasks_name_list,
                self.get_task_dealer(tasks_name_list, self.hideout_list),
            )
        ]

    # 引数のタスクのwikiURLを返す。
    def get_task_url(self, dealer, task_name):
        return self.jsn[dealer][task_name]["wiki_url"]

    # 引数のタスクのフルネームを返す。
    def get_task_item_fullname(self, dealer, task_name):
        fullnameList = []
        list = []
        if "items" in self.jsn[dealer][task_name]:
            for item in self.jsn[dealer][task_name]["items"]:
                list.append(item)
            for i in list:
                fullnameList.append(
                    self.jsn[dealer][task_name]["items"][i]["full_name"]
                )
        return fullnameList

    def get_task_item_name(self, dealer, task_name):
        fullnameList = []
        list = []
        if "items" in self.jsn[dealer][task_name]:
            for item in self.jsn[dealer][task_name]["items"]:
                list.append(item)
            for i in list:
                fullnameList.append(
                    self.jsn[dealer][task_name]["items"][i]["name"]
                )
        return fullnameList

    def get_task_item_num(self, dealer, task_name):
        fullnameList = []
        list = []
        if "items" in self.jsn[dealer][task_name]:
            for item in self.jsn[dealer][task_name]["items"]:
                list.append(item)
            for i in list:
                fullnameList.append(
                    self.jsn[dealer][task_name]["items"][i]["num"]
                )
        return fullnameList

    def get_task_item_inRaid(self, dealer, task_name):
        fullnameList = []
        list = []
        if "items" in self.jsn[dealer][task_name]:
            for item in self.jsn[dealer][task_name]["items"]:
                list.append(item)
            for i in list:
                fullnameList.append(
                    self.jsn[dealer][task_name]["items"][i]["inRaid"]
                )
        return fullnameList

    def get_task_item_img(self, dealer, task_name):
        fullnameList = []
        list = []
        if "items" in self.jsn[dealer][task_name]:
            for item in self.jsn[dealer][task_name]["items"]:
                list.append(item)
            for i in list:
                fullnameList.append(
                    self.jsn[dealer][task_name]["items"][i]["img"]
                )
        return fullnameList

    def get_task_item_category(self, dealer, task_name):
        fullnameList = []
        list = []
        if "items" in self.jsn[dealer][task_name]:
            for item in self.jsn[dealer][task_name]["items"]:
                list.append(item)
            for i in list:
                fullnameList.append(
                    self.jsn[dealer][task_name]["items"][i]["category"]
                )
        return fullnameList

    def get_task_wikiURL(self, dealer, task_name):
        result = []
        for num in range(len(self.get_task_item_fullname(dealer, task_name))):
            result.append(self.jsn[dealer][task_name]["wiki_url"])
        return result

    def get_task_name(self, dealer, task_name):
        result = []
        for num in range(len(self.get_task_item_fullname(dealer, task_name))):
            result.append(task_name)
        return result

    def get_task_item_all(self, dealer, task_name):
        result = [
            list(e)
            for e in zip(
                self.get_task_item_fullname(dealer, task_name),
                self.get_task_item_name(dealer, task_name),
                self.get_task_item_num(dealer, task_name),
                self.get_task_item_inRaid(dealer, task_name),
                self.get_task_item_img(dealer, task_name),
                self.get_task_item_category(dealer, task_name),
                self.get_task_wikiURL(dealer, task_name),
                self.get_task_name(dealer, task_name),
            )
        ]
        print(result)
        if len(result) > 0:
            for a in range(len(result)):
                result[a][6] = [result[a][6]]
                result[a][7] = [result[a][7]]
        return result

    def get_hideout_task_item_all(self, dealer, task_name):
        result = [
            list(e)
            for e in zip(
                self.get_task_item_fullname(dealer, task_name),
                self.get_task_item_name(dealer, task_name),
                self.get_task_item_num(dealer, task_name),
                self.get_task_item_img(dealer, task_name),
            )
        ]
        return result

    def get_task_item_sum(self, tasks_name):
        lists = []
        for task_name in tasks_name:
            for item in self.get_task_item_all(task_name[1], task_name[0]):
                lists.append(item)
        length = len(lists)
        for num in range(length):
            next = num + 1
            while next < length:
                if (
                    lists[num][0] == lists[next][0]
                    and lists[num][2] > 0
                    and lists[next][2] > 0
                ):
                    pop = lists.pop(next)
                    lists[num][7] = lists[num][7] + pop[7]
                    lists[num][6] = lists[num][6] + pop[6]
                    lists[num][2] = lists[num][2] + pop[2]
                    length = length - 1
                next = next + 1
        return lists

    def get_hideout_task_item_sum(self, tasks_name):
        lists = []
        for task_name in tasks_name:
            for item in self.get_hideout_task_item_all(
                task_name[1], task_name[0]
            ):
                lists.append(item)
        length = len(lists)
        for num in range(length):
            next = num + 1
            while next < length:
                if (
                    lists[num][0] == lists[next][0]
                    and lists[num][2] > 0
                    and lists[next][2] > 0
                ):
                    lists[num][2] = lists[num][2] + lists.pop(next)[2]
                    length = length - 1
                next = next + 1
        return lists


# print(dj.get_task_item_all('prapor','Debut'))
# 最初のkeyを取る
# for key in jsn:
#     print(key)

# keyの値を取る
# print(jsn["The Punisher - Part 6"])

# itemの一覧表示
# for key in jsn["The Punisher - Part 6"]:
#     for item in key["item"]:
#         print(item)
