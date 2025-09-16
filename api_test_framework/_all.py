import requests

from data import BASE_URL


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    # Validar la estructura de un post individual
    first_post = posts[0]
    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post
