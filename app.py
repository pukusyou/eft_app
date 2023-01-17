from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('mainpage.html')

@app.route('/task/', methods=['GET', 'POST'])
def task_setting():
    return render_template('task_setting.html')

if __name__ == "__main__":
    app.run(debug=True)