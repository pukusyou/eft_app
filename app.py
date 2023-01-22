from flask import Flask, render_template, request, redirect, url_for
import deal_json as dj

app = Flask(__name__,static_folder='./static')
json = dj.load_json()
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('mainpage.html')
def post():
	task = request.form.getlist('task')

@app.route('/task/', methods=['GET','POST'])
def task_setting():
    if request.method == 'GET':
        return render_template('task_setting.html', prapor_tasks=json.get_dealer_task_name('prapor'), therapist_tasks=json.get_dealer_task_name('Therapist'),
        skier_tasks=json.get_dealer_task_name('Skier'), peacekeeper_tasks=json.get_dealer_task_name('Peacekeeper'),
        mechanic_tasks=json.get_dealer_task_name('Mechanic'), ragman_tasks=json.get_dealer_task_name('Ragman'), jaeger_tasks=json.get_dealer_task_name('Jaeger'))

@app.route('/task/item/', methods=['GET','POST'])
def task_item():
    if request.method == 'GET':
        return render_template('task_setting.html')
    else:
        tasks_no_symbol = []
        tasks = request.form.getlist('task')
        for task in tasks:
            tasks_no_symbol.append(task.replace('_',' '))
        remain_tasks = json.get_sa_tasks(tasks_no_symbol)
        tasks_item = json.get_task_item_sum(remain_tasks)
        return render_template('task_item.html', tasks_item=tasks_item)

if __name__ == "__main__":
    app.run(debug=True)