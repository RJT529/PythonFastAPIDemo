import json
from fastapi.testclient import TestClient
from controller import app

client = TestClient(app)

def test_get_courses_endpoint():
    response = client.get("/courses")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0

def test_get_course_overview_endpoint():
    response = client.get("/course/overview?course_name=Computer Vision Course")
    assert response.status_code == 200
    overview = response.json()
    assert len(overview) > 0

def test_get_chapter_info_endpoint():
    response = client.get("/course/chapter?course_name=Computer Vision Course&chapter_index=0")
    assert response.status_code == 200
    chapter = response.json()
    assert chapter["name"] == "Introduction to Convolutional Neural Networks for Visual Recognition"

def test_update_course_rating_endpoint():
    response = client.post("/course/rating", json={
                                                    "course_name": "Computer Vision Course",
                                                    "chapter_index": 2,
                                                    "rating": "positive"
                                                })
    assert response.status_code == 200
    updated_course = response.json()
    assert len(updated_course) > 0

def test_invalid_endpoint():
    response = client.get("/invalid-endpoint")
    assert response.status_code == 404
