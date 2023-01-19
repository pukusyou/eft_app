import bs4
import json

class script:

    def __init__(self, path): 
        self.soup = bs4.BeautifulSoup(open(path,encoding='utf-8'), 'html.parser')

    def get_Task_name(self):
        list = []
        list = self.soup.find('ul',class_="list1").select('li>a')
        task_list = []
        for task in list:
            task_list.append(task.string)
        return task_list

    def get_task_url(self):
        list = []
        list = self.soup.find('ul',class_="list1").select('li>a')
        task_list = []
        for task in list:
            task_list.append(task.get('href'))
        return task_list

    def write_JSON(self):
        js = "{"
        for num in range(len(self.get_Task_name())):    
            js = js + '"' + self.get_Task_name()[num] + '":{"wiki_url":"' + self.get_task_url()[num] + '"},\n'
        js = js + '}'
        print(js)
        f = open('test.json', 'w', encoding='UTF-8')
        f.writelines(js)

scr = script('wiki_html\Skier - Escape from Tarkov Wiki_.html')
scr.write_JSON()