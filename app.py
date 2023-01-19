from flask import Flask, render_template, request, redirect, url_for
import deal_json as dj

app = Flask(__name__)
json = dj.load_json()
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('mainpage.html')
def post():
	task = request.form.getlist('task')

@app.route('/task/', methods=['GET','POST'])
def task_setting():
    if request.method == 'GET':
        return render_template('task_setting.html', tasks=json.get_dealer_task_name('prapor'))

@app.route('/task/item/', methods=['GET','POST'])
def task_item():
    if request.method == 'GET':
        return render_template('task_setting.html')
    else:
        tasks_no_symbol = []
        tasks = request.form.getlist('task')
        for task in tasks:
            tasks_no_symbol.append(task.replace('_',' '))
        remain_tasks = json.get_remaining_tasks('prapor',tasks_no_symbol)
        tasks_item = json.get_task_item_sum('prapor',remain_tasks)
        return render_template('task_item.html', tasks_item=tasks_item)

if __name__ == "__main__":
    app.run(debug=True)