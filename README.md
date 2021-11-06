# Kanban board Submission

## About The Project
This is my first ever Web Application development. I used Flask to build Kanban board that lists tasks with the following details:
* Task-id: indicates the order in which a task was added
* Task-title: brief description of the task
* Task-status: one of To-do, Doing, Done
* Task-date: date when the task was added

The structure of this submission is:
```
02_KANBAN
│   README.md
│   requirements.txt    
│   app.py
│   test.py
└───templates
    │   base.html
```

## Get Started
### Installation
This application was built and tested on Windows machine. For Windows users, use the following command to run the application.
```python3
python -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python app.py
```

### Pytest
Please note that this test uses **pytest**, not **unittest**.
```python3
python -m pytest test.py
```

## Built With
This Web Applicaiton was built by [Flask](https://flask.palletsprojects.com/en/0.12.x/).

## References
[Adding Tests with Pytest](http://www.marknagelberg.com/deploying-and-maintaining-a-web-app-part-3-adding-tests-with-pytest/)\
[Python Flask Beginner Tutorial](https://www.youtube.com/watch?v=yKHJsLUENl0)