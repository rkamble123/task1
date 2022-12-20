from django.urls import path
from . import views

urlpatterns = [
    # path('log_in',views.log_in.as_view()),
    # path('log_out',views.log_out.as_view()),
    # path('user_acc',views.user_acc.as_view()),
    # path('admin_acc',views.admin_acc.as_view()),


    path('get_user/',views.user_api.as_view()),
    path('add_user/<int:pk>',views.user_api.as_view()),
    # path('get_all_course/',views.get_all_course),
    # path('add_course/',views.add_course),
    # path('get_course/<int:pk>',views.get_course),
    path('topic_api/',views.topic_api.as_view()),
    path('add_topics/',views.topic_api.as_view()),
    path('course_api/',views.course_api.as_view()),


]