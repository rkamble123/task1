from rest_framework import serializers
from .models import UserModel , TopicsModel , CourseModel

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self,valid_data):
        return UserModel.objects.create(**valid_data)



class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseModel
        fields = '__all__'

    def update(self, instance, validated_data):
        print(instance.course_name)
        instance.course_name = validated_data.get('course_name',instance.course_name)
        print(instance.course_name)
        instance.updated_date = validated_data.get('updated_date',instance.updated_date)
        print(instance.updated_date)
        instance.save()
        return instance


    def create(self,valid_data):
        return CourseModel.objects.create(**valid_data)



class TopicSerializer(serializers.ModelSerializer):
    
    # course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = TopicsModel
        fields = '__all__'
        # read_only_fields = ('id','course_name')
        # fields = ('course_name','topic_name','topic_url')


        # category_name = serializers.RelatedField(source='category', read_only=True)

    def create(self,valid_data):
        return TopicsModel.objects.create(**valid_data)

    def update(self, instance, validated_data):
        instance.course_name = validated_data.get('course_name',instance.course_name)
        instance.topic_name = validated_data.get('topic_name',instance.topic_name)
        instance.topic_url = validated_data.get('topic_url',instance.topic_url)
        instance.updated_date = validated_data.get('updated_date',instance.updated_date)
        instance.save()
        return instance

    

 