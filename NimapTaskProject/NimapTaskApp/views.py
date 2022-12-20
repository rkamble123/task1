from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from .models import CourseModel,UserModel,TopicsModel
from .serializers import UserSerializer,TopicSerializer,CourseSerializer 
from django.http import JsonResponse,HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.utils.decorators import method_decorator

# Create your views here.


class user_api(View):

    def get(self,request,pk):
        print(type(pk))
        user = UserModel.objects.get(id=pk)
        serialized_data = UserSerializer(user)
        return JsonResponse(serialized_data.data,safe= False)


    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = UserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"msg":"Data Created"})
        return HttpResponse({'msg':'Something Went Wrong'})
        



@method_decorator(csrf_exempt,name='dispatch')
class course_api(View):
   
    def get(self,request,*args,**xargs):
        data = CourseModel.objects.all()
        serialized_data = CourseSerializer(data,many=True)
        return JsonResponse(serialized_data.data,safe= False)
    
    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = CourseSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Data Created"},safe=False)
        return JsonResponse({'msg':'Something Went Wrong'},safe=False)
    
    def put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id=parsed_data.get('id')
        course_data = CourseModel.objects.get(id=id)
        serialized_data = CourseSerializer(course_data,data = parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({"msg":"Data Updated"},safe=False)
        return JsonResponse({'msg':'Something Went Wrong'},safe=False)
        
    def patch(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id=parsed_data.get('id')
        course_data = CourseModel.objects.get(id=id)
        serialized_data = CourseSerializer(course_data,data = parsed_data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({"msg":"Data Altered"},safe=False)
        return JsonResponse({'msg':'Something Went Wrong'},safe=False)

    def delete(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id=parsed_data.get('id')
        delete_data = CourseModel.objects.get(id=id)
        delete_data.delete()
        return JsonResponse({"msg":"Data Altered"},safe=False)
    


@method_decorator(csrf_exempt,name='dispatch')
class topic_api(View):
    def get(self,request):
        data = TopicsModel.objects.all()
        serialized_data = TopicSerializer(data,many=True)
        return JsonResponse(serialized_data.data,safe= False)
        

    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = TopicSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Data added Successfully"},safe=False)
        return JsonResponse({'msg':'Something Went Wrong'},safe=False)


    def put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id=parsed_data.get('id')
        course_data = TopicsModel.objects.get(id=id)
        serialized_data = TopicSerializer(course_data,data = parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({"msg":"Data Changed"},safe=False)
        return JsonResponse({'msg':'Something Went Wrong'},safe=False)


    def patch(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id=parsed_data.get('id')
        course_data = TopicsModel.objects.get(id=id)
        serialized_data = TopicSerializer(course_data,data = parsed_data,partial = True)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({"msg":"Data Altered"},safe=False)
        return JsonResponse({'msg':'Something Went Wrong'},safe=False)

    
    def delete(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id')
        delete_data = TopicsModel.objects.get(id=id)
        delete_data.delete()
        return JsonResponse({"msg":"Data Deleted"},safe=False)
    