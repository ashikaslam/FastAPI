import pytest
from rest_framework.test import APIClient
from blog.models import Post

@pytest.mark.django_db
def test_create_post():
    client = APIClient()
    data = {"title": "Test Title", "content": "Test Content"}
    response = client.post("/api/posts/", data)
    assert response.status_code == 201
    assert Post.objects.count() == 1
