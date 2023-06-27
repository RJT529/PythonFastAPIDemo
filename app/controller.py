from fastapi import FastAPI, Query, Body, HTTPException
from enums import SortingOptions
from typing import Optional
from service import CourseService
from dto import Course, Chapter, Ratings, Overview
app = FastAPI()

@app.get("/courses", response_model=list[Course])
def get_courses_endpoint(sort_by: SortingOptions = Query(SortingOptions.ALPHABETICAL, description="Sorting option"),
                        domain: Optional[str] = Query(None, description="Filter courses by domain")):
    return CourseService().get_courses(sort_by, domain)

@app.get("/course/overview", response_model=Overview)
def get_course_overview_endpoint(course_name: str = Query(None, description="Name of the course")):
    return CourseService().get_course_overview(course_name)

@app.get("/course/chapter/", response_model=Chapter)
def get_chapter_info_endpoint(course_name: str = Query(None, description="Name of the course"),
                              chapter_index: int = Query(None, description="Chapter Index")):
    return CourseService().get_chapter_info(course_name, chapter_index)

@app.post("/course/rating", response_model=Ratings)
def update_course_rating_endpoint(payload: dict = Body(...)):
    return CourseService().update_course_rating(payload["course_name"], payload["chapter_index"], payload["rating"])
