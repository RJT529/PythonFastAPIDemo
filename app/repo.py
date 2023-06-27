from dto import Course
from mongoClient import MongoClient

class CourseRepo:
    def get_courses(self,course_name=None):
        filter_query={}
        if course_name: 
            filter_query = {'name': course_name}
        data = MongoClient.collection.find(filter_query)
        courses = [Course(**document) for document in data]
        return courses
    
    def update_course_rating(self, course_name, course_rating):
        filter_query = {'name': course_name}
        update_query = {'$set': {'ratings': course_rating}}
        MongoClient.collection.update_one(filter_query, update_query) 
