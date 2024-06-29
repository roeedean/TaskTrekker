from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random
import string

# Initialize data structure with lists
data = {
    "lists": {
        "Default": pd.read_csv("to_do_list.csv")
    }
}

def assign_taskid(todos):
    task_ids = todos['task_id'].to_list()
    id_length = 5
    characters = string.ascii_lowercase + string.digits
    while True:
        new_id = 't'+''.join(random.choice(characters) for _ in range(id_length))
        if new_id not in task_ids:
            return new_id

def due_status(due_date):
    today = pd.Timestamp.now().strftime('%Y-%m-%d')
    if due_date == today:
        return 'Due today'
    elif due_date > today:
        return 'On time'
    elif due_date < today:
        return 'Past due'

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html", lists=data["lists"].keys())

@app.route('/list/<list_name>')
def index(list_name):
    sort_by = request.args.get('sort_by', '')
    show_completed = request.args.get('show_completed', 'false').lower() == 'true'
    
    if list_name not in data["lists"]:
        list_name = 'Default'

    todos = data["lists"][list_name]
    if not show_completed:
        todos = todos[todos['status'] != 'complete']

    if sort_by == 'name':
        todos_sorted = todos.sort_values(by='task')
    elif sort_by == 'due_status':
        todos_sorted = todos.sort_values(by='due_status')
    elif sort_by == 'due_date':
        todos_sorted = todos.sort_values(by='due_date')
    else:
        todos_sorted = todos

    todos_sorted['due_status'] = todos_sorted['due_date'].apply(due_status)
    return render_template("index.html", todos=todos_sorted.to_dict(orient='records'), sort_by=sort_by, lists=data["lists"].keys(), current_list=list_name, show_completed=show_completed)

@app.route('/add_task', methods=['POST'])
def add_task():
    item = request.form.get('task')
    create_date = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    due_date = request.form.get('due_date')
    status = 'open'
    current_list = request.form.get('list', 'Default')

    if current_list not in data["lists"]:
        current_list = 'Default'

    todos = data["lists"][current_list]
    task_id = assign_taskid(todos)
    due_status = ''
    todos.loc[len(todos)] = [item, create_date, due_date, status, task_id, due_status]
    todos.to_csv(f"{current_list}_to_do_list.csv", index=False)
    data["lists"][current_list] = todos
    return redirect(url_for('index', list_name=current_list))

@app.route('/update_todo/', methods=['POST'])
def update_todo():
    task_id = (request.form.get('task_id'))
    current_list = request.form.get('list', 'Default')

    if current_list not in data["lists"]:
        current_list = 'Default'

    todos = data["lists"][current_list]
    task_index = todos[todos['task_id'] == task_id].index[0]
    button_pushed = request.form.get('update_todo')
    if button_pushed == 'update':
        todos.at[task_index, 'due_date'] = request.form.get('due_date')
        todos.at[task_index, 'task'] = request.form.get('task')
    elif button_pushed == 'complete':
        todos.at[task_index, 'status'] = 'complete'
    else:
        pass
    todos.to_csv(f"{current_list}_to_do_list.csv", index=False)
    data["lists"][current_list] = todos
    return redirect(url_for('index', list_name=current_list))

@app.route('/create_list', methods=['POST'])
def create_list():
    list_name = request.form.get('list_name')
    if list_name and list_name not in data["lists"]:
        data["lists"][list_name] = pd.DataFrame(columns=["task", "created_date", "due_date", "status", "task_id", "due_status"])
    return redirect(url_for('index', list_name=list_name))

@app.route('/delete_list/<list_name>', methods=['POST'])
def delete_list(list_name):
    if list_name in data["lists"] and list_name != "Default":
        del data["lists"][list_name]
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)
