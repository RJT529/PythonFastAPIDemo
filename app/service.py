from enums import SortingOptions, Rating
from typing import Optional
from fastapi import HTTPException
from repo import CourseRepo

class CourseService:
    def get_courses(self,sort_by: SortingOptions = SortingOptions.ALPHABETICAL, domain: Optional[str] = None):
        courses = CourseRepo().get_courses()
        if domain:
            courses = [course for course in courses if domain.lower() in [d.lower() for d in course.domain]]
        if sort_by == SortingOptions.ALPHABETICAL:
            courses = sorted(courses, key=lambda course: course.name)
        elif sort_by == SortingOptions.DATE:
            courses = sorted(courses, key=lambda course: course.date, reverse=True)
        elif sort_by == SortingOptions.RATING:
            courses = sorted(courses, key=lambda course: course.ratings, reverse=True)
        return courses
    
    def get_course_overview(self, course_name: str):
        course = CourseRepo().get_courses(course_name)
        if len(course) > 0: 
            return {"overview": course[0].description}
        raise HTTPException(status_code=404, detail="Course not found")
    
    def get_chapter_info(self, course_name: str, chapter_index : int):
        courses = CourseRepo().get_courses(course_name)
        if len(courses) > 0 :
            course = courses[0]
            chapters = course.chapters
            if chapter_index < len(chapters):
                return chapters[chapter_index]
            else:
                raise HTTPException(status_code=404, detail="Chapter not found")
        raise HTTPException(status_code=404, detail="Course not found")
    
    def update_course_rating(self, course_name: str, chapter_index: int, rating: Rating):
        courses = CourseRepo().get_courses(course_name)
        if len(courses) > 0 :
            course = courses[0]
            chapters = course.chapters
            if chapter_index < len(chapters):
                chapter_id = f"{course_name}_{chapter_index}"
                if rating == Rating.POSITIVE:
                    print(course.ratings)
                    course.ratings[chapter_id] = course.ratings.get(chapter_id, 0) + 1
                elif rating == Rating.NEGATIVE:
                    course.ratings[chapter_id] = course.ratings.get(chapter_id, 0) - 1
                CourseRepo().update_course_rating(course_name,course.ratings)                   
                return {"ratings": course.ratings}
            else:
                raise HTTPException(status_code=404, detail="Chapter not found")
        raise HTTPException(status_code=404, detail="Course not found")
    
    