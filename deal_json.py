import json

class load_json:

    def __init__(self):        
        json_open = open('json/task.json', 'r')
        self.dealer_list = ['prapor']
        self.jsn = json.load(json_open)

    # dealerの持っているすべてのタスク名を返す。(空白を'_'に置き換えたものも返す)
    def get_dealer_task_name(self, dealer):
        task_list = []
        task_list_ = []
        for key in self.jsn[dealer]:
            task_list.append(key)
        for task in task_list:
            task_list_.append(task.replace(' ', '_'))
        return list(zip(task_list,task_list_))

    # dealerの持っているすべてのタスク名を返す。
    def get_dealer_task_name_plain(self, dealer):
        task_list = []
        for key in self.jsn[dealer]:
            task_list.append(key)
        return task_list

    # 残っているタスクを返す
    def get_remaining_tasks(self, dealer, tasks):
        tasks_name_list = [i for i in self.get_dealer_task_name_plain(dealer) if i not in tasks]
        return tasks_name_list

    # 引数のタスクのwikiURLを返す。
    def get_task_url(self, dealer, task_name):
        return self.jsn[dealer][task_name]["wiki_url"]

    # 引数のタスクのフルネームを返す。
    def get_task_item_fullname(self, dealer, tasks_name):
        fullnameList = []
        for task_name in tasks_name:
            list = []
            if('items' in self.jsn[dealer][task_name]):
                for item in self.jsn[dealer][task_name]["items"]:
                    list.append(item)
                for i in list:
                    fullnameList.append(self.jsn[dealer][task_name]["items"][i]["full_name"])
        return fullnameList

    def get_task_item_name(self, dealer, tasks_name):
        fullnameList = []
        for task_name in tasks_name:
            list = []
            if('items' in self.jsn[dealer][task_name]):
                for item in self.jsn[dealer][task_name]["items"]:
                    list.append(item)
                for i in list:
                    fullnameList.append(self.jsn[dealer][task_name]["items"][i]["name"])
        return fullnameList

    def get_task_item_num(self, dealer, tasks_name):
        fullnameList = []
        for task_name in tasks_name:
            list = []
            if('items' in self.jsn[dealer][task_name]):
                for item in self.jsn[dealer][task_name]["items"]:
                    list.append(item)
                for i in list:
                    fullnameList.append(self.jsn[dealer][task_name]["items"][i]["num"])
        return fullnameList

    def get_task_item_inRaid(self, dealer, tasks_name):
        fullnameList = []
        for task_name in tasks_name:
            list = []
            if('items' in self.jsn[dealer][task_name]):
                for item in self.jsn[dealer][task_name]["items"]:
                    list.append(item)
                for i in list:
                    fullnameList.append(self.jsn[dealer][task_name]["items"][i]["inRaid"])
        return fullnameList

    def get_task_item_img(self, dealer, tasks_name):
        fullnameList = []
        for task_name in tasks_name:
            list = []
            if('items' in self.jsn[dealer][task_name]):
                for item in self.jsn[dealer][task_name]["items"]:
                    list.append(item)
                for i in list:
                    fullnameList.append(self.jsn[dealer][task_name]["items"][i]["img"])
        return fullnameList

    def get_task_item_all(self, dealer, tasks_name):
        return [list(e) for e in zip(self.get_task_item_fullname(dealer,tasks_name), self.get_task_item_name(dealer,tasks_name),
        self.get_task_item_num(dealer,tasks_name), self.get_task_item_inRaid(dealer,tasks_name), self.get_task_item_img(dealer,tasks_name))]

    def get_task_item_sum(self,dealer, tasks_name):
        lists = []
        lists = self.get_task_item_all(dealer, tasks_name)
        print(lists[11])
        print(lists[16])
        length = len(lists)
        for num in range(length):
            next = num + 1
            while(next<length):
                if(lists[num][0]==lists[next][0]):
                    print("Ok")
                    lists[num][2] = lists[num][2] + lists.pop(next)[2]
                    length = length - 1
                next = next + 1
        return lists

    # 最初のkeyを取る
    # for key in jsn:
    #     print(key)

    # keyの値を取る
    # print(jsn["The Punisher - Part 6"])

    # itemの一覧表示
    # for key in jsn["The Punisher - Part 6"]:
    #     for item in key["item"]:
    #         print(item)