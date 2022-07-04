from django.urls import path

from Project_Team_App.employee_views import IndexView, View_Technology, Request_Technology, View_Schedule, \
    View_Recorded_Video, View_Notes, View_Quiz, View_Answer, Chat, View_Reply

urlpatterns =[
    path('',IndexView.as_view()),
    path('view_technology',View_Technology.as_view()),
    path('request_technology',Request_Technology.as_view()),
    path('view_schedule',View_Schedule.as_view()),
    path('recorded_video',View_Recorded_Video.as_view()),
    path('view_notes',View_Notes.as_view()),
    path('view_question',View_Quiz.as_view()),
    path('view_answer',View_Answer.as_view()),
    path('chat',Chat.as_view()),
    path('view_reply',View_Reply.as_view())

]
def urls():
      return urlpatterns,'employee', 'employee'