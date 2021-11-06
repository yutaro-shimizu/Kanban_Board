from app import app
from datetime import datetime

app.testing = True
client = app.test_client()

# unit testing
def test_render() -> None:
    "test the page connects and renders fine"
    response = client.get('/')
    assert response.status_code == 200
    assert b"Kanban Board" in response.data

def test_post():
    "ensure that a task is added into the database"
    response = client.post('/add',
                            data={'id': '1',
                                    'title': 'Finish PCW',
                                    'complete': 'To do',
                                    'date':datetime.now()},
                            follow_redirects=True)
    assert b'1' in response.data
    assert b'Finish PCW' in response.data
    assert b'To do' in response.data