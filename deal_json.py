import json

class load_json:

    def __init__(self):        
        json_open = open('json/task.json', 'r')
        self.jsn = json.load(json_open)

    def get_dealer_task_name(self, dealer):
        for key in self.jsn[dealer]:
            print(key)
    # 最初のkeyを取る
    # for key in jsn:
    #     print(key)

    # keyの値を取る
    # print(jsn["The Punisher - Part 6"])

    # itemの一覧表示
    # for key in jsn["The Punisher - Part 6"]:
    #     for item in key["item"]:
    #         print(item)

j = load_json()
j.get_dealer_task_name("prapor")