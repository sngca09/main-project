from django.urls import path

from Project_Team_App.trainer_views import IndexView, View_Schedule, Upload_Notes, Add_Recorded_Class, Chat

urlpatterns =[
    path('',IndexView.as_view()),
    path('view_schedule',View_Schedule.as_view()),
    path('upload_notes',Upload_Notes.as_view()),
    path('recorded_class',Add_Recorded_Class.as_view()),
    path('chat',Chat.as_view())


]
def urls():
      return urlpatterns,'trainer', 'trainer'