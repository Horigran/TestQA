import requests

baseurl = "https://jsonplaceholder.typicode.com/posts"

def test_get_all():
    response = requests.get(baseurl)
    assert response.status_code == 200

def test_check_posts():
    response = requests.get(baseurl)
    data = response.json()
    assert len(data) == 100

def test_create_post_payload():
    payload = {
        "title": "breaking bad",
        "body": "I am the cook",
        "userId": 1
    }
    response = requests.post(baseurl, json=payload)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]

def test_get_post_404():
    response = requests.get(f"{baseurl}/34567543456")
    assert response.status_code == 404