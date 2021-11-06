from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Kanban(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Integer)
    date = db.Column(db.DateTime)

@app.route('/')
def index():
    #show all todos
    todo_list = Kanban.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    # add new task
    title = request.form.get("title")
    new_todo = Kanban(title=title, complete=1, date=datetime.now())
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    # update task
    todo = Kanban.query.filter_by(id=todo_id).first()
    if todo.complete < 3:
        todo.complete += 1
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # add new task
    todo = Kanban.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)