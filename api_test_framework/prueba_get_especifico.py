import requests

from _all import BASE_URL


def test_get_single_post():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert "userId" in post
    assert "title" in post
    assert "body" in post
