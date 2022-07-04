from django.shortcuts import  redirect, render
from django.views.generic import TemplateView, View

from Project_Team_App.models import Technology, Request_technology, add_employee, time_schedule, trainer_reg, \
    recorded_class, upload_notes, Questions, Answers, chat


class IndexView(TemplateView):
    template_name = 'employee/employee_index.html'

class View_Technology(TemplateView):
    template_name = 'employee/view_technology.html'
    def get_context_data(self, **kwargs):
        context = super(View_Technology,self).get_context_data(**kwargs)
        tech = Technology.objects.filter(status='addedd')
        context['tech']=tech
        return context

class Request_Technology(View):
    def dispatch(self, request, *args, **kwargs):
        id2 = request.GET['id2']
        c=int(id2)
        id1=self.request.user.id
        employee=add_employee.objects.get(user_id=id1)
        print(employee,'qqqqqqqqqqqqqqqqqqqq')
        b=employee.id
        print(b,'rrrrrrrrrrrrrrrrr')
        tech = Technology.objects.get(pk=c)
        tech.status1='Requested'
        tech.save()
        request_tech=Request_technology()
        request_tech.employee_id=b
        request_tech.technology_id=c
        request_tech.status='requested'
        request_tech.save()

        return render(request,'employee/employee_index.html',{'messages':"Technology Requested"})

class View_Schedule(TemplateView):
    template_name = 'employee/view_schedule.html'
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        employee=add_employee.objects.get(user_id=id1)
        id2=employee.id
        tech=Request_technology.objects.get(employee_id=id2)
        name=tech.technology.technology_name

        context = super(View_Schedule,self).get_context_data(**kwargs)
        view_time_schedule = time_schedule.objects.filter(technology_name=name)
        context['view_time_schedule']=view_time_schedule
        return context

class View_Recorded_Video(TemplateView):
    template_name = 'employee/view_recorded_video.html'
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        employee=add_employee.objects.get(user_id=id1)
        id2=employee.id
        tech=Request_technology.objects.get(employee_id=id2)
        name=tech.technology.technology_name
        a=trainer_reg.objects.get(technology=name)
        b=a.id

        context = super(View_Recorded_Video,self).get_context_data(**kwargs)
        view_video = recorded_class.objects.filter(trainer_id=b)
        context['view_video']=view_video
        return context

class View_Notes(TemplateView):
    template_name = 'employee/view_notes.html'
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        employee=add_employee.objects.get(user_id=id1)
        id2=employee.id
        tech=Request_technology.objects.get(employee_id=id2)
        name=tech.technology.technology_name
        a=trainer_reg.objects.get(technology=name)
        b=a.id

        context = super(View_Notes,self).get_context_data(**kwargs)
        view_note = upload_notes.objects.filter(trainer_id=b)
        context['view_note']=view_note
        return context

class View_Quiz(TemplateView):
    template_name = 'employee/view_questions.html'
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        employee=add_employee.objects.get(user_id=id1)
        id2=employee.id
        tech=Request_technology.objects.get(employee_id=id2)
        name=tech.technology.technology_name
        i=Questions.objects.get(technology__technology_name=name)
        context = super(View_Quiz,self).get_context_data(**kwargs)
        context['i']=i
        return context

    def post(self , request,*args,**kwargs):
        id1=self.request.user.id
        employee=add_employee.objects.get(user_id=id1)
        id3=employee.id
        print(id3)
        id2=request.POST['id2']
        Question1=request.POST['question1']
        Option1 = request.POST['options1']
        print(1111111111111111111111111,Option1)
        Question2=request.POST['question2']
        Option2 = request.POST['options2']
        print(1111111111111111111111111,Option2)
        Question3=request.POST['question3']
        Option3 = request.POST['options3']
        print(1111111111111111111111111,Option3)
        Question4=request.POST['question4']
        Option4 = request.POST['options4']
        print(1111111111111111111111111,Option4)
        Question5=request.POST['question5']
        Option5 = request.POST['options5']
        print(1111111111111111111111111,Option5)

        paper = Answers()
        paper.emoployee_id=id3
        paper.qns_id=id2
        paper.Question1=Question1
        paper.answer1=Option1
        paper.Question2=Question2
        paper.answer2=Option2
        paper.Question3=Question3
        paper.answer3=Option3
        paper.Question4=Question4
        paper.answer4=Option4
        paper.Question5=Question5
        paper.answer5=Option5
        paper.status='submited'
        paper.save()

        return render(request,'employee/employee_index.html',{'messages':"Successfully Supmited"})

class View_Answer(TemplateView):
    template_name = 'employee/view_answer.html'
    def get_context_data(self, **kwargs):
        id=self.request.user.id
        employee=add_employee.objects.get(user_id=id)
        id2=employee.id
        context = super(View_Answer,self).get_context_data(**kwargs)
        tech = Answers.objects.get(emoployee_id=id2)
        context['tech']=tech
        return context

class Chat(TemplateView):
    template_name = 'employee/chat.html'
    def post(self , request,*args,**kwargs):
        message=request.POST['message']
        date=request.POST['date']
        id=self.request.user.id
        employee=add_employee.objects.get(user_id=id)
        id2=employee.id
        chat_mess=chat()
        chat_mess.employee_id=id2
        chat_mess.message=message
        chat_mess.date=date
        chat_mess.status='addedd'
        chat_mess.save()
        return render(request,'employee/employee_index.html',{'messages':"message send"})

class View_Reply(TemplateView):
    template_name = 'employee/view_reply.html'
    def get_context_data(self, **kwargs):
        id=self.request.user.id
        employee=add_employee.objects.get(user_id=id)
        id2=employee.id
        context = super(View_Reply,self).get_context_data(**kwargs)
        view_message = chat.objects.get(emoployee_id=id2)
        context['view_message']=view_message
        return context











