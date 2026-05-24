from api_calls import app
import pytest


def test_all_calls():
    client = app.test_client()
    response = client.get('/calls')
    assert response.status_code == 200

def test_one_call_by_id():
    client = app.test_client()
    response = client.get('/calls/3')
    response1 = client.get('/calls/15')
    assert response.status_code == 200  
    assert response1.status_code == 404  

def test_archive_call():
    client = app.test_client()
    response = client.patch('/calls/2/archive',json={"is_archived":True})
    assert response.status_code == 200
    response1 = client.patch('/calls/20/archive',json={"is_archived":False})
    assert response1.status_code == 404

def test_add_notes():
    client = app.test_client()
    response = client.post('/calls/3/notes',json={"note":"This is a note"})
    assert response.status_code == 201  
  

