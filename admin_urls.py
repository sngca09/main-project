

from django.urls import path

from Project_Team_App.admin_views import IndexView, Add_Employee, View_Employee, Remove_Employee, \
     Add_Technology, Remove_Technology, Approve_Trainer, ApproveView, View_Request, Approve_Request, Time_Schedule, \
    Time_Schedule_Trainer, View_Time_Schedule, Update_Schedule, View_Trainer, Add_Quizz, Add_Quizz_Qns, View_Quizz, \
    View_Quiz_Qns, View_Answers, View_Emp_Ans, View_Employee_Answer

urlpatterns =[
    path('',IndexView.as_view()),
    path('add_employee',Add_Employee.as_view()),
    # path('add_trainer',Add_Trainer.as_view()),
    path('view_employee',View_Employee.as_view()),
    path('remove_employee',Remove_Employee.as_view()),
    path('approve_trainer',Approve_Trainer.as_view()),
    path('view_trainer',View_Trainer.as_view()),
    path('add_technology',Add_Technology.as_view()),
    path('remove_technology',Remove_Technology.as_view()),
    path('approve',ApproveView.as_view()),
    path('view_request',View_Request.as_view()),
    path('approve_request',Approve_Request.as_view()),
    path('time_schedule',Time_Schedule.as_view()),
    path('time_schedule_trainer',Time_Schedule_Trainer.as_view()),
    path('view_time_schedule',View_Time_Schedule.as_view()),
    path('update_schedule',Update_Schedule.as_view()),
    path('add_quiz',Add_Quizz.as_view()),
    path('add_quizz_qns',Add_Quizz_Qns.as_view()),
    path('view_quiz',View_Quizz.as_view()),
    path('view_quizz_qns',View_Quiz_Qns.as_view()),
    path('view_ans',View_Answers.as_view()),
    path('view_emp_ans',View_Emp_Ans.as_view()),
    path('view_employee_answer',View_Employee_Answer.as_view())

]
def urls():
      return urlpatterns,'admin', 'admin'