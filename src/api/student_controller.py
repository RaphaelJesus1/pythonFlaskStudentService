from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.student_serializer import student_request, student_result, student_schooltests_result
from src.services.student_service import create, change, delete, get, getStudents
 

ns = api.namespace('api/student', description='Operations related to students')


@ns.route('')#refine rota
class StudentCollection(Resource):
    @api.expect(student_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(student_result)#define resultado da metodo 
    def post(self):
        """
        Create a new student
        """ 
        student = create(request.json)
        return student
    
    @api.marshal_with(student_result)
    def get(self):
        """
        Get students
        """ 
        students = getStudents()
        return students

 

@ns.route('/<int:id>')
class StudentIDCollection(Resource): 
    @api.marshal_with(student_schooltests_result)
    def get(self, id):
        """
        Get student by ID
        """ 
        student = get(id)
        return student 


    @api.expect(student_request)
    @api.marshal_with(student_result)
    def put(self, id):
        """
        Change student by ID
        """ 
        student = change(id,request.json)
        return student 
 
    @api.marshal_with(student_result)
    def delete(self, id):
        """
        Delete student by ID
        """ 
        student = delete(id)
        return student 